#!/bin/bash
counter=1
while [ $counter -le 24 ]
do
    echo $counter
    ((counter++))
    python3 Game.py
done

echo All done
