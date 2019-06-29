Copy rrb3 archive from
https://pypi.org/project/rrb3/#files
Files will be in /home/pi/Downloads

cd /home/pi/Dowbloads
ls (you wiil see)
rrb3-1.1.tar.gz

gunzip -d rrb3-1.1.tar.gz
ls (you will see)
rrb3-1.1.tar

tar -xvf rrb3-1.1.tar (you should see)
rrb3-1.1/
rrb3-1.1/rrb3.py
rrb3-1.1/setup.py
rrb3-1.1/setup.cfg
rrb3-1.1/README.rst
rrb3-1.1/MANIFEST.in
rrb3-1.1/examples/
rrb3-1.1/examples/test_stepper.py
rrb3-1.1/examples/rover_web.py
rrb3-1.1/examples/test_motors.py
rrb3-1.1/examples/rover_avoiding.py
rrb3-1.1/examples/test_all.py
rrb3-1.1/examples/test_ranger.py
rrb3-1.1/PKG-INFO
rrb3-1.1/INSTALL.txt
rrb3-1.1/LICENSE.txt
rrb3-1.1/rrb3.egg-info/
rrb3-1.1/rrb3.egg-info/not-zip-safe
rrb3-1.1/rrb3.egg-info/top_level.txt
rrb3-1.1/rrb3.egg-info/dependency_links.txt
rrb3-1.1/rrb3.egg-info/requires.txt
rrb3-1.1/rrb3.egg-info/PKG-INFO
rrb3-1.1/rrb3.egg-info/SOURCES.txt

Make sure /usr/bin/python is linked to /usr/bin/python3.5
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.5 /usr/bin/python


Then follow the instructions
    
cd rrb3-1.1
pi@Raspi-3:~/Downloads/rrb3-1.1 $ ls
examples     LICENSE.txt  PKG-INFO    rrb3.egg-info  setup.cfg
INSTALL.txt  MANIFEST.in  README.rst  rrb3.py        setup.py

sudo python setup.py install

sudo: unable to resolve host Raspi-3
running install
running bdist_egg
running egg_info
writing rrb3.egg-info/PKG-INFO
writing requirements to rrb3.egg-info/requires.txt
writing top-level names to rrb3.egg-info/top_level.txt
writing dependency_links to rrb3.egg-info/dependency_links.txt
reading manifest file 'rrb3.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching '*.md'
writing manifest file 'rrb3.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-armv7l/egg
running install_lib
running build_py
creating build
creating build/lib
copying rrb3.py -> build/lib
creating build/bdist.linux-armv7l
creating build/bdist.linux-armv7l/egg
copying build/lib/rrb3.py -> build/bdist.linux-armv7l/egg
byte-compiling build/bdist.linux-armv7l/egg/rrb3.py to rrb3.cpython-35.pyc
creating build/bdist.linux-armv7l/egg/EGG-INFO
copying rrb3.egg-info/PKG-INFO -> build/bdist.linux-armv7l/egg/EGG-INFO
copying rrb3.egg-info/SOURCES.txt -> build/bdist.linux-armv7l/egg/EGG-INFO
copying rrb3.egg-info/dependency_links.txt -> build/bdist.linux-armv7l/egg/EGG-INFO
copying rrb3.egg-info/not-zip-safe -> build/bdist.linux-armv7l/egg/EGG-INFO
copying rrb3.egg-info/requires.txt -> build/bdist.linux-armv7l/egg/EGG-INFO
copying rrb3.egg-info/top_level.txt -> build/bdist.linux-armv7l/egg/EGG-INFO
creating dist
creating 'dist/rrb3-1.1-py3.5.egg' and adding 'build/bdist.linux-armv7l/egg' to it
removing 'build/bdist.linux-armv7l/egg' (and everything under it)
Processing rrb3-1.1-py3.5.egg
creating /usr/local/lib/python3.5/dist-packages/rrb3-1.1-py3.5.egg
Extracting rrb3-1.1-py3.5.egg to /usr/local/lib/python3.5/dist-packages
Adding rrb3 1.1 to easy-install.pth file

Installed /usr/local/lib/python3.5/dist-packages/rrb3-1.1-py3.5.egg
Processing dependencies for rrb3==1.1
Searching for RPi.GPIO==0.6.3
Best match: RPi.GPIO 0.6.3
Adding RPi.GPIO 0.6.3 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Finished processing dependencies for rrb3==1.1

rrb3 is INSTALLED

