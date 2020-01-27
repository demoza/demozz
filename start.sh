#!/bin/bash
clear
echo "Press Enter To Continue"
read a1
if [[ -s update.demoza ]];then
echo "All Requirements Found...."
else
echo 'Installing Requirements....'
echo .
echo .
pkg install tsu
apt install python3-pip
pkg install python
pip install requests
pip install colorama
echo Made By Demoza >update.demoza
echo Requirements Installed....
echo Press Enter To Continue...
read upd
fi
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
figlet Codanme:Reborn
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border Demoza
echo -e "\e[1;34m For Any Question Mail To Me!!\e[0m"
echo -e "\e[1;32m           Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/HarunMISTIK \e[0m"
echo " "
echo " "
echo "Press 1 To  Start SMS Bomber "
echo "Press 2 To  Update"
echo "Press 99 To  Exit"
read ch
if [ $ch -eq 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
python sms.py
rm *.xxx >/dev/null 2>&1
exit 0
elif [ $ch -eq 2 ];then
clear
cd 
rm -rf Reborn
clear
git clone https://github.com/demoza/Reborn/
cd Reborn
chmod +x start.sh
read a6
./start.sh
exit
elif [ $ch -eq 99 ];then
clear
echo -e "\e[1;31m"
figlet Reborn
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border Demoza
echo -e "\e[1;34m For Any Question Mail Me!!\e[0m"
echo -e "\e[1;32m           Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/HarunMISTIK \e[0m"
echo " "
exit 0
else
echo -e "\e[4;32m Invalid Input !! \e[0m"
echo "Press Enter To Go Home"
read a3
clear
fi
done