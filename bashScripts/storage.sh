#/bin/bash

for adr in $(ls $1); do
    echo "$(du -sh $1/$adr)"
done
