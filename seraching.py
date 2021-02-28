shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
item_to_find = "spam"
found_at = None

# for index in range(len(shopping_list)):
#    if shopping_list[index] == item_to_find:
#        found_at = index
#        break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print(f"Item found at position {found_at}")
else:
    print(f"{item_to_find} not found")




