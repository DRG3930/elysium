import random
from ast import Str
from tokenize import String

import requests
from pyexpat.errors import messages

def print_hi(name, false=None, String r):
    url = "http://www.sendanonymoussms.com/send.php"


    msg = random.Random["Good morning",
    "are you almost ready",
    "Cant wait to show you"
    ][0]

def loop_Table_Of_Hanoy():
    for x in y
    rcvr = ["479-689-6732",  # chris
            "417-350-7234",  # becca
            "651-560-8492",  # unknown 1
            "406-298-1719"]  # unkown 2

   headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "_ga=GA1.2.854810418.1738160529; _gid=GA1.2.895072633.1738160529",
        "Origin": "http://www.sendanonymoussms.com",
        "Pragma": "no-cache",
        "Referer": "http://www.sendanonymoussms.com/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0"
    }
    payload = {
        "name": "Anonymous",
        "country": "+1",
        "ReceiverNumber": Str(rcvr),
        "message": msg,
        "remLen1": "145",
        "security_code": "unbadhar",
        "post": "1",
        "Submit": "SEND SMS!"
    }

    response = requests.post(url,
                             headers=headers,
                             data=payload,
                             verify=false)
 


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
