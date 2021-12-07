#!/bin/sh
# Name : irreale network installer shell-script
# Author : Harvey Wu

# This is a script that can dowload 'irreale' from internet. It runs on 
# Unix-like operating systems (Linux, Macos, etc.), if you are currently
# using Windows please download the irreale installation package.

VERSION = "0.1.0"
BASE_URL = ""
INSTALL_DIR = "~/.irreale"
CONFIG_DIR = "~/.config/irreale/"

echo "irreale network installer v ${VERSION}"

main(){
  env_check
}

# Check the environment.
env_check(){
  env = (git mkdir rmdir rm chmod python clang rustc cargo make)
  for i in ${#env[*]}
  do
    command -v "${env[i]}" > /dev/null 2>&1
  done
}
