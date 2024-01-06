#!usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import pyfiglet 
from colorama import Fore, Back, Style
os.system("sudo apt-get install figlet toilet")
os.system("sudo apt-get install figlet boxes")
os.system("sudo apt-get install figlet lolcat")
os.system("""git clone https://github.com/xero/figlet-fonts""")
os.system("""cd figlet-fonts""")
os.system("""sudo mv * /usr/share/figlet/""")
os.system("""cd ..""")
os.system("clear")
os.system("""figlet -f Bloody "QuirX" | sed 's/^/          /' | lolcat""")
os.system("""toilet -f ivrit 'UPDATER' | boxes -p h8 | lolcat""")

                                                 
print(Fore.LIGHTMAGENTA_EX + "\033[1m" + """ [1] ✓ Paket Yükseltme""" + "\033[1m")
print(Fore.LIGHTGREEN_EX + "\033[1m" + """ [2] ✓ Paket Güncelleme""" + "\033[1m")


                                                         
                                                        



islemnum=int(input("İslem Numarasını Giriniz: "))

if(islemnum==1):
    os.system("sudo apt-get upgrade")
else: 
    print(Fore.LIGHTGREEN_EX + "[+] Zaten Güncelleme Yapılmış")

if(islemnum==1):
    os.system("sudo apt-get update")
else:
    print(Fore.LIGHTGREEN_EX + "[+] Zaten Güncelleme Yapılmış")



       