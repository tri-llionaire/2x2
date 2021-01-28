import random, itertools
def scramble(current, entered_scramble):
    for x in entered_scramble.split():
        if x == 'R':
            move = '080102110405060720091023131415121603001918212217'
        elif x == 'R\'':
            move = '180102170405060700091003151213141623201908212211'
        elif x == 'R2':
            move = '200102230405060718091017141512131611081900212203'
        elif x == 'U':
            move = '010203000809060712131011161714150405181920212223'
        elif x == 'U\'':
            move = '030001021617060704051011080914151213181920212223'
        elif x == 'U2':
            move = '020300011213060716171011040514150809181920212223'
        elif x == 'F':
            move = '000107042105062009101108120203151617181913142223'
        elif x == 'F\'':
            move = '000113140305060211080910122021151617181907042223'
        elif x == 'F2':
            move = '000120211405061310110809120704151617181902032223'
        elif x == 'L':
            move = '001916030506070408010211121314152217182120091023'
        elif x == 'L\'':
            move = '000910030704050608212211121314150217180120191623'
        elif x == 'L2':
            move = '002122030607040508191611121314151017180920010223'
        elif x == 'D':
            move = '000102030405181908090607121310111617141521222320'
        elif x == 'D\'':
            move = '000102030405101108091415121318191617060723202122'
        elif x == 'D2':
            move = '000102030405141508091819121306071617101122232021'
        elif x == 'B':
            move = '151202030400010708091011231314221718191620210506'
        elif x == 'B\'':
            move = '050602030422230708091011011314001916171820211512'
        elif x == 'B2':
            move = '222302030415120708091011061314051819161720210001'
        elif x == 'x':
            move = '080910110704050620212223131415120203000118191617'
        elif x == 'x\'':
            move = '181916170506070400010203151213142223202108091011'
        elif x == 'x2':
            move = '202122230607040518191617141512131011080900010203'
        elif x == 'y':
            move = '010203000809101112131415161718190405060723202122'
        elif x == 'y\'':
            move = '030001021617181904050607080910111213141521222320'
        elif x == 'y2':
            move = '020300011213141516171819040506070809101122232021'
        elif x == 'z':
            move = '050607042122232009101108010203001916171813141512'
        elif x == 'z\'':
            move = '151213140300010211080910232021221718191607040506'
        elif x == 'z2':
            move = '222320211415121310110809060704051819161702030001'
        else:
            pass
        new = list(current)
        for i in range(24):
            new[i] = current[int(move[(2*i):(2*i)+2])]
        current = ''.join(new)
    return current + entered_scramble
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
    if u[:4] == 'wwww':
        return 'white'
    elif u[4:8] == 'oooo':
        return 'orange'
    elif u[8:12] == 'gggg':
        return 'green'
    elif u[12:16] == 'rrrr':
        return 'red'
    elif u[16:20] == 'bbbb':
        return 'blue'
    elif u[20:24] == 'yyyy':
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
