sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt install python3-pip python3 -y
sudo apt install git screen -y
sudo apt install libopus-dev -y

git clone https://github.com/rexjohannes/volumio-bot.git VolumioBot -b main
cd VolumioBot
sudo python3 -m pip install --upgrade -r requirements.txt
chmod +x run.sh
clear

echo Enter BotToken now

sleep 3
nano ./config/token.txt
clear
echo Done! Starting...
echo To Exit press Str. + A + D
sleep 4
bash run.sh