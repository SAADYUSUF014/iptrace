import os

class Set:
    def setup(self):
        system = os.getenv("system")  # Assuming the "system" variable is set elsewhere
        
        # Removing old files
        if system == "termux":
            os.system("rm -rf /data/data/com.termux/files/usr/share/IP-Tracer")
            os.system("rm -rf /data/data/com.termux/files/usr/bin/ip-tracer")
            os.system("rm -rf /data/data/com.termux/files/usr/bin/trace")
        elif system == "ubuntu":
            os.system("sudo rm -rf /usr/bin/ip-tracer")
            os.system("sudo rm -rf /usr/bin/trace")
            os.system("sudo rm -rf /usr/share/IP-Tracer")
        else:
            os.system("rm -rf /usr/bin/ip-tracer")
            os.system("rm -rf /usr/bin/trace")
            os.system("rm -rf /usr/share/IP-Tracer")
        
        # Adding bin file
        if system == "termux":
            os.system("mv -v modules/ip-tracer /data/data/com.termux/files/usr/bin/")
            os.system("mv -v modules/trace /data/data/com.termux/files/usr/bin/")
            os.system("chmod +x /data/data/com.termux/files/usr/bin/ip-tracer trace")
            os.system("chmod +x /data/data/com.termux/files/usr/bin/trace")
        elif system == "ubuntu":
            os.system("sudo mv -v modules/ip-tracer /usr/bin/")
            os.system("sudo mv -v modules/trace /usr/bin/")
            os.system("sudo chmod +x /usr/bin/ip-tracer")
            os.system("sudo chmod +x /usr/bin/trace")
        else:
            os.system("mv -v modules/ip-tracer /usr/bin/")
            os.system("mv -v modules/trace /usr/bin/")
            os.system("chmod +x /usr/bin/ip-tracer")
            os.system("chmod +x /usr/bin/trace")
        
        # Copy files from IP-Tracer to .IP-Tracer directory
        if system == "termux":
            os.system("mkdir /data/data/com.termux/files/usr/share/IP-Tracer")
            os.system("chmod +x * *.* .*.*")
            os.system("mv -v * *.* .*.* /data/data/com.termux/files/usr/share/IP-Tracer/")
        elif system == "ubuntu":
            os.system("sudo mkdir /usr/share/IP-Tracer/")
            os.system("sudo chmod +x * *.* .*.*")
            os.system("sudo mv -v * *.* .*.* /usr/share/IP-Tracer/")
        else:
            os.system("mkdir /usr/share/IP-Tracer")
            os.system("chmod +x * *.* .*.*")
            os.system("mv -v * *.* .*.* /usr/share/IP-Tracer/")
        
        # Removing IP-Tracer directory
        if system == "termux":
            os.system("cd .. && rm -rf IP-Tracer")
        elif system == "ubuntu":
            os.system("cd .. && sudo rm -rf IP-Tracer")
        else:
            os.system("cd .. && rm -rf IP-Tracer")

    def logo(self):
        os.system("clear")
        print('''


      _ ____    _
     (_)  _ \  | |_ _ __ __ _  ___ ___ _ __
     | | |_) | | __| '__/ _` |/ __/ _ \ '__|
     | |  __/  | |_| | | (_| | (_|  __/ |
     |_|_|      \__|_|  \__,_|\___\___|_|


    }--------------------------------------{
 }------------- Track IPLocation -------------{
    }--------------------------------------{

        ''')

        if os.path.exists("/usr/bin/ip-tracer") or os.path.exists("/data/data/com.termux/files/usr/bin/ip-tracer"):
            print("\033[01;32m      IP-Tracer installed Successfully !!!\033[00m\n")
            print('''
 ----------------------------------------------
|         \033[01;36mcommand\033[01;37m       |        \033[01;36mUse\033[01;37m           |
 ----------------------------------------------
| \033[01;32mtrace -m\033[01;37m              | \033[01;33mTrack your IP\033[01;37m        |
| \033[01;32mtrace -t <traget-ip>\033[01;37m  | \033[01;33mTrack IP\033[01;37m             |
| \033[01;32mtracer --help\033[01;37m         | \033[01;33mFor more information\033[01;37m |
 ----------------------------------------------

\033[01;31mNote :- ip-api will automatically ban any IP addresses doing over 150 requests per minute.\033[00m
''')
        else:
            print("\n\n\033[01;31m  Sorry IP-Tracer is not installed !!!\033[00m")

a = Set()
a.setup()
a.logo()
