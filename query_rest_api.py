"""
    Title:  Commandline script for simple REST API query.

    Input: two keyword arguments: mac address and API key.
    Output: Company name of vendor with provided mac address

    Releases:
    Date        Version         Author
    April 2021  1.0.0           Mateusz Miernik

"""

import os
import json
import requests
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Takes keyword arguments for mac address and API key.")
    parser.add_argument("--api-key", '-ak', type=str, action="store", default="", metavar="API_KEY",
                        help="Define your valid API key.")
    parser.add_argument("--mac", '-m', type=str, action="store", default="", metavar="MAC",
                        help="Define mac address for query action.")
    args = parser.parse_args()
    mac_address = args.mac
    api_key = args.api_key

    # Check if all required arguments were provided
    if api_key == "":   # Firstly check if commandline argument with API key was provided
        api_key = os.getenv('API_KEY')
        if api_key is None:     # Secondly check if local environment variable for API key is available
            print("No definition of API key was provided. Exiting...")
            exit(1)
    elif mac_address == "":     # Check if commandline argument with mac address was provided
        print("No definition of mac address was provided. Exiting...")
        exit(1)

    print(f"You provided this mac address to make a query: {mac_address}")

    r = requests.get(f"https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac_address}")

    # Check if query returned status code = 200, if not show current status code
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
