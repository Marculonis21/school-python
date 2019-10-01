#!/bin/bash

for soubor in $(ls ./$1); do
    echo -n "mažu soubor: $soubor --- opravdu smazat? "
    read odp
    if [ $odp = a ]
    then
        rm ./$1/$soubor
        echo "...smazáno"
    else
        echo "...nesmazáno"
    fi
done
