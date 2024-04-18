from collections import deque


def stock_availability(boxes, action, *args):
    inventory_boxes = deque(boxes)

    if action == 'delivery':
        for el in args:
            inventory_boxes.append(el)
    elif action == 'sell':
        if inventory_boxes and not args:
            inventory_boxes.popleft()

        elif len(args) == 1 and type(args[0]) == int:
            for _ in range(int(args[0])):
                if inventory_boxes:
                    inventory_boxes.popleft()

        else:
            for arg in args:
                while inventory_boxes and arg in inventory_boxes:
                    inventory_boxes.remove(arg)

    return [el for el in inventory_boxes]




print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))