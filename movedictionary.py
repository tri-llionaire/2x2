import random, itertools
def or_L(current):
    new = list(current)
    new[2] = current[20]
    new[3] = current[17]
    new[10] = current[2]
    new[11] = current[3]
    new[17] = current[23]
    new[20] = current[22]
    new[22] = current[10]
    new[23] = current[11]
    new[5] = current[6]
    new[6] = current[7]
    new[7] = current[8]
    new[8] = current[5]
    return new
def or_Lp(current):
    new = list(current)
    new[2] = current[10]
    new[3] = current[11]
    new[10] = current[22]
    new[11] = current[23]
    new[17] = current[3]
    new[20] = current[2]
    new[22] = current[20]
    new[23] = current[17]
    new[5] = current[8]
    new[6] = current[5]
    new[7] = current[6]
    new[8] = current[7]
    return new
def or_Ld(current):
    new = list(current)
    new[2] = current[22]
    new[3] = current[23]
    new[10] = current[20]
    new[11] = current[17]
    new[17] = current[11]
    new[20] = current[10]
    new[22] = current[2]
    new[23] = current[3]
    new[5] = current[7]
    new[6] = current[8]
    new[7] = current[5]
    new[8] = current[6]
    return new
def or_D(current):
    new = list(current)
    new[7] = current[19]
    new[8] = current[20]
    new[11] = current[7]
    new[12] = current[8]
    new[15] = current[11]
    new[16] = current[12]
    new[19] = current[15]
    new[20] = current[16]
    new[21] = current[22]
    new[22] = current[23]
    new[23] = current[24]
    new[24] = current[21]
    return new
def or_Dp(current):
    new = list(current)
    new[7] = current[11]
    new[8] = current[12]
    new[11] = current[15]
    new[12] = current[16]
    new[15] = current[19]
    new[16] = current[20]
    new[19] = current[7]
    new[20] = current[8]
    new[21] = current[24]
    new[22] = current[21]
    new[23] = current[22]
    new[24] = current[23]
    return new
def or_Dd(current):
    new = list(current)
    new[7] = current[15]
    new[8] = current[16]
    new[11] = current[19]
    new[12] = current[20]
    new[15] = current[7]
    new[16] = current[8]
    new[19] = current[11]
    new[20] = current[12]
    new[21] = current[23]
    new[22] = current[24]
    new[23] = current[21]
    new[24] = current[22]
    return new
def or_B(current):
    new = list(current)
    new[1] = current[16]
    new[2] = current[13]
    new[6] = current[1]
    new[7] = current[2]
    new[13] = current[24]
    new[16] = current[23]
    new[23] = current[6]
    new[24] = current[7]
    new[17] = current[18]
    new[18] = current[19]
    new[19] = current[20]
    new[20] = current[17]
    return new
def or_Bp(current):
    new = list(current)
    new[1] = current[6]
    new[2] = current[7]
    new[6] = current[24]
    new[7] = current[23]
    new[13] = current[2]
    new[16] = current[1]
    new[23] = current[16]
    new[24] = current[13]
    new[17] = current[20]
    new[18] = current[17]
    new[19] = current[18]
    new[20] = current[19]
    return new
def or_Bd(current):
    new = list(current)
    new = list(current)
    new[1] = current[23]
    new[2] = current[24]
    new[6] = current[16]
    new[7] = current[13]
    new[13] = current[7]
    new[16] = current[6]
    new[23] = current[1]
    new[24] = current[2]
    new[17] = current[19]
    new[18] = current[20]
    new[19] = current[17]
    new[20] = current[18]
    return new
def move_R(current):
    new = list(current)
    new[1] = current[9]
    new[4] = current[12]
    new[9] = current[21]
    new[12] = current[24]
    new[18] = current[4]
    new[19] = current[1]
    new[21] = current[19]
    new[24] = current[18]
    new[13] = current[14]
    new[14] = current[15]
    new[15] = current[16]
    new[16] = current[13]
    return new
def move_Rp(current):
    new = list(current)
    new[1] = current[19]
    new[4] = current[18]
    new[9] = current[1]
    new[12] = current[4]
    new[18] = current[24]
    new[19] = current[21]
    new[21] = current[9]
    new[24] = current[12]
    new[13] = current[16]
    new[14] = current[13]
    new[15] = current[14]
    new[16] = current[15]
    return new
def move_Rd(current):
    new = list(current)
    new[1] = current[21]
    new[4] = current[24]
    new[9] = current[19]
    new[12] = current[18]
    new[18] = current[12]
    new[19] = current[9]
    new[21] = current[1]
    new[24] = current[4]
    new[13] = current[15]
    new[14] = current[16]
    new[15] = current[13]
    new[16] = current[14]
    return new
def move_U(current):
    new = list(current)
    new[5] = current[9]
    new[6] = current[10]
    new[9] = current[13]
    new[10] = current[14]
    new[13] = current[17]
    new[14] = current[18]
    new[17] = current[5]
    new[18] = current[6]
    new[1] = current[2]
    new[2] = current[3]
    new[3] = current[4]
    new[4] = current[1]
    return new
def move_Up(current):
    new = list(current)
    new[5] = current[17]
    new[6] = current[18]
    new[9] = current[5]
    new[10] = current[6]
    new[13] = current[9]
    new[14] = current[10]
    new[17] = current[13]
    new[18] = current[14]
    new[1] = current[4]
    new[2] = current[1]
    new[3] = current[2]
    new[4] = current[3]
    return new
def move_Ud(current):
    new = list(current)
    new[5] = current[13]
    new[6] = current[14]
    new[9] = current[17]
    new[10] = current[18]
    new[13] = current[5]
    new[14] = current[6]
    new[17] = current[9]
    new[18] = current[10]
    new[1] = current[3]
    new[2] = current[4]
    new[3] = current[1]
    new[4] = current[2]
    return new
def move_F(current):
    new = list(current)
    new[3] = current[8]
    new[4] = current[5]
    new[5] = current[22]
    new[8] = current[21]
    new[14] = current[3]
    new[15] = current[4]
    new[21] = current[14]
    new[22] = current[15]
    new[9] = current[10]
    new[10] = current[11]
    new[11] = current[12]
    new[12] = current[9]
    return new
def move_Fp(current):
    new = list(current)
    new[3] = current[14]
    new[4] = current[15]
    new[5] = current[4]
    new[8] = current[3]
    new[14] = current[21]
    new[15] = current[22]
    new[21] = current[8]
    new[22] = current[5]
    new[9] = current[12]
    new[10] = current[9]
    new[11] = current[10]
    new[12] = current[11]
    return new
def move_Fd(current):
    new = list(current)
    new[3] = current[21]
    new[4] = current[22]
    new[5] = current[15]
    new[8] = current[14]
    new[14] = current[8]
    new[15] = current[5]
    new[21] = current[3]
    new[22] = current[4]
    new[9] = current[11]
    new[10] = current[12]
    new[11] = current[9]
    new[12] = current[10]
    return new
def rot_x(current):
    new = move_R(current)
    new = or_Lp(new)
    return new
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
    current[25] = entered_scramble
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
    if (status[1] == status[2] == status[3] == status[4]) and (status[5] == status[6] == status[7] == status[8]) and (status[9] == status[10] == status[11] == status[12]) and (status[13] == status[14] == status[15] == status[16]) and (status[17] == status[18] == status[19] == status[20]) and (status[21] == status[22] == status[23] == status[24]):
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
    print('     {} {}\n     {} {}\n{} {}  {} {}  {} {}  {} {}\n{} {}  {} {}  {} {}  {} {}\n     {} {}\n     {} {}'.format(scrambled[2], scrambled[1], scrambled[3], scrambled[4], scrambled[6], scrambled[5], scrambled[10], scrambled[9], scrambled[14], scrambled[13], scrambled[18], scrambled[17], scrambled[7], scrambled[8], scrambled[11], scrambled[12], scrambled[15], scrambled[16], scrambled[19], scrambled[20], scrambled[22], scrambled[21], scrambled[23], scrambled[24]))
def remove(string):
    string = string.split()
    last = '0'
    h = 0
    for x in string:
        if last[0] == x[0]:
            h = 1
        last = x
    if h == 1:
        return True
    else:
        return False
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
    if u[1:5] == ['w', 'w', 'w', 'w']:
        return 'white'
    elif u[5:9] == ['o', 'o', 'o', 'o']:
        return 'orange'
    elif u[9:13] == ['g', 'g', 'g', 'g']:
        return 'green'
    elif u[13:17] == ['r', 'r', 'r', 'r']:
        return 'red'
    elif u[17:21] == ['b', 'b', 'b', 'b']:
        return 'blue'
    elif u[21:25] == ['y', 'y', 'y', 'y']:
        return 'yellow'
    else:
        return ''
def reverse(v):
    newv = ''
    vs = v[25].split()
    for i in vs[::-1]:
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
