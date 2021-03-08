

translate = {'ten': 'Десять', 'nine': 'Девять', 'eight': 'Восемь', 'seven': 'Семь', 'six': 'Шесть', 'five': 'Пять', 'four': 'Четыре', 'three': 'Три', 'two': 'два', 'one': 'один', 'zero': 'ноль'}
def num_translate(number):
   return translate.get(number)
print(num_translate('zero'))
print(num_translate('one'))
print(num_translate('two'))
print(num_translate('three'))
print(num_translate('four'))
print(num_translate('five'))
print(num_translate('six'))
print(num_translate('seven'))
print(num_translate('eight'))
print(num_translate('nine'))
print(num_translate('ten'))

