#!/bin/bash

DONE_CA_ADD=done_ca_add

if [ -f /tmp/kobo_toolbox_secrets/rootCA.crt ] && [ ! -f $DONE_CA_ADD ]; then
  cat /tmp/kobo_toolbox_secrets/rootCA.crt >> /usr/local/lib/python2.7/dist-packages/requests/cacert.pem
  touch $DONE_CA_ADD
fi
