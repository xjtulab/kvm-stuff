#!/usr/bin/bash

git clone git://git.kernel.org/pub/scm/linux/kernel/git/clrkwllms/rt-tests.git
cd rt-tests
git branch testing
git checkout testing
sudo make install
cd ../

echo "[info]Install cyclictest done!"
