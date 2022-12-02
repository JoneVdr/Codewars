def next_bigger(n):
        next_bigger(num= 12)
        next_bigger(num= 513)
        next_bigger(num= 2017)
        next_bigger(num= 9)
        next_bigger(num= 111)
        next_bigger(num= 531)
        num = (i, j)
while True:
    if i > j:
        num = (i, j)
    if i < j:
        num = (j, i)
    if i == j:
        num = (i, j)
        print ("-1")
        break

