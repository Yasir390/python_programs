
marks1 = int(input('enter marks 1 : '))
marks2 = int(input('enter marks 2 : '))
marks3 = int(input('enter marks 3 : '))

totalPercentage = (marks1+marks2+marks3)/3

if(totalPercentage >= 40):
    print('you pass')
else:
    print('you failed')