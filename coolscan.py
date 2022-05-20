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
    print(" \033[1;91m@Good bye\033[1;m")
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
        whois
        dig
        goaltdns
        massdns
        puredns

        Hunting for Subdomain:
        subfinder
        assetfinder
        findomain
     
        Directory Busting:
        Gobuster
        Dirbuster
        Dirb
        Ffuf

        HTTP Probing:
        httpx

        Subdomain Takeover:
        subjack

        Nmap Scans:
        nmap vuln scan


        1-) nmap Vuln scan
        2-) sslscan
        3-) dig
        4-) default dirb
        5-) default sqlmap
        6-) enumerate usernames wpscan
        7-) default nikto
        8-) whois
        0-) Exit

        """)

def baslangic():
    menu()
    print("   Enter one of the options.")

    selection = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")

    # nmap vuln
    if selection == "1":
        print(" Starting nmap vuln scan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("nmap -sV --script vuln "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
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
    if selection =="2":
        print(" Starting sslscan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("sslscan "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
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
    if selection =="3":
        print(" Starting dig...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("dig "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # dirb
    if selection =="4":
        print(" Starting dirb...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("dirb "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
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
    if selection =="5":
        print(" Starting sqlmap...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("sqlmap -u "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
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
    if selection =="6":
        print(" Starting wpscan...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("wpscan  --url "+url+" --enumerate u")
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
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
    if selection =="7":
        print(" Starting nikto...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("nikto -h "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
        if selectionurl == "1":
            baslangic()
        if selectionurl == "2":
            print(" \033[1;91m@Good bye\033[1;m")
            sys.exit() 
        else:
            print(" Please enter one of the options in the menu. \n You are directed to the main menu.")
            time.sleep(2)
            baslangic()

    # whois
    if selection =="8":
        print(" Starting whois...")
        time.sleep(1)
        os.system("clear")
        logo()
        print(" Enter your IP address or example.com")
        print("")
        url = raw_input("     Enter Your Destination: ")
        os.system("whois "+url)
        print("\n \033[1;91m1-) Back to Main Menu \n 2-) Exit \033[1;m")
        selectionurl = raw_input("root""\033[1;91m@coolscan:~$\033[1;m ")
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
        print(" \033[1;91mGoodbye\033[1;m")
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
        print "you need to be root to run this script"
        sys.exit()

rootkontrol()
#g3nj1z