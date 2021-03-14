#!/usr/bin/bash
# Setting up the pimoroni explorer pro hat

# Update
sudo apt-get update

# Get the explorer stuff going
curl https://get.pimoroni.com/i2c | bash

# Install python pre-reqs
sudo apt-get install python-smbus
sudo apt-get install python-pip

# Install explorerhat
sudo pip install explorerhat

# Install software-properties-common
sudo apt-get install software-properties-common

# Install mosquitto
sudo apt-get install mosquitto

# Install mosquitto-clients
sudo apt-get install mosquitto-clients

# Check the status of the server
sudo service mosquitto status

# Update and exit
sudo apt-get update



