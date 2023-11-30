# define sum_of_squares = 0
sum_of_sqaures = 0
# define sum = 0
sum = 0
# define i = 1
i = 1

# while i <= 100
while i <= 100:
    # sum_of_sqaures = sum_of_squares + i * i
    sum_of_sqaures += i * i
    # sum = sum + i
    sum += i
    # i = i + 1
    i += 1

# square_of_sum = sum * sum
square_of_sum = sum ** 2
# diff = square_of_sum - sum_of_squares
diff = square_of_sum - sum_of_sqaures
# display diff
print(diff)