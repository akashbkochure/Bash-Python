#!/bin/bash

for i in {1..5}
do
    echo $i
done

#############

#!/bin/bash

i=1
while [ $i -le 5 ]
do
    echo $i
    ((i++))
done
