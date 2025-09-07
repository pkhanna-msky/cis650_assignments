measures = [10, 10.1, 9.9, 10.1, 9.9, 9.8, 9.9, 10.3,10]

#(a) Average
total = 0.0
count = 0
for x in measures:
    total += x
    count += 1
average = total / count
print(f'(a) Average: {average: .2f}')

#(b) Standard deviation
# First compute sum of squared diviation from the mean
ssd = 0.0
for x in measures:
    diff = x -average
    ssd += diff * diff

#Population SD: divide by n
pop_sd = (ssd / count) ** 0.5
print(f'(b) Population SD: {pop_sd: .2f}')

