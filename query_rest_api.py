"""
    Commandline script for simple REST API query.
"""
import os
import json
from argparse import ArgumentParser

import requests


def main():
    parser = ArgumentParser(description="Takes one keyword argument of mac address.")
    parser.add_argument("--api-key", '-ak', type=str, action="store", default="", metavar="API_KEY",
                        help="Define your valid API key.")
    parser.add_argument("--mac", '-m', type=str, action="store", default="", metavar="MAC",
                        help="Define mac address for query action.")
    args = parser.parse_args()
    mac_address = args.mac
    api_key = args.api_key

    if api_key == "":
        print("No definition of API key was provided. Exiting...")
        exit(1)
    elif mac_address == "":
        print("No definition of mac address was provided. Exiting...")
        exit(1)

    print(f"You provided this mac address to make a query: {mac_address}")

    api_key = os.getenv('MACADDRESS_API_KEY')
    r = requests.get(f"https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac_address}")

    if r.status_code != 200:
        try:
            r.raise_for_status()
        except Exception as e:
            print(e)
        print(f"Something went wrong. Status code is {r.status_code}. \nExiting...")
        exit(1)

    response_dict = json.loads(r.text)
    company_name = response_dict['vendorDetails']['companyName']
    print(f"Company name for provided mac address is: {company_name}")


if __name__ == "__main__":
    main()
