#!/usr/bin/env python

import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: ip-tracer [command]... [arguments]...")
        print(" Commands:")
        print(" -t <target_ip>      to trace target ip.")
        print(" -m                  to trace your own ip.")
        print(" -h                  to show help.")
        print(" -u                  to update ip-tracer.")
        print(" help                to show help.")
        print(" update              to update ip-tracer.")
        print(" start               to start ip-tracer menu.")
        sys.exit(1)

    command = sys.argv[1]

    if command == "-m":
        os.system("php modules/.tracem.php")
    elif command == "-t":
        if len(sys.argv) == 3:
            os.system("php modules/.traceip.php " + sys.argv[2])
        else:
            print("error: invalid arguments !!")
            print("use: ip-tracer -t <target_ip>")
            sys.exit(1)
    elif command == "-u":
        os.system("php modules/.update.php")
        sys.exit(0)
    elif command == "update":
        os.system("php modules/.update.php")
        sys.exit(0)
    elif command == "start":
        os.system("php .IP-Tracer.php")
        sys.exit(0)
    elif command == "-rm":
        os.system("php modules/.uninstall.php")
        sys.exit(0)
    else:
        print("Usage: ip-tracer [command]... [arguments]...")
        print(" Commands:")
        print(" -t <target_ip>      to trace target ip.")
        print(" -m                  to trace your own ip.")
        print(" -h                  to show help.")
        print(" -u                  to update ip-tracer.")
        print(" help                to show help.")
        print(" update              to update ip-tracer.")
        print(" start               to start ip-tracer menu.")
        sys.exit(1)

if __name__ == "__main__":
    main()
