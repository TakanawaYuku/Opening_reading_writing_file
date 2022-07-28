import os


def gen_cook_book(f):
    """генератор словаря из f"""
    book = {}
    gen = (line.strip() for line in f if line.strip() != '')
    structure = ['ingredient_name', 'quantity', 'measure']
    for rew in gen:
        if "|" not in rew and not rew.strip().isdigit():
            book[rew] = []
            key = rew
        elif "|" in rew:
            s = rew.split(' | ')
            s[1] = int(s[1])
            dt = dict(zip(structure, s))
            book[key].append(dt)
    return book


def init_cook_book(file):
    """Оболочка для чтения файла"""
    with open(file, encoding="utf-8") as f:
        book = gen_cook_book(f)
    return book


def get_shop_list_by_dishes(dishes, person_count):
    """Генератор словаря с игредиентами для блюд"""
    for_dishes = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            name = ingr['ingredient_name']
            if name in for_dishes:
                for_dishes[name]['quantity'] += ingr['quantity'] * person_count
            else:
                for_dishes[name] = {'measure': ingr['measure'], 'quantity': ingr['quantity'] * person_count}
    return for_dishes


FILE_NAME = 'recipes.txt'
BASE_PATH = os.getcwd()
file_path = os.path.join(BASE_PATH, FILE_NAME)

cook_book = init_cook_book(file_path)

list_by_dishes = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4)
print(list_by_dishes)