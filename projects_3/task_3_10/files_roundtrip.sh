#!/bin/bash

for i in {1..10};do
	touch test$i.txt
done

echo "В текущей папке добавлены 10 файлов"

j=10

while [ "$j" -ge 1 ]; do
	file="test$i.txt"

	if [ -f "$file" ]; then
		rm -v "$file"
	fi
	((j--))
done

echo "В текущей папке удалены 10 файлов"
