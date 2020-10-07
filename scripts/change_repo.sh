#!/usr/bin/bash
sudo cp /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bk
echo "Get Alibaba repo mirror:"
sudo wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-8.repo
echo "Clear cache..."
sudo yum makecache
echo "Change Source repo done!"