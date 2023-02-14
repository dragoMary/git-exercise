from collections import Counter
from data import stock

def get_user_name():
    return input('Enter your name: ')

def greet_user(name):
    print(f'Hello {name}')

def get_operation_selected():
    print('1. List items by warehouse')
    print('2. Search and order an item')
    print('3. Browse by category')
    print('4. Quit'
    return int(input('Pick any statement by its number: '))


def main():
    name = get_user_name()
    greet_user(name)
    operation = get_operation_selected()



if __name__ == '__main__':
    main()






def list_items_by_warehouse():
    warehouses = {}
    for item in stock:
        warehouse_number = item['warehouse']
        item_name = item['state'] + ' ' + item['category']
        if warehouse_number not in warehouses:
            warehouses[warehouse_number] = []
        warehouses[warehouse_number].append(item_name)

    print(f'Total warehouses number: {len(warehouses)}')
    for warehouse_number, items in warehouses.items():
        print(f'Warehouse number: {warehouse_number}')
        print(f'Items: {items}')

def search_and_order_item():
    item_name = input('Enter the name of the item you want to search and order: ')
    item_found = False
    for item in stock:
        if item_name.lower() in (item['state'] + ' ' + item['category']).lower():
            item_found = True
            item_count = Counter([item["state"] + " " + item["category"] + " - Warehouse " + str(item["warehouse"]) for item in stock if item_name.lower() in (item['state'] + ' ' + item['category']).lower()])
            for item, count in item_count.items():
                print(f'Item "{item}" is in stock {count} amount')
            break
    if not item_found:
        print('Item not found in stock.')
    else:
        available_warehouses = [item.split(" - Warehouse ")[1] for item, count in item_count.items()]
        print(f'Available warehouses: {available_warehouses}')
        selected_warehouse = int(input('Enter the warehouse number: '))
        if str(selected_warehouse) not in available_warehouses:
            print(f"The warehouse number you entered is invalid.")
        else:
            for item, count in item_count.items():
                if str(selected_warehouse) in item.split(" - Warehouse "):
                    selected_item = item
                    selected_item_count = count
                    break

            while True:
                order_quantity = int(input('Enter the amount you want to order: '))
                if order_quantity > selected_item_count:
                    print(f"The maximum amount you can order is {selected_item_count}")
                else:
                    print(f"You have ordered {order_quantity} {selected_item.split(' - Warehouse ')[0]}")
                    for item in stock:
                        if (item['state'] + ' ' + item['category']).lower() == selected_item.lower() and item[
                            'warehouse'] == selected_warehouse:
                            item['count'] -= order_quantity
                            break

                    break

list_items_by_warehouse()




def browse_by_category():
    categories = Counter([item["category"] for item in stock])
    print("Categories: ")
    for index, (category, count) in enumerate(categories.items()):
        print(f"{index + 1}. {category} ({count} items)")

    selected_category = int(input("Enter the number of the category you would like to see: "))
    selected_category_name = list(categories.keys())[selected_category - 1]

    items_in_selected_category = [item for item in stock if item["category"] == selected_category_name]
    print(f"There are {len(items_in_selected_category)} items in the {selected_category_name} category.")

    for item in items_in_selected_category:
        item_info = f"{item['state']} - Warehouse {item['warehouse']}"
        print(f"{item['category']}: {item_info}")
search_and_order_item()




print(f'{name}, thank you for the visit.')