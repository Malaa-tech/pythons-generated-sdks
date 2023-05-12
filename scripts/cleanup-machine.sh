#!/bin/bash

# Desc : Remove all brew related dependencues, files, and directories from developer machine
# Notes :
# - This script is tested on MacOs Ventura 13.0, Apple M2 Pro Chip

Red='\033[0;31m'

echo "${Red} Removing brew packages 🗑️${NO_COLOR}"
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh
sudo rm -r /opt/homebrew
