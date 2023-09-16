#!/bin/bash

for ((i = 1; i <= 50; i++)); do
  square_root=$(echo "scale=0; sqrt($i)" | bc)
  if [ "$((square_root * square_root))" -eq "$i" ]; then
    echo "$i"
  fi
done
