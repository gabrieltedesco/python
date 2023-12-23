def firstn_gen(n):
    control = 0
    while n != control:
        yield control
        control += 1

def firstn(n):
    nums = []
    control = 0
    while control < n:
        nums.append(control)
        control += 1
    return nums

print(firstn(10))
print(list(firstn_gen(10)))
