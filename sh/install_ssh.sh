#!/bin/ash
mkdir -p ~/.ssh/
cp /app-run/.ssh/* ~/.ssh/
chmod 400 ~/.ssh/pkey
#ls ~/.ssh/
eval "$(ssh-agent -s)"
ssh-add -k ~/.ssh/pkey
