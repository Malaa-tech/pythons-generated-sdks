#!/bin/bash

# Desc : Script to install needed packages for mac machine using binaries and Brew package manager
# Notes :
# - This script is tested on MacOs Ventura 13.0, Apple M2 Pro Chip

# ==================== Colors ====================
Green='\033[0;32m'
Red='\033[0;31m'
Pink='\033[0;35m'
NO_COLOR='\033[0m'

echo "${Pink} We are setting up your machine ⏳ ..."

# Required packages to run Malaa backend
function install_core_packages(){
    echo "${Green} Installing Brew...${NO_COLOR}"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    echo "${Green} Installing Git...${NO_COLOR}"
    brew install git

    echo "${Green} Installing Python version 3 latest...${NO_COLOR}"
    brew install python3

    echo "${Green} Installing Docker...${NO_COLOR}"
    brew install --cask docker

    echo  "${Green} Installing Docker Compose"
    brew install docker-compose

    echo "${Green} Installing poetry...${NO_COLOR}"
    brew install poetry

    echo "${Green} Installing node...${NO_COLOR}"
    brew install node

    echo "${Green} Installing yarn...${NO_COLOR}"
    brew install yarn

    echo "${Green} Installing Taskfile...${NO_COLOR}"
    brew install go-task/tap/go-task

    echo "${Green} Installing Skaffold...${NO_COLOR}"
    brew install skaffold

    echo "${Green} Installing kubectl...${NO_COLOR}"
    brew install kubectl

    echo "${Green} Installing kubeseal...${NO_COLOR}"
    brew install kubeseal

}

# To install dev tools to increase productivity and enhance the development experience
function install_dev_tools() {
    echo "${Green} Installing k9s...${NO_COLOR}"
    brew install k9s

    echo "${Green} Installing kubectx...${NO_COLOR}"
    brew install kubectx

    echo "${Green} Installing kustomize...${NO_COLOR}"
    brew install kustomize

    echo "${Green} Installing stern...${NO_COLOR}"
    brew install stern

    echo "${Green} Installing kubeval (Linting for k8s yaml manifests)...${NO_COLOR}"
    brew install kubeval

    echo "${Green} Installing tldr...${NO_COLOR}"
    brew install tldr

    echo "${Green} Installing git gh...${NO_COLOR}"
    brew install gh
}

# Enabling auto completions for cli tools
function install_auto_completions(){
    echo "${Green} Enabling auto completions for kubectl...${NO_COLOR}"
    echo 'autoload -Uz compinit' >>~/.zshrc
    echo 'compinit' >>~/.zshrc
    echo 'source <(kubectl completion zsh)' >>~/.zshrc
}

# Remove packages if any error happened
function cleanup(){
    echo "${Red} Removing brew packages 🗑️${NO_COLOR}"
    # Run local cleanup script cleanup-machine
    chmod +x ./cleanup-machine.sh
    ./cleanup-machine.sh
    exit 1
}

# Optional shortcuts to be added to your .zshrc profile(file)
function setup_shortcuts(){
    echo "${Green} Adding shortcuts to your .zshrc profile...${NO_COLOR}"
    echo 'alias k=kubectl' >>~/.zshrc
    echo 'alias kx=kubectx' >>~/.zshrc
    echo 'alias ks=kubeseal' >>~/.zshrc
    echo 'alias t=tldr' >>~/.zshrc
    echo 'alias g=git' >>~/.zshrc
    echo 'alias d=docker' >>~/.zshrc
    echo 'alias dc=docker-compose' >>~/.zshrc
}

# Listen to any error and run remove_pkgs function
trap cleanup ERR
trap cleanup SIGINT
trap cleanup SIGTERM

# Run functions
install_core_packages
install_dev_tools

# Only run auto completions if you are using Zsh and no errors happened
if [[ "$SHELL" == *"zsh"* ]] && [[ $? -eq 0 ]]; then
  install_auto_completions
else
  echo "Either there were errors or you are not using Zsh."
fi

# Optional shortcuts to be added to your .zshrc profile(file)
# setup_shortcuts
