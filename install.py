import os

if os.path.exists('/usr/lib/sudo'):
    if not os.path.exists('/usr/bin/php'):
        os.system('sudo apt-get update')
        os.system('sudo apt-get upgrade -y')
        os.system('sudo apt-get install php -y')
        os.system('sudo apt-get install php5 -y')
else:
    if os.path.exists('/usr/bin'):
        if not os.path.exists('/usr/bin/php'):
            os.system('apt-get update')
            os.system('apt -get upgrade -y')
            os.system('apt-get install php -y')
            os.system('apt-get install php5 -y')

if not os.path.exists('/usr/bin'):
    if not os.path.exists('/data/data/com.termux/files/usr/bin/php'):
        os.system('pkg update')
        os.system('pkg upgrade -y')
        os.system('pkg install php -y')
        os.system('pkg install php5 -y')

os.system('php .setup.php')
exit()
