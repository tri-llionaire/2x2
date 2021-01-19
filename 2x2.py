"""
     2  1 #white
     3  4
6 5 10  9 14 13 18 17 #blue
7 8 11 12 15 16 19 20
    22 21
    23 24 #yellow
"""
import random, time, itertools
import movedictionary
solved = ['0', 'w', 'w', 'w', 'w', 'o', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'y', 'y', 'y', 'y', '']
scrambled = list(solved)
new = []
data_sessions = ''
current_formatted = ''
others_formatted = ''
n = ''
u = 0
w = 0
keeps = ''
x = 0
z = 0
q = 1
g = 1
fromscrambled = []
fromsolved = []
best_five = 0
best_twelve = 0
best_solve = 999.99
worst_solve = 0.0
currentsession = []
todo = []
sol = []
newv = ''
bad = []
moves = ['R', 'R\'', 'R2', 'U', 'U\'', 'U2', 'F', 'F\'', 'F2']
current = list(solved)
def scramble(current, entered_scramble):
    current[25] = entered_scramble
    for x in entered_scramble.split():
        if x == 'R':
            current = movedictionary.move_R(current)
        elif x == 'R\'':
            current = movedictionary.move_Rp(current)
        elif x == 'R2':
            current = movedictionary.move_Rd(current)
        elif x == 'U':
            current = movedictionary.move_U(current)
        elif x == 'U\'':
            current = movedictionary.move_Up(current)
        elif x == 'U2':
            current = movedictionary.move_Ud(current)
        elif x == 'F':
            current = movedictionary.move_F(current)
        elif x == 'F\'':
            current = movedictionary.move_Fp(current)
        elif x == 'F2':
            current = movedictionary.move_Fd(current)
        elif x == 'L':
            current = movedictionary.or_L(current)
        elif x == 'L\'':
            current = movedictionary.or_Lp(current)
        elif x == 'L2':
            current = movedictionary.or_Ld(current)
        elif x == 'D':
            current = movedictionary.or_D(current)
        elif x == 'D\'':
            current = movedictionary.or_Dp(current)
        elif x == 'D2':
            current = movedictionary.or_Dd(current)
        elif x == 'B':
            current = movedictionary.or_B(current)
        elif x == 'B\'':
            current = movedictionary.or_Bp(current)
        elif x == 'B2':
            current = movedictionary.or_Bd(current)
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
def generate():
    last = 'i'
    scramble = ''
    moves = ['R', 'R\'', 'R2', 'U', 'U\'', 'U2', 'F', 'F\'', 'F2']
    for i in 'twelveletter':
        index = random.randint(0, 8)
        while last[0] == moves[index][0]:
            index = random.randint(0, 8)
        scramble = scramble + moves[index] + ' '
        last = moves[index]
    return scramble
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
def guesses(todo, repeating):
    was = ''
    for x in itertools.product(moves, repeat=repeating):
        for i in x:
            if i[0] == was:
                bad.append(' '.join(x))
                break
            was = i[0]
        todo.append(' '.join(x))
        was = ''
    for h in todo[:]:
        if h in bad:
            todo.remove(h)
    return todo
def find(u):
    global side
    side = ''
    if u[1:5] == ['w', 'w', 'w', 'w']:
        side = 'white'
        return True
    elif u[5:9] == ['o', 'o', 'o', 'o']:
        side = 'orange'
        return True
    elif u[9:13] == ['g', 'g', 'g', 'g']:
        side = 'green'
        return True
    elif u[13:17] == ['r', 'r', 'r', 'r']:
        side = 'red'
        return True
    elif u[17:21] == ['b', 'b', 'b', 'b']:
        side = 'blue'
        return True
    elif u[21:25] == ['y', 'y', 'y', 'y']:
        side = 'yellow'
        return True
    else:
        side = ''
        return False
def rot_x(current):
    new = movedictionary.move_R(current)
    new = movedictionary.or_Lp(new)
    return new
def rot_xp(current):
    new = movedictionary.move_Rp(current)
    new = movedictionary.or_L(new)
    return new
def rot_xd(current):
    new = movedictionary.move_Rd(current)
    new = movedictionary.or_Ld(new)
    return new
def rot_y(current):
    new = movedictionary.move_U(current)
    new = movedictionary.or_Dp(new)
    return new
def rot_yp(current):
    new = movedictionary.move_Up(current)
    new = movedictionary.or_D(new)
    return new
def rot_yd(current):
    new = movedictionary.move_Ud(current)
    new = movedictionary.or_Dd(new)
    return new
def rot_z(current):
    new = movedictionary.move_F(current)
    new = movedictionary.or_Bp(new)
    return new
def rot_zp(current):
    new = movedictionary.move_Fp(current)
    new = movedictionary.or_B(new)
    return new
def rot_zd(current):
    new = movedictionary.move_Fd(current)
    new = movedictionary.or_Bd(new)
    return new
print('CUBE(2x2)v3.6')
choice = input('timer, (e)ditor, (c)alculator: ')
if choice == 'c':
    scr = input('enter scramble (l for list, r for random): ')
    if scr == 'l':
        current = input(': ')
    elif scr == 'r':
        top = generate()
        current = scramble(solved, top)
        print(top)
    else:
        current = scramble(solved, scr)
    output(current)
    print('ready to find')
    starting = time.time()
    while q != 0:
        for l in guesses(todo, q):
            fromscrambled.append(scramble(current, l))
            fromsolved.append(scramble(solved, l))
        print('scrambled all at depth {}({})'.format(q, q*2))
        for u in fromscrambled:
            for v in fromsolved:
                if v[25] in sol:
                    break
                if u[25] in sol:
                    break
                if u[:24] == v[:24]:
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
                    nex = u[25] + ' ' + newv
                    if nex not in sol:
                        if remove(nex) == False:
                            print('matched {}({})'.format(nex, len(nex.split())))
                            sol.append(nex)
                if u[:24] == solved[:24]:
                    print('solution', u[25])
                    sol.append(u[25])
                if v[:24] == solved[:24]:
                    print('solution', v[25])
                    sol.append(v[25])
        print('finished checking')
        if not sol:
            print('trying depth {}({})'.format(q+1, (q+1)*2))
        else:
            q = -1
        q += 1
    ending = time.time()
    print('done at {:.2f}s'.format(ending - starting))
elif choice == 'e':
    while True:
        moves = input('enter (r for random): ')
        if moves == 'r':
            keeps = generate()
            state = scramble(current, keeps)
        else:
            keeps = keeps + moves + ' '
            state = scramble(solved, keeps)
        print(state)
        output(state)
        print('( {})'.format(keeps))
else:
    choose = input('(e)nter times or (t)imer: ')
    while True:
        keep = generate()
        scrambled = scramble(solved, keep)
        output(scrambled)
        print('( {})'.format(keep))
        if choose == 'e':
            timed = input('enter time: ')
            timed = '{:.2f}'.format(float(timed))
        else:
            wait = input('start timer')
            start = time.time()
            n = input()
            end = time.time()
            timed = end - start
            timed = '{:.2f}'.format(float(timed))
            print(timed)
        time.sleep(2)
        currentsession.append(timed)
        if float(timed) > worst_solve:
            worst_solve = float(timed)
            print('new worst solve')
        if float(timed) < best_solve:
            best_solve = float(timed)
            print('new best solve')
        w += 1
        if (w % 5) == 0:
            for i in currentsession:
                x += float(i)
            current_five = x/5
            x = 0
            print('new avg 5: {:.2f}'.format(current_five))
            if current_five > best_five:
                print('(also session record for 5)')
                best_five = current_five
        if (w % 12) == 0:
            for i in currentsession[-12:]:
                x += float(i)
            current_five = x/12
            x = 0
            print('new avg 12: {:.2f}'.format(current_twelve))
            if current_twelve > best_twelve:
                print('(also session record for 12)')
                best_twelve = current_twelve
        for i in currentsession:
            x += float(i)
            z += 1.0
        session_avg = x/z
        x = 0
        z = 0
        print('session avg: {:.2f}'.format(session_avg))
        time.sleep(2)
        while g != 0:
            for l in guesses(todo, g):
                fromscrambled.append(scramble(scrambled, l))
            for u in fromscrambled:
                if u[25] in sol:
                    break
                temp = find(u)
                if temp == True:
                    print('solution {} {}'.format(u[25], side))
                    sol.append(u[25])
            if sol:
                g = -1
            g += 1
        g = 1
        print('\n\n\n')
