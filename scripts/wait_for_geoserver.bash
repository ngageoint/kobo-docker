#!/bin/bash
set -e

echo 'Waiting for container `geoserver`.'
dockerize -timeout=60s -wait http://localhost:8080
echo 'Container `geoserver` up.'
#
#until [ "`curl --silent --connect-timeout 1 -I http://localhost:8080 | grep \"302 Found\"`" != "" ] 
#do 
#  sleep 10
#done

