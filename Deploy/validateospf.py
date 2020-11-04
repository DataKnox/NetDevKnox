import requests
import json
import pytest
import logging
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
logging.basicConfig(level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

ip_address = ['10.10.21.15', '10.10.21.155']
base_url = "http://{}/restconf/data"
find_routerid_url = 'Cisco-IOS-XE-ospf-oper:ospf-oper-data/ospf-state/ospf-instance'
headers = {'Accept': 'application/yang-data+json',
           'Content-Type': 'application/yang-data+json'}


def test_ospf():
    for ip in ip_address:
        print(f"Starting with device {ip}")
        logging.info(f"Starting with device {ip}")
        url = f"https://{ip}/restconf/data/Cisco-IOS-XE-ospf-oper:ospf-oper-data/ospf-state/ospf-instance"

        routerid_resp = requests.get(
            url=url, auth=('cisco', 'cisco'), headers=headers, verify=False)
        logging.info(routerid_resp.status_code)
        logging.info(routerid_resp.text)
        router_id = json.loads(routerid_resp.text)[
            "Cisco-IOS-XE-ospf-oper:ospf-instance"][0]['router-id']
        print(f"Retrieved router-id {router_id} for host {ip}")
        new_url = (
            f"{url}=address-family-ipv4,{router_id}/ospf-area=0/ospf-interface/")
        interfaces = requests.get(
            url=new_url, headers=headers, auth=('cisco', 'cisco'), verify=False).json()['Cisco-IOS-XE-ospf-oper:ospf-interface']
        ospf_state = False
        for interface in interfaces:
            if 'ospf-neighbor' in interface:
                nbrs = interface['ospf-neighbor']
                for nbr in nbrs:
                    if nbr['state'] == 'ospf-nbr-full':
                        ospf_state = True
                        print(f"OSPF is up on {ip}")
        # print(new_url)
        assert(ospf_state == True)


test_ospf()
