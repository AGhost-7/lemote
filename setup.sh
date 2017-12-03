#!/usr/bin/env bash

git submodule update --init
sudo apt-get install build-essential -y
sudo apt-get install flex -y
sudo apt-get install python3-pip -y
sudo apt-get install libcwiid-dev -y
sudo apt-get install python3-dev -y
sudo apt-get install automake -y

pushd cwiid
aclocal
autoconf
./configure
make
sudo make install
popd
