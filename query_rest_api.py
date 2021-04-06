"""
    Commandline script for simple REST API query.

"""
import requests
import json
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Takes one keyword argument of mac address.")
    parser.add_argument("-mac", type=str, action="store", default="", metavar="MAC",
                        help="Define mac address for query action.")
    args = parser.parse_args()
    mac_address = args.mac
    if mac_address == "":
        print("No definition of mac address was provided. Exiting...")
        return 1

    print(f"You provided this mac address to make a query: {mac_address}")

    r = requests.get(r"https://api.macaddress.io/v1?apiKey=at_Y73ZuLrBFF6Ojg0j0y6dpoud1A6g9&output=json&search="
                     + str(args.mac))

    response_dict = json.loads(r.text)
    company_name = response_dict['vendorDetails']['companyName']
    print(f"Company name for provided mac address is: {company_name}")


if __name__ == "__main__":
    main()
