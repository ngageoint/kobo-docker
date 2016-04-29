#!/bin/bash
set -e

GEOSERVER_USER=${GEOSERVER_USER:-"admin"}
GEOSERVER_PASSWORD=${GEOSERVER_PASSWORD:-"geoserver"}

GEOSERVER_DATA_DIR=/srv/geoserver
if [ -f $GEOSERVER_DATA_DIR/security/masterpw.info ]
then
  /bin/rm $GEOSERVER_DATA_DIR/security/masterpw.info
  sed -i 's/admin/'$GEOSERVER_USER'/' $GEOSERVER_DATA_DIR/security/usergroup/default/users.xml
  sed -i 's/password=".*"/password="plain:'$GEOSERVER_PASSWORD'"/' $GEOSERVER_DATA_DIR/security/usergroup/default/users.xml
  sed -i 's/admin/'$GEOSERVER_USER'/' $GEOSERVER_DATA_DIR/security/role/default/roles.xml
fi

