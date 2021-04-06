# Description

A script that can query a rest API, parse, and return the output.
Script takes one parameter from commandline - mac address.
It is using https://macaddress.io/ website.

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
python query_rest_api.py -mac example_mac_address
```

Script takes only one keyword argument "-mac"