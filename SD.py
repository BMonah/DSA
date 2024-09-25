import os

os.chdir('/Users/bonnymonah/Desktop/AWS Cloud SAA03/Important')
print(os.getcwd())

sample = [7119087, 18233, 43355]
id = 'PTGUBGG'
arr = []
for num in sample:
    num = str(num)
    res = num+id
    arr.append(res)
print(arr)
