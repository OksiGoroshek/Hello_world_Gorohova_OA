#!/bin/bash

for filter in {1..20}; do
	if [ $((filter % 2)) -eq 0 ]; then
		continue
	elif [ $filter -eq 15 ]; then
		break
	fi
	echo "$filter"
done

