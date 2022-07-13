#!/usr/bin/python
# -*- coding: utf-8 -*-
# g3nj1z

import sys
import os
import time
import signal
from time import sleep
from sys import argv
from platform import system


def sigint_handler(signum, frame):
    os.system("clear")
    print ("CTRL+C detected!")
    print(" \033[1;91m@Good bye !\033[1;m")
    sys.exit() 
 
signal.signal(signal.SIGINT, sigint_handler)

def logo():
    print ("""\033[1;91m

█████████████████████████████████████████████████
█─▄▄▄─█─▄▄─█─▄▄─█▄─▄███─▄▄▄▄█─▄▄▄─██▀▄─██▄─▀█▄─▄█
█─███▀█─██─█─██─██─██▀█▄▄▄▄─█─███▀██─▀─███─█▄▀─██
▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀
                    github.com/g3nj1z/coolscan
------First Step towards Website Hacking---------
\033[1;m
    """)

# options
def menu():
    logo()
    print("""

        Active Reconnaissance:
        1-) whois
        2-) dig
     
        Directory Busting:
        3-) Gobuster
        4-) Dirb

        HTTP Probing:
        5-) httpx

        Nmap Scans:
        6-) nmap vuln scan

        SSL Scanner
        7-) sslscan

        Vulnerability
        8-) default sqlmap
        9--) enumerate usernames wpscan
        10-) default nikto

        Exploit
        11-) Exploitdb

        Collection
        12-) External Pentest

        0-) Exit

        """)

def baslangic():
    menu()
    print("   Enter one of the options.")

    selection = input("root""\033[1;91m@coolscan:~$\033[1;m ")

    # whois
    if selection == "1":
        print(" Starting whois...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("whois "+url +" > whois.txt")
        os.system("whois "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # dig
    if selection =="2":
        print(" Starting dig...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("dig "+url +" > dig.txt")
        os.system("dig "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # BUG gobuster 
    if selection == "3":
        print(" Starting gobuster...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("gobuster -e -u "+url +" > gobuster.txt")
        os.system("gobuster -e -u "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # BUG dirb
    if selection == "4":
        print(" Starting dirb...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("dirb "+url +" > dirb.txt")
        os.system("dirb "+url)       
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # httpx
    if selection == "5":
        print(" Starting httpx...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("httpx "+url +" > httpx.txt")
        os.system("httpx "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # nmap vuln
    if selection == "6":
        print(" Starting nmap vuln scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("nmap -sV --script vuln "+url +" > nmapvuln.txt")
        os.system("nmap -sV --script vuln "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # sslscan
    if selection =="7":
        print(" Starting sslscan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("sslscan "+url +" > sslscan.txt")
        os.system("sslscan "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # sqlmap
    if selection =="8":
        print(" Starting sqlmap...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("sqlmap -u "+url +" > sqlmap.txt")
        os.system("sqlmap -u "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # wpscan
    if selection =="9":
        print(" Starting wpscan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("wpscan  --url "+url+" --enumerate u" +" > wpscan.txt")
        os.system("wpscan  --url "+url+" --enumerate u")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # nikto
    if selection =="10":
        print(" Starting nikto...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("nikto -h "+url +" > nikto.txt")
        os.system("nikto -h "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # exploitdb
    if selection =="11":
        print(" Starting searchsploit...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your exploit details")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("searchsploit "+url +" > exploitdb.txt")
        os.system("searchsploit "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # external pentest
    if selection =="12":
        print(" Starting external pentest...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = input("     Enter Your Destination: ")
        os.system("whois "+url +" > Xwhois.txt")    
        os.system("dig "+url +" > Xdig.txt")
        os.system("httpx "+url +" > Xhttpx.txt")
        os.system("nmap -sV --script vuln "+url +" > Xnmap.txt")

        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    if selection =="0":
        print(" \033[1;91mGoodbye !\033[1;m")
        sys.exit()

    else:
        print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
        time.sleep(2)
        baslangic()

# root permission
def rootkontrol():
    if os.geteuid()==0:
        baslangic()
    else:
        print("you need to be root to run this script")
        sys.exit()

rootkontrol()
#g3nj1z