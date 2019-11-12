#!/bin/bash

for item in $(du -hs $1/*/); do

    #for loop du dělí text zvláštním způsobem
    #První se vrací velikost, pak umístění. Potřeba data na chvílí ukládat. 
    if [[ $item == *"/"* ]]; then
        NAME=$(echo $item | awk '{n=split($0,x,"/"); print x[n-1] }')
        echo "Adresář: $NAME - velikost: $SIZE"
    else
        SIZE=$item
    fi
done
