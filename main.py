#Ввод исходного текста
source_text_str = 'Все счастливые семьи похожи друг на друга, каждая несчастливая семья несчастлива по-своему. Все смешалось в доме Облонских. Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой, и объявила мужу, что не может жить с ним в одном доме. Положение это'
print()
print('Исходный текст:')
print(source_text_str)

#Удаление знаков препинания с помощью методов строк
source_text_str = source_text_str.replace('.', (''))
source_text_str = source_text_str.replace(',', (''))
print()
print('Текст без знаков препинания:')
print(source_text_str)

#Формирование списка со словами
source_list = source_text_str.split()
print()
print('Список слов из текста:')
print(source_list)

#Приведение всех слов к нижнему регистру
source_list_low = list(map(str.lower, source_list))
print()
print('Все слова в нижнем регистре:')
print(source_list_low)

#Лемматизация
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
for word_number in range(len(source_list_low)):
    temp_word = morph.parse(source_list_low[word_number])[0]
    source_list_low[word_number] = temp_word.normal_form
print()
print('Все слова в нормальной (словарной) форме:')
print(source_list_low)

#Вывод количества разных слов в тексте и получение словаря
unique_words_list = list(set(source_list_low))
print()
print('Количество разных слов в тексте: ', len(unique_words_list))
print()
print('Словарь из слов текста и их количества:')
text_dict = {}
for list_element_number in range(len(unique_words_list)):
    number_of_repeats = 0
    for i in range(len(source_list_low)):
        if source_list_low[i] == unique_words_list[list_element_number]:
            number_of_repeats+= 1
    text_dict[unique_words_list[list_element_number]] = number_of_repeats
print(text_dict)

#Вывод 5 наиболее часто встречающихся слов
aux_list = list(text_dict.items())
aux_list.sort(key = lambda i: i[1])
print()
print('5 самых частых слов в тексте:')
for diad_number in range(len(aux_list)-5, len(aux_list), 1):
    inner_aux_list = list(aux_list[diad_number])
    print('Количество повторений слова', inner_aux_list[0], '-', inner_aux_list[1])


