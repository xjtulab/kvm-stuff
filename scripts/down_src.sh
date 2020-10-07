#!/usr/bin/bash
mkdir source
cd source
wget http://ftp.sjtu.edu.cn/sites/ftp.kernel.org/pub/linux/kernel/v4.x/linux-4.18.16.tar.gz
echo "Download kernel done!"
wget https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/4.18/patch-4.18.16-rt9.patch.gz
echo "Download rt-patch done!"
cd ..

#tar source and patch
sudo mkdir /usr/src/rt-preempt-linux
sudo tar -xzvf linux-4.18.16.tar.gz -C /usr/src/rt-preemt-linux
sudo gzip patch-4.18.16-rt9.patch.gz
sudo cp patch-4.18.16-rt9.patch /usr/src/rt-preemt-linux/linux-4.18.16/
cd /usr/src/rt-preemt-linux/linux-4.18.16/
sudo patch -p1 < patch-4.18.16-rt9.patch

#config 
sudo make mrproper
sudo cp /boot/config-4.18.0-193.el8.x86_64 .config
