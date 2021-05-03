from flask import Flask, render_template
from flask_httpauth import HTTPDigestAuth
import os
import json
import psutil
import datetime
with open("settings.json", "r") as f_in:
    info = json.load(f_in)
app = Flask(__name__)
app.config['SECRET_KEY'] = info["flask_secret"]
auth = HTTPDigestAuth()
users = {
    info["username"]: info["password"],
}
@app.route("/")
def index():
    with open("english.lang.json") as conf:
        language = json.load(conf)

    temp = psutil.sensors_temperatures(["coretemp"][0][1])
    clock = round(psutil.cpu_freq()[0])
    cpuusage = psutil.cpu_percent(interval=1, percpu=False)
    uptime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%S:%M:%H %d-%m-%Y")

    return render_template("index.html", TXT_CONFIRM= language["TXT_CONFIRM"], TXT_RUNTIME=language["TXT_RUNTIME"], uptime_finally=uptime, temperatur=temp, TXT_TEMPERATURE=language["TXT_TEMPERATURE"], cpuusage_final=cpuusage, TXT_USAGE=language["TXT_USAGE"], TXT_CLOCK=language["TXT_CLOCK"], clock_final=clock, TXT_RESTART_2=language["TXT_RESTART_2"], TXT_SHUTDOWN_2=language["TXT_SHUTDOWN_2"], TXT_SHUTDOWN_1=language["TXT_SHUTDOWN_1"], TXT_RESTART_1=language["TXT_RESTART_1"])
@app.route("/shutdown/<wich>")
@auth.login_required
def reboot(wich):
    if wich == "shutdown":
        os.system("sudo sleep 5 && /sbin/shutdown now &")
        return render_template("shutdown.html")
    elif wich == "reboot":
        os.system("sudo sleep 5 && /sbin/shutdown -r now &")
        return render_template("reboot.html")
    else:
        return "error"
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None