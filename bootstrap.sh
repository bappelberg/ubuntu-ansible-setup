#/usr/bin/sh

sudo apt update
sudo apt upgrade -y

sudo apt install -y ssh
sudo systemctl enable --now ssh

if systemctl is-active --quiet ssh; then
	echo "SSH-service is now running"
else
	echo "SSH-service is not running"
fi

sudo apt install vim -y

hostname -I | cut -d' ' -f1
# 172.20.10.14