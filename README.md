Dump tool for archive data of BBc-1 transactions
====
This is a simple dump tool for BBc-1 transaction archive.

# Environment

* Linux/Mac
* Python3.5 or later

## preparation

```bash
bash prepare.sh
```
Please wait for a while. It builds openssl, so it takes long time.

If you use virtualenv of python3, do as follows:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requiremehts.txt
```

# Usage
Run transaction_dumper.py after entering the virtualenv environment.
```bash
source venv/bin/activate
python transaction_dumper.py -f <filename>
```
For other options, -h option shows the help.

# Archive data structure

This tool assumes the following data structure:

* bson-object (binary JSON)
  - Python dictionary (or Javascript object)
    - timestamp: array of [Transaction_ID hex string, BBc-1 transaction data]
    - timestamp: array of [Transaction_ID hex string, BBc-1 transaction data]
    - timestamp: array of [Transaction_ID hex string, BBc-1 transaction data]
    - ...

The timestamps are unixtime format and the unit of them is millisecond.
(If you want to get a normal unixtime, divide the value by 1000)
