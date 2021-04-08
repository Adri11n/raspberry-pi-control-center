import json
import secrets
with open("settings.json", "r") as f:
    lol = json.load(f)
print("username = " + lol["username"] + "\n" + "password = " + lol["password"])
username = input("whats the username you want to use? > ")
password = input("whats the password you want to use? > ")
flask_secret = secrets.token_urlsafe(100)
conf_write = {
    "username": username,
    "password": password,
    "flask_secret": flask_secret
}
with open("settings.json", "w") as out:
    json.dump(conf_write, out)