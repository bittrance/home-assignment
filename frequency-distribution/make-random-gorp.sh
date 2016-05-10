#/bin/bash

mbytes=${1:-10}
here=$(dirname ${0})

dd if=/dev/urandom of=/dev/stdout bs=1M count=${mbytes} | base64 -w 0 > ${here}/random-gorp
