#!/bin/bash
clear
echo -e "\e[1;32m Reborn \e[0m"
echo " "
echo " "
echo "Press Enter To Continue..."
read a
if [[ -s update.demoza ]];then
echo " "
echo -e "\e[1;32m All Requirements Found... \e[0m"
else
echo " "
echo -e "\e[1;32m Please Wait While We Install Necessary Requirements... \e[0m"
echo " "
echo " "
apt update
apt upgrade
pip install requests
pkg install python
pip install colorama
echo " "
echo -e "\e[1;32m Requirements Installed Successfully...  \e[0m"
echo "This App Was Last Updated On"$date >update.demoza
echo "SuperDorker Was Created By SpeedX... Any Queries Mail harunbusiness@aol.com " >>update.demoza
fi
for (( start=5;start>=5;start++ ))
do
clear
echo -e "\e[1;32m"
figlet -f slant -c Reborn
echo -e "\e[1;34m Created By \e[0m"
toilet -f mono12 -F gay Demoza
echo -e "\e[4;34m Created By SpeedX \e[0m"
echo -e "\e[1;34m For Any Questions Mail Me!!!\e[0m"
echo -e "\e[1;32m             Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[4;32m  YouTube Channel: https://www.youtube.com/HarunMISTIK\e[0m"
echo " "
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
echo -e "\e[1;33m"
echo "Press 1 To Start Sms Bomber"
echo "Press 2 To Update "
echo "Press 99 to Exit "
read ch
if [ $ch -eq 1 ];then
clear
python sms.py
fi
done
fi
echo "100% Completed !!!"
echo "List Created For Dork: "$dork
echo "Vulnerable Sites Saved in FileName: SDList.txt"
echo " "
rm list*.txt
echo "Do You Want To View it Now (Y/N):"
read cho
if [ "$cho" = "Y" ] || [ "$cho" = "y" ] ;then
echo -e "\e[1;31mThis List Was Created By Super Dorker !!!"
echo " "
cat SDList.txt
echo " "
echo " "
echo "Press Enter To Go To Main Menu"
read a4
else
echo "Going Back to Main Menu..."
sleep 1
fi
elif [ $ch -eq 2 ];then
clear
pkg install git
echo -e "\e[1;34m Downloading Latest Files..."
git clone https://github.com/demoza/Reborn
if [[ -s SDorker/SDork ]];then
cd SDorker
cp -r -f * .. > temp
cd ..
rm -rf  Reborn >> temp
chmod +x start.sh
echo -e "\e[1;34m Press Enter To Continue.."
read a1
elif [ $ch -eq 3 ];then
clear
cd files
while true
do
clear
echo -e "\e[1;32m "
figlet -f slant -c S Reborn
echo -e "\e[1;34m Created By \e[0m"
toilet -f mono12 -F gay Demoza
echo -e "\e[4;34m Created By Demoza \e[0m"
echo -e "\e[1;34m For Any Questions Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[1;31m "
echo " "
echo "Press 1 Start Sms Bomber"
echo "Press 2 To Update "
echo "Press 99 To Exit "
read dc
if [ $dc -eq 1 ];then
python sms.py
elif [ $dc -eq 2 ];then
echo -e "\e[1;33mSome XSS Dorks"
echo " "
cat xss.demoza
echo " "
echo " "
echo "Press Enter To Go Back"
read a2
elif [ $dc -eq 3 ];then
echo -e "\e[1;33m"
echo " "
cat fi.demoza
echo " "
echo " "
echo "Press Enter To Go Back"
read a2
elif [ $dc -eq 4 ];then
break
else
echo "Invalid Input !!!"
sleep 2
fi
done
echo -e "\e[1;31m"
cd ..
elif [ $ch -eq 2];then
clear
pkg install git
echo -e "\e[1;34m Downloading Latest Files..."
git clone https://github.com/demoza/Reborn
if [[ -s SDorker/SDork ]];then
cd SDorker
cp -r -f * .. > temp
cd ..
rm -rf  Reborn >> temp
chmod +x start.sh
fi
echo -e "\e[1;32m Reborn Will Restart Now..."
echo -e "\e[1;32m All The Required Packages Will Be Installed..."
echo -e "\e[1;34m Press Enter To Proceed To Restart..."
read a6
./SDork
exit
elif [ $ch -eq 99 ];then
clear
toilet -f mono12 -F gay S Reborn
echo -e "\e[1;32m Created By "
figlet -f slant -c Demoza
echo " "
echo -e "\e[4;34m Created By Demoza \e[0m"
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/HarunMISTIK \e[0m"
echo " "
echo -e "\e[1;32m Support Me By Either Helping In Project Or Donating Small Amount To Me For That Contact Me By Mail\e[0m"
echo " "
echo " Press Enter To Continue..."
read a5
elif [ $ch -eq 6 ];then
start=0
else
echo -e "\e[4;32m Invalid Input !!! \e[0m"
echo "Press Enter To Go Home"
read a3
start=6
clear
fi
done
echo "Thanks For Using My Sms Bomber !!"
figlet -f slant -c Reborn
echo "Created By Demoza !!!!"
toilet -f mono12 -F gay Demoza
echo -e "\e[1;34m For Any Queries Mail Me!!!\e[0m"
echo -e "\e[1;32m           Mail: harunbusiness@aol.com \e[0m"
echo -e "\e[4;32m   YouTube Page: https://www.youtube.com/HarunMISTIK \e[0m"