def func(**kwargs):
    return kwargs['a'] + kwargs['b'] * kwargs['c']


# Change any param position kwargs automatically finds key itself
ans = func(a=1, b=2, c=3)
print(ans)
