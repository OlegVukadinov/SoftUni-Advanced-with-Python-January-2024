numbers = list(map(int, input().split()))

negative_nums = 0
positive_nums = 0

for el in numbers:
    if el >= 0:
        positive_nums += el
    else:
        negative_nums += el

total_sum = negative_nums + positive_nums
print(negative_nums)
print(positive_nums)

if abs(negative_nums) > positive_nums:
    print("The negatives are stronger than the positives")

elif abs(negative_nums) < positive_nums:
    print("The positives are stronger than the negatives")

