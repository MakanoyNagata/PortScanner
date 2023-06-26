import socket
import subprocess
import sys
import os
import time

clear = lambda: os.system('clear')
sleep = lambda x: time.sleep(x)
open_ports = []

def error_banner(error):
    clear()
    sleep(0.1)
    subprocess.call(["figlet", "PortScanner"])
    print("AUTOR AND SCRIPTED by @makanoy0nagata")
    print("\nError: " + error)
    print("Present: sudo python3 port_scanner.py [ip] [ports]\n")
    exit()

def scan_loop(host, ports):
    clear()
    sleep(0.1)
    subprocess.call(["figlet", "PortScanner"])
    print("AUTOR AND SCRIPTED by @makanoy0nagata")
    print(f"\n Scanning {host} host...")
    print("------------------------------------------")
    print(" Open Ports: ")
    try:
        for port in range(24, ports):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"\t {port} is open")
                open_ports.append(port)
            s.close()
        print("")
    except Exception as e:
        print(e)

def save_open_ports(host):
    choice = input("\n Yo wanna save open ports in file? yes/no : ")
    if choice == "y" or choice == "yes":
        
        with open('open_ports.txt', 'a') as f:
            f.write("Scaned" + host + " host\n")
            f.write("Open Ports: ")
            for el in open_ports:
                f.write(str(el) + " ")
            f.write("\n----------------------------------\n")

    else:
        exit()


if len(sys.argv) == 1:

    clear()
    sleep(0.1)
    subprocess.call(["figlet", "PortScanner"])
    print("AUTOR AND SCRIPTED by @makanoy0nagata")
    print("\nPresent: sudo python3 port_scanner.py [ip] [ports]\n")
    exit()

elif len(sys.argv) == 2:

    if len(sys.argv[1].split(".")) == 1:
        
        error_banner("Error: Please enter target ip!")
    else:

        error_banner("Please enter port number for range!")

elif len(sys.argv) == 3:
    
    if len(sys.argv[1].split(".")) == 1:
        
        error_banner("Please enter ip for firts option! port is second option!")
    else:
        host = sys.argv[1]
        ports = int(sys.argv[2])
        scan_loop(host, ports)
        save_open_ports(host)
else:
    
    error_baner("Enter correct option!")

