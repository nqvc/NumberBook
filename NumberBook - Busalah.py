import requests





print("""　
     [ Made By Busalah. ]
     [ + ] Instagram : nqvc
     [ ! ] You are not entitled to sell the Tool [ ! ]
     
     [ Note ] don't type 0 in the beginning
""")




def database_1(number, code):
    if code == "966":
        code = "SA"
    elif code == "971":
        code = "UAE"
    elif code == "964":
        code = "iq"
    elif code == "20":
        code = "eg"
    else:
        print(f"[-] database 1 not support : {code}")

    url = f"http://146.148.112.105/caller/index.php/UserManagement/search_number?number={number}&country_code={code}"
    r = requests.get(url)
    if "No recourd found." in r.text:
        print("[-] not found in database")
    else:
        try:
            print(f"[+] Found Name: {str(r.json()['result'][0]['name'])}")
        except:
            pass


def database_2(number, code):
    url = 'http://86.48.0.204:919//main'

    header = {
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "%D9%86%D9%85%D8%A8%D8%B1%D8%A8%D9%88%D9%83%20%D8%A7%D9%84%D8%AE%D9%84%D9%8A%D8%AC%201/3.3 CFNetwork/1240.0.4 Darwin/20.5.0",
        "Accept-Encoding": "gzip, deflate",
        "Host": "86.48.0.204:919",
        "Accept": "*/*",
        "Accept-Language": "ar",
        "Authorization": "Basic aW9zYWRtaW46cGFzc3BvcmQ=",
        "token": "pcfgv64567ko1",
        "Content-Length": "19",
    }

    data = {
        "number": f"{code}" + number,
    }

    r = requests.post(url, data=data, headers=header)
    try:
        for name in r.json():
            print(f"[+] Found Name: {name['name']}")
    except:
        pass

number = input("[?] Number: ")
if "+" in number:
    input("[X] Error : please dont add Country code here")
    exit()

Country = input("[?] Country Code (+966 - +971 - +964 - +20 ): ")
if "+" in Country:
    Country = Country.replace("+", "")

database_1(number, Country)
database_2(number, Country)