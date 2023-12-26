def days_to_flower(K, M, T, X):
    growth_per_night = K
    flower_threshold = M
    bird_eats = T
    final_height = X
    days = 0
    current_height = 0

    while current_height < final_height:
        days += 1
        current_height += growth_per_night

    if days % 7 == 0:
        current_height -= bird_eats

    if current_height >= flower_threshold:
        return days
    else:
        return -1

K, M, T, X = map(int, input().split())

result = days_to_flower(K, M, T, X)
print(result)