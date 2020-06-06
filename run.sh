pkill -f 'app.py'
nohup python3 app.py & >> /home/pi/log 2>&1
