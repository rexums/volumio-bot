sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt install python3-pip python3 -y
sudo apt install git screen -y
sudo apt install libopus-dev -y
git clone https://github.com/rexjohannes/volumio-bot.git
cd volumio-bot
sudo python3 -m pip install --upgrade -r requirements.txt
chmod +x run.sh
nano ./config/token.txt
bash run.sh
