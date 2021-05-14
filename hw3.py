def thesaurus(*names):
    res = {}
    for name in names:
        first_letter = name[0].capitalize()
        
        if first_letter not in res:
            res[first_letter] = []
        
        res[first_letter].append(name)
    return res


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# def thesaurus_adv(*full_names):
#     res = {}
#     for name in full_names:
#         first_last_name_letter = name[5].capitalize()
        
#         if first_last_name_letter not in res:
#             res[first_last_name_letter] = {}
#         print(res)
    
#     for name in full_names:
#         first_name_letter = name[0].capitalize()
        
#         if first_name_letter not in res:
#             res[first_last_name_letter[first_name_letter]] = []

        

#     return res


# print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))