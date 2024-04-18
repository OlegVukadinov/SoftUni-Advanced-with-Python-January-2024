from collections import deque


def flights(*args):
    flights = {}
    destinations = [el for el in args if not isinstance(el, int)]
    passengers = deque(str(el) for el in args if not isinstance(el, str))
    for destination in destinations:
        if destination == "Finish":
            break

        elif destination in flights:
            current_passengers = int(passengers.popleft())
            flights[destination] += current_passengers
        else:
            current_passengers = int(passengers.popleft())
            flights[destination] = current_passengers
    return flights


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))