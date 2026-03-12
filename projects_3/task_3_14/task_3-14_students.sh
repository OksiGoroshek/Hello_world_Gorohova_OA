#!/bin/bash

echo "Выводит только имена"
awk '{print $1}' students.txt

echo "Выводит только оценки"
awk '{print $2}' students.txt

echo "Выводит номер строки и имя"
awk '{print NR, $1}' students.txt
