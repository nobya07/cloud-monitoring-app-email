from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    return render_template("index.html",
                           cpu_metric=cpu_metric,
                           mem_metric=mem_metric)

app.run(host='0.0.0.0', port=5000)