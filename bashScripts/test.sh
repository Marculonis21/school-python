#!/bin/bash

read -p "Enter Number 1: " n1
read -p "Enter Number 2: " n2

n=$((n1+n2))
echo $((n+n1))
echo $n
if [ $n == "6" ]
then
    echo "True"
else
    echo "False"
fi
