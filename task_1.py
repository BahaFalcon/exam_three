def transform(some_list):
    """
    Функция для создания словаря с ключами “int”, “float”, “str”, “bool”, “none”
    :param some_list: задаем параметры
    :return: возвращаем словарь
    """
    keys_dict = {}
    for i in some_list:
        if isinstance(i, float):
            keys_dict.update({'float': i})
        elif isinstance(i, bool):
            keys_dict.update({'bool': i})
        elif isinstance(i, str):
            keys_dict.update({'str': i})
        elif isinstance(i, int):
            keys_dict.update({'int': i})
        else:
            keys_dict.update({'none': i})
    return keys_dict


values = [2, 4.7, "hi", False, None]

print(transform(values))
