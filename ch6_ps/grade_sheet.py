num = int(input('enter your number : '))

if(num >= 50 and num <= 60):
    print('B+')
elif(num >= 61 and num <= 70):
    print('A-')
elif(num >= 71 and num <= 79):
    print('A')
elif(num >= 80 and num <= 100):
    print('A+')
elif(num >= 40 and num <= 49):
    print('D+')
else:
    print('you failed')