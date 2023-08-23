#!/bin/bash

lisattavat_kansiot=(/audio /domain /logic /menu /visual)
kooste="$PWD:"

for k in "${lisattavat_kansiot[@]}";
    do kooste+="$PWD$k:"
done

export PYTHONPATH=$kooste
cd ..

python3 -m harvesting_asteroids
