#!/bin/sh
wget https://api.modpacks.ch/public/modpack/35/174/server/linux
chmod +x linux
./linux 35 --auto
echo 'eula=true' > eula.txt
yum install java-1.8.0-openjdk
