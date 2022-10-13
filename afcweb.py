#!/usr/bin/python3.5
#Ciee Mau Recode ya
# Recode aja cil gk ngapa
import requests
from subprocess import call

def main():
    call("clear")
    print("\033[1;31mWarning: ", "\033[0mURL target Anda harus seperti http://example.com/search?q=")
    url = input("Target Url: ")
    print("\n  Mulai Scanning Harap Tunggu!...")

    vulnerable = []
    f = open("XssPayloads.txt", "r")
    for payload in f.read().splitlines():
        link = url + payload
        r = requests.get(link)
        if payload.lower() in r.text.lower():
            print("\033[1;31m [-] Situs ini rentan terhadap:\033[0m" + payload)

            if payload not in vulnerable:
                vulnerable.append(payload)
            else:
                pass
        else:
            pass
    f.close()

    print("[-] mengerim payloads:")
    print("\n".join(vulnerable))


if __name__ == "__main__":
    main()
