"""
    Commandline script for simple REST API query.

"""
import requests
import json
from argparse import ArgumentParser

parser = ArgumentParser(description="Takes one keyword argument of mac address.")
parser.add_argument("-mac", type=str, action="store", default="", metavar="MAC",
                    help="Define mac address for query action.")
args = parser.parse_args()
mac_address = args.mac
print(f"You provided this mac address to make a query: {mac_address}")

r = requests.get(r"https://api.macaddress.io/v1?apiKey=at_Y73ZuLrBFF6Ojg0j0y6dpoud1A6g9&output=json&search="
                 + str(args.mac))

request_content = r.content
response_dict = json.loads(r.text)
company_name = response_dict['vendorDetails']['companyName']
print(f"Company name for provided mac address is: {company_name}")