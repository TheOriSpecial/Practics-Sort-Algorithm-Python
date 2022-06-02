
arr = []
with open('Test.txt','r+') as f:
    arr = [row.strip('.,!?') for row in f.read().split()]
print(arr)

with open('TestOutput.txt','w') as ff:
    for j in range(len(arr)):
        ff.writelines(arr[j] + '\n')
