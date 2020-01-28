#!/bin/bash
clear
echo -e "\e[1;32m Reborn \e[0m"
echo "Press Enter To Continue"
read a1
if [[ -s update.demoza ]];then
echo "All Requirements Found...."
else
echo 'Installing Requirements....'
echo .
echo .
apt install figlet toilet python curl -y
apt install python3-pip
pip install -r requirements.txt
echo Made By DEMOZA >demoza.speedx
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet Reborn
toilet -f mono12 -F border Demoza
echo -e "\e[4;34m   Created By Demoza \e[0m"
echo -e "\e[1;32m     Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[4;32m       YouTube Page: https://www.youtube.com/HarunMISTIK \e[0m"
echo " "
echo "Press 1  To  Start  SMS Bomber "
echo "Press 2  To  Update SMS Bomber "
echo "Press 99 To  Quit "
read ch
if [ $ch -eq 1 ];then
clear
python sms.py
exit 0
elif [ $ch -eq 2 ];then
clear
cd
rm -rf Reborn
git clone https://github.com/demoza/Reborn
cd Reborn
clear
echo "[+] Success Please Restart Tool"
exit 0
elif [ $ch -eq 3 ];then
clear
figlet Reborn
echo "Invaild Input Press Enter To Go Home"
read a3
./TBomb.sh
exit
elif [ $ch -eq 4 ];then
clear
figlet Reborn
echo "Invaild Input Press Enter To Go Home"
read a3
clear
elif [ $ch -eq 99 ];then
clear
echo -e "\e[1;31m"
figlet Reborn
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border DEMOZA
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/HarunMISTIK \e[0m"
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done
