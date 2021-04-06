# Description

A script that can query a rest API, parse, and return the output.
Script can take two parameters from commandline - API key and MAC address.
It makes query request to https://macaddress.io/ website.

# Requirements

* `python 3.8.6`

# Before you start

Make sure to read this entire documentation first before trying to execute any commands listed below to get an
understanding of how this utility works, instead of blindly copying and pasting commands into the terminal.

If things like `virtualenv` or `pip` are not clear for you, make sure to read about them or ask your coworkers. Its your
responsibility to troubleshoot any problems directly related to basic stuff (like abovementioned `virtualenv` or `pip`).

# Installation

Using `virtualenv` install all required packages with:

```commandline
pip install -r requirements.txt
```

# Running

Example run scenario looks like this:

```commandline
python query_rest_api.py -api-key example_api_key -mac example_mac_address
```

Script takes two keyword argument:
* `-mac` for MAC address of some vendors
* `-api-key` for valid API key

Please be advised that API key can be also provided from environmental variable.
You can type in bash (linux):
```commandline
export MACADDRESS_API_KEY=qwertyuiop
```
and then run a command without providing `-api-key` keyword argument as below:
```commandline
python query_rest_api.py -mac example_mac_address
```

OR

Run one comandline execution of script with providing API key from environmental variable (environmental variable will be available only once):
```commandline
MACADDRESS_API_KEY=qwertyuiop python query_rest_api.py -mac example_mac_address
```