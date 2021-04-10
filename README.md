# raspberry-pi-control-center
control panel for the raspberry pi written in python served with flask and forked/reritten from https://bitbucket.org/baldisos/raspberry-pi-control-panel
 python3 -m gunicorn --keyfile /root/key.pem --certfile /root/cert.pem --do-handshake-on-connect --ssl-version TLS -b 127.0.0.1:443 main:app -D
