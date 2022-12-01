#!/usr/bin/bash
# This script performs the following operations
# add all file to staging area
# make file executable
# readd update to staging area
# add commmit message
# push all local changes remotely
git add .
chmod +x $1
git add .
git commit -m "$2"
git push

