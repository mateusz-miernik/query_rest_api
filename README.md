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

First arguments specify paths to files containing (preferably) absolute paths to original `.mudp`/`.dvl` files. Each
file can be a simple text file, a `.csv` file or an `.xlsx` file, where at least one column contains the paths. Second
argument points to a directory where reprocessed files are located (resim output directory). `LD` is a function
abbreviation, so that function's specific signals can be validated. Optional `-o` argument specifies custom path to
`.csv` file with results. **NOTE:** this alters paths for `.xlsx` and `.txt` files too. Another optional argument, `-n`,
specifies column name that contains `.mudp`/`.dvl` paths. It defaults to `Input` and is ignored when input file is a
plain text file.