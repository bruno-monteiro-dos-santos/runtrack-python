def draw_carpet(n):
    T=n
    for i in range((n+1)*T):
        for j in range ((n+1)*T):
            if (i//T + j//T) % 2==0:
                if i % T == j % T:
                    print('x', end='')
                else:
                    print('.', end='')
                
            else:
                if i % T == T - j % T - 1:
                    print('x', end='')
                else:
                    print('.', end='')
        print()

draw_carpet(10)
