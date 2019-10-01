#!/bin/bash

#kopíruje soubory z adr1 do adr2
# použití: copy_file.sh adr1 adr2

mkdir $2

for s in $(ls $1); do
	echo "Kopíruji soubor: $s"
	cp $1/$s $2
done

echo "Konec copy"
