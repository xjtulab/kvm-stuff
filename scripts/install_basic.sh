#!/usr/bin/bash
echo "Install git..."
sudo yum install git 
echo "Install gcc..."
sudo yum install gcc 
echo "Install numacti-dep for cyclictest"
sudo yum install numactl-devel 
echo "Install pinyin"
sudo dnf install ibus-libpinyin.x86_64 -y

#some lib for compile kernel 
sudo yum install ncurses-devel
sudo yum install elfutils-libelf-devel
sudo yum install openssl-devel
sudo yum install flex bison
