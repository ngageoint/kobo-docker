#!/bin/bash

if [ -f /tmp/kobo_toolbox_secrets/rootCA.crt ] && [ ! -f /usr/share/ca-certificates/rootCA.crt ]; then
  cat /tmp/kobo_toolbox_secrets/rootCA.crt >> /usr/local/lib/python2.7/dist-packages/requests/cacert.pem
fi

