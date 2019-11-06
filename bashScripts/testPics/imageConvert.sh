#!/bin/bash
mkdir final

for s in $(ls); do
    if [ -f "./$s" ]
    then
        echo " "
        echo "./$s"
        end=$(echo $s | awk -F'.' '{ print $2 }')
        if [ "$end" == "JPG" ]
        then
            jmeno=$(echo $s | awk -F'.' '{ print $1 }')
            echo "converting - $s -> ./final/$jmeno.PNG"
            convert -resize 30% -colorspace Gray $s ./final/$jmeno.PNG
            echo "converted"
        else
            echo "file not an image"
        fi
    fi

    #convert -resize 50% -colorspace Gray s1 s2.s3
done
