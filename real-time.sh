#!/bin/bash

counter=5

while [ $counter -gt 0 ]

do

echo "Countdown: $counter"

counter=$((counter - 1))

done

echo "Blast off!"
