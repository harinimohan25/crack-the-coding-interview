def array_left_rotation(a, n, k):
    for i in range(k):
        a.append(a.pop(0))
    return a

n, k = map(int, raw_input().strip().split(' '))
a = list(map(int, raw_input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))