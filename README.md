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

Please prepare transaction archive that contains multple transaction data (see appendix). Here we assume the file name is "sample.dat."

If you specify no options, you will see as follows:

```
# python transaction_dumper.py -f sample.dat

... snip ...

**asset_body_json data**
Verify: True
**asset_body_json data**
Verify: True
num_transactions: 554
invalid_transactions: 0
```

Only asset body info of each transaction of the first BBcRelation object are shown. If invalid transactions, meaning that the signature verification fails, exist, the number of 'invalid_transactions' will be more than 1.



If you specify -v option, you will see as follows:

```
# python transaction_dumper.py -f sample.dat -v

... snip ...

------- Dump of the transaction data ------
* transaction_id: b'91afe9516fdb906d2648da279a57390b672562591abddd3742686ecd71a5d8fa'
version: 1
timestamp: 1538792793716
id_length: 32
Event[]: 0
Reference[]: 0
Relation[]: 1
 [0]
  asset_group_id: b'39e41b0ee4a327e8a84d6b5e08d066a6a5640374bc0f475504fcb6e738277301'
  Pointers[]: 1
   [0]
     transaction_id: b'c623238439f84f17cf2a0e12b06ef27f803fb6f77e79c2f00fb7b1a112b8287f'
     asset_id: None
  Asset:
     asset_id: b'43f77ef97b1508addd1633cbfe2759487abaa0abcedd827c3dcbdf6931854ff1'
     user_id: b'96b05497c0e0c6c4023caba107b99a51564a9b37772dfb6e7a5cf31723ba8a7f'
     nonce: b'75c2371be563f3990a375994336b036a58258dc2738cf94ef7a660ac5983d7e0'
     file_size: 0
     file_digest: None
     body_size: 453
     body: b'*** asset body info ***'
Witness:
 [0]
  user_id: b'96b05497c0e0c6c4023caba107b99a51564a9b37772dfb6e7a5cf31723ba8a7f'
  sig_index: 0
Cross_Ref: None
Signature[]: 1
 [0]
  key_type: 2
  signature: b'823f86ac7f9a8d756ede37115057dad463721483e991d27ceda88c8153dda567d215e7cbfdfb42a48ee5a1c79a06fa230544a214f61e0a93cf85c647dfd1a46d'
  pubkey: b'04602a3c9692a883375d1667804d7dcb2ed21ebc3103802ed9552293f038877b713fa2f1c9f7ce2f4cc9fda78b563a88186bf43102dfe69155da1635c6150e7d41'

---summary---
TransactionID: 91afe9516fdb906d2648da279a57390b672562591abddd3742686ecd71a5d8fa
Previous Transaction ID: c623238439f84f17cf2a0e12b06ef27f803fb6f77e79c2f00fb7b1a112b8287f
*** asset body info ***
Verify: True
num_transactions: 554
invalid_transactions: 0
```

In addition to the simple case explained above, you will see the full dump of each thansaction and the summary information. TransactionID is the identifier of the transaction and Previous Transaction ID is one that the BBcPointer object points to.

For the contents of a transaction data, please check the design documents of BBc-1 [here](https://github.com/beyond-blockchain/bbc1/blob/develop/docs/BBc1_design_document_v1.0_ja.pdf)

### Note

This tool is not so flexible dump tool in that it has a strong assumptions for a transaction as follows:

* Only the asset_body of the first BBcRelation is shown (see line 57 in transaction_dumper.py)

Please modify those lines as you want.

# Appendix: Archive data structure

This tool assumes the following data structure:

* bson-object (binary JSON)
  - Python dictionary (or Javascript object)
    - timestamp: array of [Transaction_ID hex string, BBc-1 transaction data]
    - timestamp: array of [Transaction_ID hex string, BBc-1 transaction data]
    - timestamp: array of [Transaction_ID hex string, BBc-1 transaction data]
    - ...

The timestamps are unixtime format and the unit of them is millisecond.
(If you want to get a normal unixtime, divide the value by 1000)
