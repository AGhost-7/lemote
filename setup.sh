#!/usr/bin/env bash

set -e

git submodule update --init
sudo apt-get install build-essential -y
sudo apt-get install flex -y
sudo apt-get install python3-pip -y
sudo apt-get install libcwiid-dev -y
sudo apt-get install python3-dev -y
sudo apt-get install automake -y
sudo apt-get install bison -y

pushd cwiid
aclocal
autoconf
./configure
make
sudo make install
popd

sudo apt-get install python3-cairo -y
