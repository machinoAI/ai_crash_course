def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("A"))
print(add_item("B"))



def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item("A"))
print(add_item("B"))