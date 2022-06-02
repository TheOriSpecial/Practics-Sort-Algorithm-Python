
mass = [1,5,9,7,3,6,4,8,2,651,22,8181,9999,1,0,1]
end = len(mass)
swaps = True
while end > 1 or swaps:
    end = max(1, int(end / 1.25))  # minimum end is 1
    swaps = False
    for i in range(len(mass) - end):
        j = i + end
        if mass[i] > mass[j]:
            mass[i], mass[j] = mass[j], mass[i]
            swaps = True

print (mass)
