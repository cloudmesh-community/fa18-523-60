#!/bin/bash
#---- This script uninstalls the mongodb  ---#

echo "remove the mongo clients and packages"

sudo apt-get purge mongodb mongodb-clients mongodb-server mongodb-dev

echo "ensure all packages are removed , this will remove the /etc/mongo.conf file as well"

sudo apt-get autoremove --purge mongodb

echo "after deinstalling remove the physical files"

sudo rm -r /var/log/mongodb
sudo rm -r /var/lib/mongodb
