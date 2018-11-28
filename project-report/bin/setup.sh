#!/bin/bash
set -e

# The script installs MongoDB on ubuntu 18.04 and download and imports the dataset to MongoDB.
# The script must run as root user or user that has sudo privilege to install 
# Script assumes the dataset is in same directory of  the script,if not change the dir path
# Ensure mongo_install.sh has execute (chmod + mongo_install.sh)

export LOGFILE1="master.log"
export LOGFILE2="status.log"
export LOGFILE3="kaggle.log"

echo "download the dataset from kaggle.com"
kaggle datasets download kemical/kickstarter-projects -f ks-projects-201801.csv >> $LOGFILE3

echo "Script Installs Latest Mongodb DB on ubuntu 18.04 Bionic"

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

echo "Find & Update the latest packages"
sudo apt-get update > $LOGFILE1

echo "Install MongoDB package"
sudo apt install -y mongodb >> $LOGFILE1

echo "Check the Service and Database"


#sudo systemctl enable mongod

#sudo service mongod restart

sudo systemctl status mongodb > $LOGFILE2

# mongo --eval 'db.runCommand({ connectionStatus: 1 })' >> $LOGFILE2

#sudo systemctl restart mongodb  >> $LOGFILE2

echo "Import the database "

mongoimport -d kickstarter -c projects --type csv --file kickproject.csv --headerline >> $LOGFILE2

echo "Import Completed"

