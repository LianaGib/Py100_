# TODO  Напишите функцию count_letters
def count_letters(text):
    letters = []
    dict_0 = {}
    for i in text.lower():
        if i.isalpha():
            letters.append(i)
    dict_letters = dict_0.fromkeys(letters, 1)
    for i in dict_letters:
        count = 0
        for a in letters:
            if i == a:
                count += 1
                dict_0[i] = count
    return dict_0


#dict_letter = count_letters(main_str)
def calculate_frequency(dict_letter):
    dict_2 = {}
    for key, value in dict_letter.items():
        total_1 = value/sum(dict_letter.values())
        dict_2[key] = round(total_1, 2)
    for key, value in dict_2.items():
        print(f'{key}: {value}')


# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count_letters(main_str)
dict_letter = count_letters(main_str)
calculate_frequency(dict_letter)
