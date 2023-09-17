#!/bin/bash

my_array=("apple" "banana" "cherry")

echo ${my_array[0]}  

###########

#!/bin/bash

my_array=("apple" "banana" "cherry")

read num

echo ${my_array[$num]}  



#############


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
