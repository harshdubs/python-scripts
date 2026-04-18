def normal_squares(n):
    sq = []
    for i in range(n):
        sq.append(i*i)
    return sq

def gen_squares(n):

    for i in range(n):
        yield i*i
i = gen_squares(5)

for a in range(5):
    print(next(i))
print(normal_squares(5))

print(next(i))