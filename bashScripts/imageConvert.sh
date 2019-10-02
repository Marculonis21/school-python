#!/bin/bash
#
#$1 vstupní soubor
#$2 vystup
# konvertuj.sh $1 $2    

for s in $(ls -l *.$1) ; do
    jmeno= echo $s | awk -F'.' '{ print $1 }'

    echo "$s --> $jmeno.$2"

    convert $s $jmeno.$2
done
