#/bin/bash

dd if=/dev/urandom of=/dev/stdout bs=1M count=$1 | base64 -w 0 > random-gorp
