def test(d,a):
    if d == 'R':
        print(sorted(a))
    else:
        print(sorted(a,reverse=True)) 

test('R', [3, 2, 1, 2])
test('L', [1, 4, 5, 3, 5])