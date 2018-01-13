# coding: utf-8

def read_cook_book():
    with open("cook-book.txt") as cb:
        list_dish_name = []
        list_ingridient = []
        for line in cb:
            dish_name = line.strip()
            list_dish_name.append(dish_name)
            ammount_dishes = cb.readline()
            ingridient_list = []
            for i in range(int(ammount_dishes)):
                fields = cb.readline()
                fields = fields.split(" | ")
                cook_book_key = {}
                cook_book_key["ingridient_name"] = fields[0]
                cook_book_key["quantity"] = int(fields[1])
                cook_book_key["measure"] = fields[2].rstrip()
                ingridient_list.append(cook_book_key)
            cb.readline()
            list_ingridient.append(ingridient_list)

        ingridients_dict = dict()
        count = 0
        for elem in list_dish_name:
            ingridients_dict[elem] = list_ingridient[count]
            count += 1
        return ingridients_dict


def get_shop_list_by_dishes(dishes, person_count, populate_cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in populate_cook_book[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую + пробел): ') \
        .title().split(', ')
    populate_cook_book = read_cook_book()
    shop_list = get_shop_list_by_dishes(dishes, person_count, populate_cook_book)
    print_shop_list(shop_list)


create_shop_list()
