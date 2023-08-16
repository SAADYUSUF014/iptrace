import os
import subprocess

def logo():
    os.system("clear")
    print('''
\033[01;33m


\033[01;31m      _\033[01;33m ____    _
     \033[01;31m(_)\033[01;33m  _ \  | |_ _ __ __ _  ___ ___ _ __
     | | |_) | | __| '__/ _` |/ __/ _ \ '__|
     | |  __/  | |_| | | (_| | (_|  __/ |
     |_|_|      \__|_|  \__,_|\___\___|_|


   \033[01;37m}\033[01;31m----------------------------------------\033[01;37m{
}\033[01;31m-------------- \033[01;32mTrack IPLocation\033[01;31m --------------\033[01;37m{
   }\033[01;31m----------------------------------------\033[01;37m{

\033[00m
''')

def about():
    logo()
    print('''
         \033[01;33mTool Name \033[01;37m:- \033[01;36mIP-Tracer
         \033[01;33mAuthor \033[01;37m:- \033[01;36mRajkumar Dusad
         \033[01;33mPowered By \033[01;37m:- \033[01;36mAex Software's

 \033[01;33mIP-Tracer\033[01;32m is use \033[01;36mip-api \033[01;32mto retrieve any IP address information. Our system will automatically ban any IP addresses doing over 150 requests per minute.\033[00m
''')
    getact = input('  IP-Tracer >> ')
    menu()

def upd():
    logo()
    print("\n\033[01;32mUpdating IP-Tracer.........\033[01;37m\n\n")
    subprocess.run(["cd ~/ && git clone https://github.com/rajkumardusad/IP-Tracer.git"], shell=True)
    subprocess.run(["cd ~/ && sudo git clone https://github.com/rajkumardusad/IP-Tracer.git"], shell=True)
    subprocess.run(["cd ~/IP-Tracer && sh install"], shell=True)
    logo()
    print("\n\033[01;32m              IP-Tracer updated !!!\033[01;37m\n")
    menu()

def menu():
    logo()
    print("   \033[01;32m[ \033[01;37m1 \033[01;32m] \033[01;33mTrack IP Address.")
    print("   \033[01;32m[ \033[01;37m2 \033[01;32m] \033[01;33mTrack Your IP Address.")
    print("   \033[01;32m[ \033[01;37m3 \033[01;32m] \033[01;33mAbout us.")
    print("   \033[01;32m[ \033[01;37m4 \033[01;32m] \033[01;33mHelp.")
    print("   \033[01;32m[ \033[01;37m5 \033[01;32m] \033[01;33mUpdate IP-Tracer.")
    print("   \033[01;32m[ \033[01;37mx \033[01;32m] \033[01;33mExit \n\n\033[00m")
    inp = input('  IP-Tracer >> ')
    if inp == "x" or inp == "exit":
        print("\n\033[01;31m  Exiting .......\033[00m\n")
        print("\033[01;32m  Bye ....... :)\n\n\033[00m")
        exit()
    elif inp == "1":
        trac()
    elif inp == "2":
        tracm()
    elif inp == "3":
        about()
    elif inp == "4":
        help()
    elif inp == "5":
        upd()
    else:
        print("\n  \033[01;31mErr : Invalid Command \033[01;32m'%s'\033[00m" % inp)
        menu()

menu()
