sudo su
apt update -y
apt upgrade -y
apt install python3-pip python3 -y
apt install git screen -y
apt install libopus-dev -y
git clone https://github.com/rexjohannes/volumio-bot.git
cd volumio-bot
python3 -m pip install --upgrade -r requirements.txt
chmod +x run.sh
nano ./config/token.txt
bash run.sh
