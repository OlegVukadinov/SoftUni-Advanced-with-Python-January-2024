n, m = map(int, input().split())

n_set = set()
m_set = set()

for _ in range(n):
    num = int(input())
    n_set.add(num)

for _ in range(m):
    num = int(input())
    m_set.add(num)

common_el = n_set.intersection(m_set)

for el in common_el:
    print(el)

