def custom_write(file_name, strings):
    strings = 0
    strings_positions = {}
    for i in info:
        file = open(file_name, 'a', encoding='utf-8')
        tell = (file.tell())
        strings += 1
        file.write(f'{i}\n')
        file.close()
        strings_positions.update({(strings, tell) : i})
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)