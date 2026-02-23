from flask import Flask, render_template
import psutil
import shutil
import subprocess

app = Flask(__name__)

@app.route('/')
def home():

    # CPU Usage
    cpu_metric = psutil.cpu_percent()

    # Memory Usage
    mem_metric = psutil.virtual_memory().percent

    # Disk Usage
    disk = shutil.disk_usage("/")
    disk_metric = (disk.used / disk.total) * 100

    # Network Usage
    net = psutil.net_io_counters()
    bytes_sent = net.bytes_sent / (1024 * 1024)
    bytes_recv = net.bytes_recv / (1024 * 1024)

    # Pod Status
    pod_status = subprocess.getoutput("kubectl get pods --no-headers | awk '{print $3}'")

    # Restart Count
    restart = subprocess.getoutput("kubectl get pods -o jsonpath='{.items[*].status.containerStatuses[*].restartCount}'")

    # Node Status
    node = subprocess.getoutput("kubectl get nodes --no-headers | awk '{print $2}'")

    # System Uptime
    uptime = subprocess.getoutput("uptime -p")

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

app.run(host='0.0.0.0', port=5000)