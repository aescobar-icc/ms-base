#!/bin/ash
source /app-run/sh/base.sh

log "INSTALLING ssh conf"
source /app-run/sh/install_ssh.sh

log "checking libs..."
mkdir -p /app-run/libs
cd /app-run/libs

cp /app-run/requirements.git requirements.git
source requirements.git

for lib_dir in $(ls -ltr);do
	if [[ -d $lib_dir ]] ;then
		cd $lib_dir
		log "TESTING : $lib_dir"
		python setup.py test
		log "INSTALLING : $lib_dir"
		pip install .
		cd ..
		rm -rf $lib_dir
	#else
	#	errorlog "IGNORING $lib_dir !!"
	fi
done