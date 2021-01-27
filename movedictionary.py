import random, itertools
def or_L(current):
    lmove = '001916030506070408010211121314152217182120091023'
    new = list(current)
    for i in range(24):
        new[i] = current[int(lmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_Lp(current):
    lpmove = '000910030704050608212211121314150217180120191623'
    new = list(current)
    for i in range(24):
        new[i] = current[int(lpmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_Ld(current):
    ldmove = '002122030607040508191611121314151017180920010223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(ldmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_D(current):
    dmove = '000102030405181908090607121310111617141521222320'
    new = list(current)
    for i in range(24):
        new[i] = current[int(dmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_Dp(current):
    dpmove = '000102030405101108091415121318191617060723202122'
    new = list(current)
    for i in range(24):
        new[i] = current[int(dpmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_Dd(current):
    ddmove = '000102030405141508091819121306071617101122232021'
    new = list(current)
    for i in range(24):
        new[i] = current[int(ddmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_B(current):
    bmove = '151202030400010708091011231314221718191620210506'
    new = list(current)
    for i in range(24):
        new[i] = current[int(bmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_Bp(current):
    bpmove = '050602030423220708091011011314001916171820211512'
    new = list(current)
    for i in range(24):
        new[i] = current[int(bpmove[(2*i):(2*i)+2])]
    return ''.join(new)
def or_Bd(current):
    bdmove = '222302030415120708091011061314051819161720210001'
    new = list(current)
    for i in range(24):
        new[i] = current[int(bdmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_R(current):
    rmove = '080102110405060720091023131415121603001918212217'
    new = list(current)
    for i in range(24):
        new[i] = current[int(rmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_Rp(current):
    rpmove = '180102170405060700091003151213141623201908212211'
    new = list(current)
    for i in range(24):
        new[i] = current[int(rpmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_Rd(current):
    rdmove = '200102230405060718091017141512131611081900212203'
    new = list(current)
    for i in range(24):
        new[i] = current[int(rdmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_U(current):
    umove = '010203000809060712131011161714150405181920212223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(umove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_Up(current):
    upmove = '030001021617060704051011080914151213181920212223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(upmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_Ud(current):
    udmove = '020300011213060716171011040514150809181920212223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(udmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_F(current):
    fmove = '000107042105062009101108120203151617181913142223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(fmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_Fp(current):
    fpmove = '000113140305060211080910122021151617181907042223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(fpmove[(2*i):(2*i)+2])]
    return ''.join(new)
def move_Fd(current):
    fdmove = '000120211405061310110809120704151617181902032223'
    new = list(current)
    for i in range(24):
        new[i] = current[int(fdmove[(2*i):(2*i)+2])]
    return ''.join(new)
def rot_x(current):
    xmove = '080910110704050620212223131415120203000118191617'
    new = list(current)
    for i in range(24):
        new[i] = current[int(xmove[(2*i):(2*i)+2])]
    return ''.join(new)
def rot_xp(current):
    new = move_Rp(current)
    new = or_L(new)
    return new
def rot_xd(current):
    new = move_Rd(current)
    new = or_Ld(new)
    return new
def rot_y(current):
    new = move_U(current)
    new = or_Dp(new)
    return new
def rot_yp(current):
    new = move_Up(current)
    new = or_D(new)
    return new
def rot_yd(current):
    new = move_Ud(current)
    new = or_Dd(new)
    return new
def rot_z(current):
    new = move_F(current)
    new = or_Bp(new)
    return new
def rot_zp(current):
    new = move_Fp(current)
    new = or_B(new)
    return new
def rot_zd(current):
    new = move_Fd(current)
    new = or_Bd(new)
    return new
def scramble(current, entered_scramble):
    current = current + entered_scramble
    for x in entered_scramble.split():
        if x == 'R':
            current = move_R(current)
        elif x == 'R\'':
            current = move_Rp(current)
        elif x == 'R2':
            current = move_Rd(current)
        elif x == 'U':
            current = move_U(current)
        elif x == 'U\'':
            current = move_Up(current)
        elif x == 'U2':
            current = move_Ud(current)
        elif x == 'F':
            current = move_F(current)
        elif x == 'F\'':
            current = move_Fp(current)
        elif x == 'F2':
            current = move_Fd(current)
        elif x == 'L':
            current = or_L(current)
        elif x == 'L\'':
            current = or_Lp(current)
        elif x == 'L2':
            current = or_Ld(current)
        elif x == 'D':
            current = or_D(current)
        elif x == 'D\'':
            current = or_Dp(current)
        elif x == 'D2':
            current = or_Dd(current)
        elif x == 'B':
            current = or_B(current)
        elif x == 'B\'':
            current = or_Bp(current)
        elif x == 'B2':
            current = or_Bd(current)
        elif x == 'x':
            current = rot_x(current)
        elif x == 'x\'':
            current = rot_xp(current)
        elif x == 'x2':
            current = rot_xd(current)
        elif x == 'y':
            current = rot_y(current)
        elif x == 'y\'':
            current = rot_yp(current)
        elif x == 'y2':
            current = rot_yd(current)
        elif x == 'z':
            current = rot_z(current)
        elif x == 'z\'':
            current = rot_zp(current)
        elif x == 'z2':
            current = rot_zd(current)
        else:
            pass
    return current
def issolved(status):
    if (status[0] == status[1] == status[2] == status[3]) and (status[4] == status[5] == status[6] == status[7]) and (status[8] == status[9] == status[10] == status[11]) and (status[12] == status[13] == status[14] == status[15]) and (status[16] == status[17] == status[18] == status[19]) and (status[20] == status[21] == status[22] == status[23]):
        return True
    else:
        return False
def guesses(repeating):
    was = ''; todo = []; bad = 0; moves = ['R', 'R\'', 'R2', 'U', 'U\'', 'U2', 'F', 'F\'', 'F2']
    for x in itertools.product(moves, repeat=repeating):
        for i in x:
            if i[0] == was:
                bad = 1
            was = i[0]
        if bad == 0:
            todo.append(' '.join(x))
            was = ''
        bad = 0
    return todo
def output(scrambled):
    print('     {} {}\n     {} {}\n{} {}  {} {}  {} {}  {} {}\n{} {}  {} {}  {} {}  {} {}\n     {} {}\n     {} {}'.format(scrambled[1], scrambled[0], scrambled[2], scrambled[3], scrambled[5], scrambled[4], scrambled[9], scrambled[8], scrambled[13], scrambled[12], scrambled[17], scrambled[16], scrambled[6], scrambled[7], scrambled[10], scrambled[11], scrambled[14], scrambled[15], scrambled[18], scrambled[19], scrambled[21], scrambled[20], scrambled[22], scrambled[23]))
def clean(string):
    string = string.split()
    for x in range(6):
        try:
            if string[x][0] == string[x+1][0]:
                a = string[x]; b = string[x+1]
                del string[x+1]
                if a == 'R':
                    if b == 'R':
                        string[x] = 'R2'
                    elif b == 'R\'':
                        del string[x]
                    else:
                        string[x] = 'R\''
                elif a == 'U':
                    if b == 'U':
                        string[x] = 'U2'
                    elif b == 'U\'':
                        del string[x]
                    else:
                        string[x] = 'U\''
                elif a == 'F':
                    if b == 'F':
                        string[x] = 'F2'
                    elif b == 'F\'':
                        del string[x]
                    else:
                        string[x] = 'F\''
                elif a == 'R\'':
                    if b == 'R':
                        del string[x]
                    elif b == 'R\'':
                        string[x] = 'R2'
                    else:
                        string[x] = 'R'
                elif a == 'U\'':
                    if b == 'U2':
                        string[x] = 'U'
                    elif b == 'U':
                        del string[x]
                    else:
                        string[x] = 'U2'
                elif a == 'F\'':
                    if b == 'F\'':
                        string[x] = 'F2'
                    elif b == 'F2':
                        string[x] = 'F'
                    else:
                        del string[x]
                elif a == 'R2':
                    if b == 'R':
                        string[x] = 'R\''
                    elif b == 'R2':
                        del string[x]
                    else:
                        string[x] = 'R'
                elif a == 'U2':
                    if b == 'U':
                        string[x] = 'U\''
                    elif b == 'U2':
                        del string[x]
                    else:
                        string[x] = 'U'
                else:
                    if b == 'F\'':
                        string[x] = 'F'
                    elif b == 'F2':
                        del string[x]
                    else:
                        string[x] = 'F'
        except:
            pass
    return ' '.join(string)
def generate():
    last = 'i'; scramble = ''; moves = ['R', 'R\'', 'R2', 'U', 'U\'', 'U2', 'F', 'F\'', 'F2']
    for i in 'twelveletter':
        index = random.randint(0, 8)
        while last[0] == moves[index][0]:
            index = random.randint(0, 8)
        scramble = scramble + moves[index] + ' '
        last = moves[index]
    return scramble
def find(u):
    if u[:4] == ['w', 'w', 'w', 'w']:
        return 'white'
    elif u[4:8] == ['o', 'o', 'o', 'o']:
        return 'orange'
    elif u[8:12] == ['g', 'g', 'g', 'g']:
        return 'green'
    elif u[12:16] == ['r', 'r', 'r', 'r']:
        return 'red'
    elif u[16:20] == ['b', 'b', 'b', 'b']:
        return 'blue'
    elif u[20:24] == ['y', 'y', 'y', 'y']:
        return 'yellow'
    else:
        return ''
def reverse(v):
    newv = ''
    for i in v[24:].split()[::-1]:
        if i == 'R':
            newv = newv + 'R\' '
        elif i == 'U':
            newv = newv + 'U\' '
        elif i == 'F':
            newv = newv + 'F\' '
        elif i == 'R\'':
            newv = newv + 'R '
        elif i == 'U\'':
            newv = newv + 'U '
        elif i == 'F\'':
            newv = newv + 'F '
        else:
            newv = newv + i + ' '
    return newv
