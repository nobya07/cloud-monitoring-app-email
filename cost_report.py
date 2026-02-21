import boto3
from datetime import date, timedelta
import smtplib

client = boto3.client('ce', region_name='ap-south-1')

today = date.today()
yesterday = today - timedelta(days=1)

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': str(yesterday),
        'End': str(today)
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost']
)

cost = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']

sender = "gajendrapunekar017@gmail.com"
receiver = "gajendrapunekar007@gmail.com"
password = "your_app_password"

message = f"""Subject: AWS Daily Cost Report

Yesterday AWS Cost: ${cost}
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()