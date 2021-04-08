from flask import Flask, render_template
import os
import json
app = Flask(__name__)
@app.route("/")
def index():
    with open("english.lang.json") as conf:
        language = json.load(conf)

    temp = os.popen("cat /sys/class/thermal/thermal_zone*/temp").read()
    temp = round(int(temp) / 1000, 1)
    clock = os.popen('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq').read()
    clock = round(int(clock) / 1000)
    cpuusage = os.popen("vmstat | tail -1 | awk '{print $15}'").read()
    cpuusage = 100 - int(cpuusage)
    uptime_row = os.popen("uptime").read().split("up")
    uptime = uptime_row[1].split(",")
    uptime = uptime[0] + "," + uptime[1]

    return render_template("index.html", TXT_CONFIRM= language["TXT_CONFIRM"], TXT_RUNTIME=language["TXT_RUNTIME"], uptime_finally=uptime, temperatur=temp, TXT_TEMPERATURE=language["TXT_TEMPERATURE"], cpuusage_final=cpuusage, TXT_USAGE=language["TXT_USAGE"], TXT_CLOCK=language["TXT_CLOCK"], clock_final=clock, TXT_RESTART_2=language["TXT_RESTART_2"], TXT_SHUTDOWN_2=language["TXT_SHUTDOWN_2"], TXT_SHUTDOWN_1=language["TXT_SHUTDOWN_1"], TXT_RESTART_1=language["TXT_RESTART_1"])
@app.route("/shutdown/<wich>")
def reboot(wich):
    if wich == "shutdown":
        os.system("sudo /sbin/shutdown -t 10")
        return render_template("shutdown.html")
    elif wich == "reboot":
        os.system("sudo /sbin/shutdown -r -t 10")
        return render_template("reboot.html")
    else:
        return "error"

app.run(host="192.168.2.100", debug=True)