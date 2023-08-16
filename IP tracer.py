#!/usr/bin/env python3
# Tool Name :- IP-Tracer
# Author :- Rajkumar Dusad
# Date :- 10/10/2018

import sys
import subprocess

def trace_own_ip():
    subprocess.run(["php", "modules/.tracem.php"])

def trace_target_ip(target_ip):
    subprocess.run(["php", "modules/.traceip.php", target_ip])

def update_ip_tracer():
    subprocess.run(["php", "modules/.update.php"])
    sys.exit()

def start_ip_tracer():
    subprocess.run(["php", ".IP-Tracer.php"])
    sys.exit()

def uninstall_ip_tracer():
    subprocess.run(["php", "modules/.uninstall.php"])
    sys.exit()

if len(sys.argv) < 2:
    print("Usage: python script.py [command]... [arguments]...")
    print(" Commands:")
    print(" -t <target_ip>      to trace target ip.")
    print(" -m                  to trace your own ip.")
    print(" -h                  to show help.")
    print(" -u                  to update ip-tracer.")
    print(" help                to show help.")
    print(" update              to update ip-tracer.")
    print(" start               to start ip-tracer menu.")
    sys.exit()

command = sys.argv[1]
if command == "-m":
    trace_own_ip()
elif command == "-t":
    if len(sys.argv) == 3:
        trace_target_ip(sys.argv[2])
    else:
        print("error: invalid arguments !!")
        print("use: python script.py -t <target_ip>")
elif command == "-u":
    update_ip_tracer()
elif command == "update":
    update_ip_tracer()
elif command == "start":
    start_ip_tracer()
elif command == "-rm":
    uninstall_ip_tracer()
else:
    print("Usage: python script.py [command]... [arguments]...")
    print(" Commands:")
    print(" -t <target_ip>      to trace target ip.")
    print(" -m                  to trace your own ip.")
    print(" -h                  to show help.")
    print(" -u                  to update ip-tracer.")
    print(" help                to show help.")
    print(" update              to update ip-tracer.")
    print(" start               to start ip-tracer menu.")
