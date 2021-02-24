wget https://api.modpacks.ch/public/modpack/35/174/server/linux
chmod +x linux./linux 35 --auto
echo 'eula=true' > eula.txt
mv forge-1.12.2-14.23.5.2846-universal.jar forge-1.12.2-14.23.5.2846.jar
add-apt-repository ppa:openjdk-r/ppa
apt-get install openjdk-8-jre