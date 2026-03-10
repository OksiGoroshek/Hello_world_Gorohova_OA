#!/bin/bash

FILE_PATH="./system.log"
ERROR_CODE=1

if [ -f "$FILE_PATH" ]; then
    echo "Лог-файл найден."
else
    echo "Ошибка: файл не существует."
fi

case $ERROR_CODE in
    0)
        echo "Статус: Ошибок не найдено." ;;
    1)
        echo "Статус: Найдена критическая ошибка!" ;;
    *)
        echo "Статус: Неизвестный код." ;;
esac
