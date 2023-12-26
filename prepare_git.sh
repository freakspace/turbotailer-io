#!/bin/bash

# Exit if any command fails
set -e

# Setup github
git --version
sudo apt update
sudo apt upgrade
sudo apt install git
git config --global user.name "Emil Nielsen"
git config --global user.email "hej@emilnielsen.com"
