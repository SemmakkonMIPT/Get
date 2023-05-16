import re

# открываем файлы
with open('numbers.txt', 'r') as infile, open('results.txt', 'w') as outfile:
    # читаем строки из файла numbers.txt
    for line in infile:
        # определяем, соответствует ли строка правильному формату
        if re.match(r'^(\+7|8)[\(\-]?9\d{2}[\)\-]?\d{2}[\-\s]?\d{2}[\-\s]?\d{3}$|^(\+7|8)?\(?(\d{3})\)?[\-\s]?(\d{3})[\-\s]?(\d{2})[\-\s]?(\d{2})$|^\d{5}\-\d{3}\-\d{4}$', line.strip()):
            # записываем правильный номер в файл results.txt
            outfile.write(line)