Dump tool for archive data of BBc-1 transactions
====
This is a simple dump tool for archived BBc-1 transactions.

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
python -m venv venv
source venv/bin/activate
pip install -r requiremehts.txt
```

# Usage
Run the command in the virtualenv environment.
```bash
source venv/bin/activate
python transaction_dumper.py -f <filename>
```
For other options, -h option shows the help.

# Archive data structure

