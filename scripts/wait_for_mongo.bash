#!/bin/bash
set -e

echo 'Waiting for container `mongo`.'
dockerize -timeout=60s -wait ${MONGO_PORT}
echo 'Container `mongo` up.'
