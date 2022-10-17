#!/usr/bin/python3
import subprocess
import datetime
import os
import platform
import getpass


if "windows" in platform.system().lower():
    try:
        print(
            """
            |----------------------------------------|
            |           Wifi Password v.1            |
            |   github: https://github.com/GarudaID  |
            |       Show your password wifi          |
            |----------------------------------------|
""")

        wifi_list = []
        wifi_dict = {}
        show_wifi_command = subprocess.run(
            "netsh wlan show profile ", shell=False, stdout=subprocess.PIPE
        )

        for line in show_wifi_command.stdout.decode("latin-1").splitlines():
            if "All" in line.replace(" ", ""):
                delim = ": "
                ssid = line[line.index(delim) + len(delim):]
                if " " in ssid:
                    ssid = '"{}"'.format(ssid)
                    wifi_list.append(ssid)
                else:
                    wifi_list.append(ssid)
        for wifi_details in wifi_list:
            show_wifi_password = subprocess.run(
                "netsh wlan show profile " + "name=" + wifi_details + " key=clear",
                shell=False,
                stdout=subprocess.PIPE,
            )
            for line in show_wifi_password.stdout.decode("latin-1").splitlines():
                if "Key Content" in line.replace("\r\n", "").strip():
                    delim = ": "
                    wifi_dict[wifi_details] = line[line.index(
                        delim) + len(delim):]
                else:
                    continue
        file = open(
            os.path.normpath(os.path.expanduser(
                "~/Desktop")).replace("\\", "\\\\")
            + "\\Wifi-"
            + str(datetime.datetime.now())
            .replace(":", "-")
            .replace(" ", "-")
            .split(".")[0]
            + ".txt",
            "w",
        )
        for key, values in wifi_dict.items():
            file.write(key.replace("\"", "") + ": " + values + "\r\n")
        file.close()
        print(
            "[+] All your previous logged-in Wifi SSIDs and passwords are saved on your Desktop!"
        )
    except:
        print(
            "[-] Sorry, something went wrong with this windows system version"
        )

else:
    print("[-] Sorry, this tool works only on Windows systems")
