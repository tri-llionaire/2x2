import time, movedictionary
solved = ['0', 'w', 'w', 'w', 'w', 'o', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'r', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'y', 'y', 'y', 'y', '']
scrambled = list(solved)
q = 1
print('CUBE(2x2)v4.2')
choice = input('timer, (e)ditor, (c)alculator: ')
if choice == 'c':
    sol = []
    scr = input('enter scramble (l for list, r for random): ')
    if scr == 'l':
        current = input(': ')
    elif scr == 'r':
        top = movedictionary.generate()
        current = movedictionary.scramble(solved, top)
        print(top)
    else:
        current = movedictionary.scramble(solved, scr)
    movedictionary.output(current)
    print('ready to find')
    starting = time.time()
    while q != 0:
        fromscrambled = []; fromsolved = []; sol = 0
        print('trying depth {}({})'.format(q, q*2))
        finded = movedictionary.guesses(q)
        print('generated all guesses for depth {}({}) at {:.2f}s'.format(q, q*2, time.time() - starting))
        for l in finded:
            fromscrambled.append(movedictionary.scramble(current, l))
            fromsolved.append(movedictionary.scramble(solved, l))
        print('scrambled all at depth {}({}) at {:.2f}s'.format(q, q*2, time.time() - starting))
        for u in fromscrambled:
            for v in fromsolved:
                if u[:24] == v[:24]:
                    nex = u[25] + ' ' + movedictionary.reverse(v)
                    print('matched {}({}) at {:.2f}s'.format(nex, len(nex.split()), time.time() - starting))
                    sol = 1
        print('finished checking')
        if sol == 1:
            q = -1
        q += 1
    print('done at {:.2f}s'.format(time.time() - starting))
elif choice == 'e':
    while True:
        emoves = input('enter (r for random): ')
        if emoves == 'r':
            keeps = movedictionary.generate()
            state = movedictionary.scramble(current, keeps)
        else:
            keeps = keeps + emoves + ' '
            state = movedictionary.scramble(solved, keeps)
        print(state)
        movedictionary.output(state)
        print('( {})'.format(keeps))
else:
    choose = input('(e)nter times or timer: ')
    w = 0; x = 0; z = 0; best_five = 0; best_twelve = 0; best_solve = 999.99; worst_solve = 0.0; currentsession = []
    while True:
        keep = movedictionary.generate()
        scrambled = movedictionary.scramble(solved, keep)
        movedictionary.output(scrambled)
        print('( {})'.format(keep))
        if choose == 'e':
            timed = input('enter time: ')
            timed = '{:.2f}'.format(float(timed))
        else:
            wait = input('start timer')
            start = time.time()
            waiting = input()
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
        x = 0; z = 0; fromscrambled = []; sol = []
        print('session avg: {:.2f}'.format(session_avg))
        time.sleep(2)
        while q != 0:
            for l in movedictionary.guesses(q):
                fromscrambled.append(movedictionary.scramble(scrambled, l))
            for u in fromscrambled:
                if u[25] in sol:
                    break
                temp = movedictionary.find(u)
                if temp != '':
                    print('solution {} {}'.format(u[25], temp))
                    sol.append(u[25])
            if sol:
                q = -1
            q += 1
        q = 1
        print('\n\n\n')
