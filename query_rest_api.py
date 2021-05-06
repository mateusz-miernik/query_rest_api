"""
    Title:  Commandline script for simple REST API query.

    Input: two keyword arguments: mac address and API key.
    Output: Company name of vendor with provided mac address

    Releases:
    Date            Version         Author              Comment
    April 2021      1.0.0           Mateusz Miernik     Initial release
    May   2021      1.1.0           Mateusz Miernik     Code refactoring

"""

import os
import json
import requests
from argparse import ArgumentParser, Namespace


def _parse_args() -> Namespace:
    parser = ArgumentParser(description="Script make a simple query to REST API.")
    parser.add_argument("mac", help="Define mac address for query action.")
    parser.add_argument("--api_key", '-a', help="Define your valid API key.")
    args = parser.parse_args()
    return args


def _process_request(api_key: str, mac_address: str) -> None:
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


def main() -> None:
    args = _parse_args()
    mac_address = args.mac
    api_key = args.api_key

    if api_key is None:   # Firstly check if commandline argument with API key was provided
        api_key = os.getenv('API_KEY')
        if api_key is None:     # Secondly check if local environment variable for API key is available
            print("No definition of API key was provided. Exiting...")
            exit(1)

    _process_request(api_key, mac_address)


if __name__ == "__main__":
    main()
