from flask import Flask, render_template
import psutil
import shutil
import subprocess

app = Flask(__name__)

def safe_cmd(command):
    try:
        result = subprocess.getoutput(command)
        if any(bad in result.lower() for bad in ["not found", "error", "refused", "forbidden"]):
            return "N/A"
        return result.strip() or "N/A"
    except:
        return "N/A"

@app.route('/')
def home():

    cpu_metric  = round(psutil.cpu_percent(interval=1), 1)
    mem_metric  = round(psutil.virtual_memory().percent, 1)

    disk        = shutil.disk_usage("/")
    disk_metric = round((disk.used / disk.total) * 100, 1)

    net         = psutil.net_io_counters()
    bytes_sent  = round(net.bytes_sent / (1024 * 1024), 2)
    bytes_recv  = round(net.bytes_recv / (1024 * 1024), 2)

    pod_status  = safe_cmd("kubectl get pods -n gajendra --no-headers | awk '{print $3}'")
    restart     = safe_cmd("kubectl get pods -n gajendra --no-headers | awk '{print $4}'")
    node        = safe_cmd("kubectl get nodes --no-headers | awk '{print $2}'")
    uptime      = safe_cmd("uptime -p")

    return render_template("index.html",
                           cpu_metric=cpu_metric,
                           mem_metric=mem_metric,
                           disk_metric=disk_metric,
                           pod_status=pod_status,
                           restart=restart,
                           node=node,
                           uptime=uptime,
                           bytes_sent=bytes_sent,
                           bytes_recv=bytes_recv)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)