#!/bin/bash

read -p "Введите вес(в килограммах): " WEIGHT
read -p "Введите рост(в сантиметрах): " HEIGHT

BMI=$((WEIGHT*10000 / (HEIGHT * HEIGHT)))

echo "Индекс массы тела: ${BMI%.*}"
