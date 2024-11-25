# Генераторы:
def all_variants(text):
    for i in range(len(text)): # Запуск цикла перебора элементов text
        for j in range(len(text) - i):  # Запуск цикла перебора элементов text - i элемент
            yield text[j:j + i + 1] # подпоследовательность переданной строки

a = all_variants("abc")
for i in a:
    print(i)