from flask import Flask, render_template
import os
app = Flask(__name__)
@app.route("/")
def index():
    #temp = os.popen("cat /sys/class/thermal/thermal_zone*/temp").read()
    #temp = int(temp) / 1000
    #clock = os.popen('cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq').read()
    #clock = int(clock) / 1000
    #cpuusage = os.popen("vmstat | tail -1 | awk '{print $15}'").read()
    #cpuusage = 100 - int(cpuusage)
    uptime = os.popen("uptime").read().split("up")
    uptime2 = uptime[1].split(",")
    uptime = uptime[0] + "," + uptime2[1]
    print(uptime)

    return uptime
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

app.run()