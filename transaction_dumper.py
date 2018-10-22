import sys
sys.path.append("libs")
from argparse import ArgumentParser
import bson
import bbclib
import json
import datetime
import time


def _parser():
    usage = 'python {} [-f filename] [-s YYYYMMDDHHmm] [-e YYYYMMDDHHmm] [-v] [--help]'.format(__file__)
    argparser = ArgumentParser(usage=usage)
    argparser.add_argument('-f', '--file', type=str, help='input filename')
    argparser.add_argument('-v', '--verbose', action='store_true', help='verbose')
    argparser.add_argument('-s', '--start', type=str, default=None, help='start date to search')
    argparser.add_argument('-e', '--end', type=str, default=None, help='end date to search')
    args = argparser.parse_args()
    return args


if __name__ == '__main__':
    args = _parser()
    if args.file is None:
        print("-f option is mandatory!")
        sys.exit()
    with open(args.file, "rb") as f:
        dat = f.read()
    objects = bson.loads(dat)

    start_from = None
    end_by = None
    if args.start is not None:
        start_from = datetime.datetime.strptime(args.start, '%Y%m%d%H%M')
        start_from = int(time.mktime(start_from.timetuple())) * 1000
    if args.end is not None:
        end_by = datetime.datetime.strptime(args.end, '%Y%m%d%H%M')
        end_by = int(time.mktime(end_by.timetuple())) * 1000

    num_transactions = 0
    invalid_transactions = 0
    for timestamp in sorted(objects.keys()):
        transaction_id_str, txdat = objects[timestamp]
        txobj = bbclib.BBcTransaction(deserialize=txdat)
        if start_from is not None and txobj.timestamp < start_from:
            continue
        if end_by is not None and txobj.timestamp > end_by:
            continue

        num_transactions += 1
        if args.verbose:
            print("===========")
            print(txobj)
            print("---summary---")
            print("TransactionID:", txobj.transaction_id.hex())
            print("Previous Transaction ID:", txobj.relations[0].pointers[0].transaction_id.hex())
        body_dat = txobj.relations[0].asset.asset_body.decode()
        print(json.loads(body_dat))

        verify_result = True
        if txobj.signatures[0].verify(txobj.transaction_id) == 0:
            verify_result = False
            invalid_transactions += 1
        print("Verify:", verify_result)

    print("num_transactions:", num_transactions)
    print("invalid_transactions:", invalid_transactions)
