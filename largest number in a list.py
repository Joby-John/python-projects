# largest number in a list containing numbers below 100
largest = -1
least = 100
count = 0
sum = 0
for pr_num in [25,12,85,32,5,75,37]:
    count = count+1
    sum = sum+pr_num
    if pr_num > largest:
        largest = pr_num
    elif pr_num < least:
        least = pr_num    

print('largest: ', largest)
print('least:', least)
print('total sum: ', sum)
print('No. of compared elements: ', count)     
print('average: ', sum/count)  
print('Range: ', largest-least) 