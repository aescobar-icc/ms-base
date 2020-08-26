#!/bin/ash
#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37

#CONSTANTS
Red='\033[0;31m'
Green='\033[0;32m'
BrownOrange='\033[0;33m'
NoColor='\033[0m' # No Color

#FUNCTIONS
function log(){
	echo -e "${Green}[ALTO.SERVICE]${BrownOrange} $1 ${NoColor}"
}
function errorlog(){
	echo -e "${Green}[ALTO.SERVICE]${Red} $1 ${NoColor}"
}
function setColorLog(){
	echo -e "$1\c"
}
function clone_branch(){
    log "CLONING: $WORKSPACE/$1 BRANCH: $2"
    git clone -b $2  git@bitbucket.org:$WORKSPACE/$1.git
    if [ $? != 0 ]
    then
        errorlog "error cloning repo, aborting... "
        exit -1
    fi
    log "checking branch.."
    cd $1
    git branch
    cd ..
}