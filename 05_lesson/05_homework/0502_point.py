# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('text.txt') as f:
    file = f.read()
    lines = file.splitlines()
    print(f'В файле - {len(lines)} строк(и)')
    line = 1
    for word in lines:
        print(f"В строке {line} - {len(word.split(' '))} слов(а)")
        line += 1