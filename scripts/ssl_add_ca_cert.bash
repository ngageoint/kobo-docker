#!/bin/bash

if [ -f /tmp/kobo_toolbox_secrets/rootCA.crt ] && [ ! -f /usr/share/ca-certificates/rootCA.crt ]; then
  cp /tmp/kobo_toolbox_secrets/rootCA.crt /usr/share/ca-certificates > /dev/null 2>&1
  echo "rootCA.crt" >> /etc/ca-certificates.conf > /dev/null 2>&1
  update-ca-certificates --fresh > /dev/null 2>&1
fi

