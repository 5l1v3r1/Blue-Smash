#!/bin/bash

echo "Instaling Pybluez"
wget http://org.csail.mit.edu/pybluez/release/pybluez-src-0.14.tar.gz
tar zxvf pybluez-src-0.14.tar.gz
cd pybluez-0.14
python setup.py build 
python setup.py install
cd ..
echo "Pybluez installed, cleaning up..."
rm -r pybluez-0.14
rm pybluez-src-0.14.tar.gz
echo "Done."
echo "Installing Tools"
cd tools
bash install_tools.sh
cd ..
echo "Installation Complete. You may now run Blue|Smash... Enjoy"
