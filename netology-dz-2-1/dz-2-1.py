#coding: utf-8

def cook_book_funk():
	list_dish_name = []
	list_ingridient = []
	with open("cook-book.txt") as cb:
		for line in cb:
			dish_name = line.strip()
			list_dish_name.append(dish_name)
			ammount_disches = cb.readline()
			ingridient_list = []
			for elem in range(int(ammount_disches)):
				fields = cb.readline()
				fields = fields.split(" | ")
				l = [line.rstrip() for line in fields]
				ingridient_list.append(l)
			cb.readline()
			list_ingridient.append(ingridient_list)

	ingridient_dict = []
	for element in list_ingridient:
		dict_elem = []
		for elementen in element:
			cook_book_key = {}
			cook_book_key["ingridient_name"] = elementen[0]
			cook_book_key["quantity"] = int(elementen[1])
			cook_book_key["measure"] = elementen[2]
			dict_elem.append(cook_book_key)
		ingridient_dict.append(dict_elem)
	ingridients_dict = dict()
	count = 0
	for elem in list_dish_name:
		ingridients_dict[elem] = ingridient_dict[count]
		count += 1
	return(ingridients_dict)

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book_funk()[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую + пробел): ') \
    .title().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()