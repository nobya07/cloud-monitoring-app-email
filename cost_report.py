import boto3
from datetime import date, timedelta
import smtplib
import os
import logging

# ── Logging setup ─────────────────────────────────────
logging.basicConfig(
    filename='/var/log/cost_report.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_aws_cost():
    try:
        client = boto3.client('ce', region_name='us-east-1')  # Cost Explorer only works in us-east-1

        today     = date.today()
        yesterday = today - timedelta(days=1)

        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': str(yesterday),
                'End':   str(today)
            },
            Granularity='DAILY',
            Metrics=['UnblendedCost']
        )

        cost = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
        unit = response['ResultsByTime'][0]['Total']['UnblendedCost']['Unit']
        return float(cost), unit, str(yesterday)

    except Exception as e:
        logging.error(f"Failed to fetch AWS cost: {e}")
        raise

def send_email(cost, unit, report_date):
    try:
        sender   = os.getenv("EMAIL_USER")
        receiver = os.getenv("EMAIL_RECEIVER", "gajendrapunekar017@gmail.com")
        password = os.getenv("EMAIL_PASS")

        if not sender or not password:
            raise ValueError("EMAIL_USER or EMAIL_PASS environment variable is not set")

        # Color indicator based on cost
        if cost > 10:
            status = "🔴 HIGH"
        elif cost > 5:
            status = "🟡 MODERATE"
        else:
            status = "🟢 NORMAL"

        message = f"""Subject: AWS Daily Cost Report - {report_date}
From: {sender}
To: {receiver}

━━━━━━━━━━━━━━━━━━━━━━━━━━
  AWS DAILY COST REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━

  Date        : {report_date}
  Total Cost  : {cost:.4f} {unit}
  Status      : {status}

━━━━━━━━━━━━━━━━━━━━━━━━━━
This is an automated report.
"""

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()

        logging.info(f"Email sent successfully. Cost: {cost:.4f} {unit}")
        print(f"✅ Email sent. Cost for {report_date}: {cost:.4f} {unit}")

    except Exception as e:
        logging.error(f"Failed to send email: {e}")
        raise

if __name__ == '__main__':
    try:
        cost, unit, report_date = get_aws_cost()
        send_email(cost, unit, report_date)
    except Exception as e:
        print(f"❌ Error: {e}")
        logging.error(f"Script failed: {e}")