from collections import deque

eggs = deque(map(int, input().split(", ")))
papers = deque(map(int, input().split(", ")))

filled_boxes = 0

while eggs and papers:
    egg = eggs[0]
    paper = papers[-1]

    if egg == 13:
        eggs.popleft()
        first_paper = papers.popleft()
        last_paper = papers.pop()
        papers.append(first_paper)
        papers.appendleft(last_paper)


    elif egg <= 0:
        eggs.popleft()
    elif egg + paper <= 50:
        eggs.popleft()
        papers.pop()
        filled_boxes += 1
    else:
        eggs.popleft()
        papers.pop()

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")


