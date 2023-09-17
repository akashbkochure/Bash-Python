#!/bin/bash

array=("apple" "pipe" "cherry" "strawberry")

for element in "${array[0]}"; do
    echo "$element"
done

####

#!/bin/bash

array=("apple" "pipe" "cherry" "strawberry")

read num

for element in "${array[$num]}"; do
    echo "$element"
done
