#!/bin/bash

check_root() {
if [ "$EUID" -ne 0 ]; then
echo "Ошибка! Сюда можно только суперпользователю"
exit 1
fi
}
check_root
echo "Можете продолжать работу"
