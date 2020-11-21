import requests
from datetime import datetime
import time
import argparse
import getpass
import json
from pprint import pprint
import logging
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


def api_login():
    data = {"username": "admin", "password": "eve", "html5": 0}
    url = 'https://10.10.21.28/api/auth/login'
    login = requests.post(url=url, data=json.dumps(data), verify=False)
    if login.status_code == 200:
        cookies = login.cookies
        print("\nLogin Successful.\n")
    else:
        print(login.status_code, "Login Failure.",)
        exit(0)
    return cookies


def query_api(url, time_stamp, cookie):
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://10.10.21.28/legacy/',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-type': 'application/json'
    }
    api_url = 'https://10.10.21.28/api/'
    full_url = api_url + url
    logging.info(f"URL:{full_url}")
    nodes = requests.get(url=full_url, headers=headers,
                         cookies=cookie, verify=False)
    response = nodes.json()
    return response


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topology', type=str,
                        dest="topo", help='Provide topology name.')
    parser.add_argument('-n', '--nodes', dest="nodes",
                        action='store_true', help='List nodes.')
    parser.add_argument('-u', '--up', dest="start",
                        action='store_true', help='Provide lab name to start')
    parser.add_argument('-d', '--down', dest="stop",
                        action='store_true', help='Provide lab name to stop')
    parser.add_argument('-a', '--all', dest="all_labs",
                        action='store_true', help='List all labs.')
    parser.add_argument('-w', '--wipe', dest="wipe",
                        action='store_true', help='Wipe all nodes.')
    args = parser.parse_args()
    now = datetime.now()
    time_stamp = int(datetime.timestamp(now) * 1000)
    print()
    cookie = api_login()
    if args.topo and args.start:
        logging.info("Running EVE-NG nodes start")
        url = 'labs/{}/nodes'.format(args.topo)
        data = query_api(url, time_stamp, cookie)
        #print(json.dumps(data, indent=2))
        data = data["data"]
        for key, value in data.items():
            print(f"Starting node {key}")
            url = 'labs/{}/nodes/{}/start'.format(args.topo, key)
            response = query_api(url, time_stamp, cookie)
            print(response)
            print()
    elif args.topo and args.stop:
        url = 'labs/{}/nodes'.format(args.topo)
        data = query_api(url, time_stamp, cookie)
        print(json.dumps(data, indent=2))
        data = data["data"]
        for key, value in data.items():
            url = 'labs/{}/nodes/{}/stop'.format(args.topo, key)
            response = query_api(url, time_stamp, cookie)
            print(response)
            print()
    elif args.topo and args.nodes:
        url = 'labs/{}/nodes'.format(args.topo)
        data = query_api(url, time_stamp, cookie)
        data = data["data"]
        for device in data.items():
            pprint(device)
        print()
    elif args.all_labs:
        url = 'folders/'
        data = query_api(url, time_stamp, cookie)
        data = data["data"]
        for i in data.items():
            pprint(i)
        print()
    elif args.topo and args.wipe:
        url = 'labs/{}/nodes'.format(args.topo)
        data = query_api(url, time_stamp, cookie)
        print(json.dumps(data, indent=2))
        data = data["data"]
        for key, value in data.items():
            url = 'labs/{}/nodes/{}/wipe'.format(args.topo, key)
            response = query_api(url, time_stamp, cookie)
            print(response)
            print()
    elif args.topo:
        url = 'labs/{}/nodes'.format(args.topo)
        data = query_api(url, time_stamp, cookie)
        print(json.dumps(data, indent=2))
        data = data["data"]
        for key, value in data.items():
            name = value["name"]
            device_type = value["type"]
            image = value["image"]
            # print(value["url"])
            url = value["url"].split(":")
            # print(url)
            ip = url[1].replace("//", "")
            # print(ip)
            port = (url[2])
            print('{} {} {} {} {} {}'.format(
                key, name, device_type, image, ip, port))
        print()
    else:
        print("No options given. Use -h for help.")


if __name__ == "__main__":
    main()
