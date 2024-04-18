from collections import deque

colors_string = deque(input().split())

collected_colours = []
main_colors = ["red", "yellow", "blue"]
sec_colors = {"orange": ["red", "yellow"], "purple":["red", "blue"], "green":["yellow", "blue"]}

while colors_string :
    first_str = colors_string.popleft()
    last_str = colors_string.pop() if colors_string else ''
    if first_str + last_str in main_colors or first_str + last_str in sec_colors:
        collected_colours.append(first_str + last_str)
    elif last_str + first_str in main_colors or last_str + first_str in sec_colors:
        collected_colours.append(last_str + first_str)
    else:
        if len(first_str) > 1:
            colors_string.insert(len(colors_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_string.insert(len(colors_string) // 2, last_str[:-1])
for color in collected_colours:
    if color in sec_colors:
        for el in sec_colors[color]:
            if el not in collected_colours:
                collected_colours.remove(color)
                break

print(collected_colours)
