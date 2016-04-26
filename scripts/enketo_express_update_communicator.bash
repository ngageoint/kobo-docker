#!/usr/bin/env bash
set -e

sed -i 's/sendImmediately = false/sendImmediately = true/' ${ENKETO_SRC_DIR}/app/lib/communicator/communicator.js

