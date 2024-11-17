p1 = 'lot of money'
p2 = 'buy now'
p3 = 'subscribe'
p4 = 'click this'

msg = input('Enter your msg: ')

if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print('This sentence has spam')
else:
    print('Not spam')