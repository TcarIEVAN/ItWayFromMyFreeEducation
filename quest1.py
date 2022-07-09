
a = "agility"[2:5] + "taxonomy"[3:6]
print(a) # iliono // то есть сумма символов /n
         #       // под индексами 2-5 + 3-6
b = [115,202,192,334,257][:4]
print(b) # исчезновение по индексу 4
c = len("crazy"[3:3+4]) # длина от 3-его по 7ой символ
print(c) # 2
d = [9,8,7,6,5,4,3,2,1][-3:] # последние 3 символа
print(d) # [3, 2, 1]
e = type([False,True,False,True][2:3])
print(e)
f = "---".join( "this is important".split() )
print(f)
g = int( ''.join( "7/7/07".split('/') ) )
print(g)
k = "too soon to tell".replace('o','*').replace('* ','')
print(k)
