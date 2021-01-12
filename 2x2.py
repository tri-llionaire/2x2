"""
     2  1 #white
     3  4
6 5 10  9 14 13 18 17 #blue
7 8 11 12 15 16 19 20
    22 21
    23 24 #yellow
"""
import random, time, itertools
solved = ['0', 'w', 'w', 'w', 'w', 'o', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'y', 'y', 'y', 'y']
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
best_five = 0
best_twelve = 0
best_solve = 999.99
worst_solve = 0.0
currentsession = []
todo = []
was = ''
bad = []
moves = ['R', 'R\'', 'R2', 'U', 'U\'', 'U2', 'F', 'F\'', 'F2']
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
def move_R2(current):
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
def move_U2(current):
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
def move_F2(current):
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
def scramble(current, entered_scramble):
    for x in entered_scramble.split():
        if x == 'R':
            current = move_R(current)
        elif x == 'R\'':
            current = move_Rp(current)
        elif x == 'R2':
            current = move_R2(current)
        elif x == 'U':
            current = move_U(current)
        elif x == 'U\'':
            current = move_Up(current)
        elif x == 'U2':
            current = move_U2(current)
        elif x == 'F':
            current = move_F(current)
        elif x == 'F\'':
            current = move_Fp(current)
        elif x == 'F2':
            current = move_F2(current)
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
'''
3,674,160
PRODUCT:
len1=9
len2=81
len3=729
len4=6,5761
len5=59,049
len6=531,441
PERMUTATIONS:
len1=9
len2=72
len3=504
len4=3,024
len5=15,120
len6=60,480
MODIFIED PRODUCT:
len1=9
len2=54
len3=324
len4=1,944
len5=11,664
len6=
'''
print('CUBE(2x2)v2.2')
choice = input('timer, (e)ditor, (c)alculator: ')
if choice == 'c':
    while True:
        q = input('depth: ')
        starting = time.time()
        for x in itertools.product(moves, repeat=int(q)):
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
        ending = time.time()
        print(todo, len(todo), '{:.2f}s'.format(ending - starting))
        todo = []
        bad = []
        was = ''
elif choice == 'e':
    while True:
        moves = input(': ')
        if moves == 'r':
            state = solved
            keeps = ''
        else:
            keeps = keeps + moves + ' - '
            state = scramble(solved, keeps)
        output(state)
        print('( {})'.format(keeps))
else:
    while True:
        keep = generate()
        scrambled = scramble(solved, keep)
        output(scrambled)
        print('( {})'.format(keep))
        wait = input('start timer')
        start = time.time()
        n = input()
        end = time.time()
        timed = end - start
        timed = '{:.2f}'.format(timed)
        print(timed)
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
        print('session avg: {:.2f}\n\n\n'.format(session_avg))
