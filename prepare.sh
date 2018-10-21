#!/bin/bash

git clone -b master https://github.com/beyond-blockchain/libbbcsig.git
cd libbbcsig
bash prepare.sh

cd lib
if [ -f libbbcsig.so ]; then
  cp libbbcsig.so ../../libs/
elif [ -f libbbcsig.dylib ]; then
  cp libbbcsig.dylib ../../libs/
fi
