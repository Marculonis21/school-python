#!/bin/bash
all= echo $(ps -aux | grep $1) | awk -F'' '{ print $2 }'
for s in $all ; do
    echo $s
done
