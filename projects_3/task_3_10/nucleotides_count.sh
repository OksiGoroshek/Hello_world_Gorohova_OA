#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
for file in *.fasta; do
if [ ! -s "$file" ]; then continue; fi
seq=$(grep -v "^>" "$file" | tr -d '\n')
A=$(echo "$seq" | grep -o "A" | wc -l)
T=$(echo "$seq" | grep -o "T" | wc -l)
C=$(echo "$seq" | grep -o "C" | wc -l)
G=$(echo "$seq" | grep -o "G" | wc -l)
printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$A" "$T" "$G" "$C"
done
