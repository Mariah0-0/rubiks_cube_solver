def R(c):
    temp21 = c['21']
    temp62 = c['62']
    temp42 = c['42']
    temp81 = c['81']
    c['21'] = c['40']
    c['62'] = c['20']
    c['42'] = c['80']
    c['81'] = c['60']
    c['40'] = temp81
    c['20'] = temp42
    c['80'] = temp62
    c['60'] = temp21
    temp22 = c['22']
    temp82 = c['82']
    c['22'] = c['41']
    c['82'] = c['61']
    c['41'] = temp82
    c['61'] = temp22
    
def Rp(c):
    temp21 = c['21']
    temp62 = c['62']
    temp42 = c['42']
    temp81 = c['81']
    c['21'] = c['60']
    c['62'] = c['80']
    c['42'] = c['20']
    c['81'] = c['40']
    c['40'] = temp21
    c['20'] = temp62
    c['80'] = temp42
    c['60'] = temp81
    temp22 = c['22']
    temp82 = c['82']
    c['22'] = c['61']
    c['82'] = c['41']
    c['41'] = temp22
    c['61'] = temp82

def R2(c):
    temp20 = c['20']
    temp40 = c['40']
    temp42 = c['42']
    temp81 = c['81']
    c['20'] = c['80']
    c['40'] = c['60']
    c['42'] = c['62']
    c['81'] = c['21']
    c['80'] = temp20
    c['60'] = temp40
    c['62'] = temp42
    c['21'] = temp81
    temp22 = c['22']
    temp41 = c['41']
    c['22'] = c['82']
    c['41'] = c['61']
    c['82'] = temp22
    c['61'] = temp41

def U(c):
    temp10 = c['10']
    temp20 = c['20']
    temp50 = c['50']
    temp60 = c['60']
    c['10'] = c['22']
    c['20'] = c['61']
    c['50'] = c['11']
    c['60'] = c['52']
    c['22'] = temp60
    c['61'] = temp50
    c['11'] = temp20
    c['52'] = temp10
    temp12 = c['12']
    temp62 = c['62']
    c['12'] = c['21']
    c['62'] = c['51']
    c['21'] = temp62
    c['51'] = temp12

def Up(c):
    temp10 = c['10']
    temp20 = c['20']
    temp50 = c['50']
    temp60 = c['60']
    c['10'] = c['52']
    c['20'] = c['11']
    c['50'] = c['61']
    c['60'] = c['22']
    c['52'] = temp60
    c['11'] = temp50
    c['61'] = temp20
    c['22'] = temp10
    temp12 = c['12']
    temp62 = c['62']
    c['12'] = c['51']
    c['62'] = c['21']
    c['21'] = temp12
    c['51'] = temp62

def U2(c):
    temp10 = c['10']
    temp20 = c['20']
    temp22 = c['22']
    temp61 = c['61']
    c['10'] = c['60']
    c['20'] = c['50']
    c['22'] = c['52']
    c['61'] = c['11']
    c['60'] = temp10
    c['50'] = temp20
    c['52'] = temp22
    c['11'] = temp61
    temp12 = c['12']
    temp21 = c['21']
    c['12'] = c['62']
    c['21'] = c['51']
    c['62'] = temp12
    c['51'] = temp21

def F(c):
    temp12 = c['12']
    temp21 = c['21']
    temp31 = c['31']
    temp42 = c['42']
    c['12'] = c['32']
    c['21'] = c['11']
    c['31'] = c['41']
    c['42'] = c['22']
    c['32'] = temp42
    c['11'] = temp31
    c['41'] = temp21
    c['22'] = temp12
    temp10 = c['10']
    temp40 = c['40']
    c['10'] = c['30']
    c['40'] = c['20']
    c['30'] = temp40
    c['20'] = temp10

def Fp(c):
    temp12 = c['12']
    temp21 = c['21']
    temp31 = c['31']
    temp42 = c['42']
    c['12'] = c['22']
    c['21'] = c['41']
    c['31'] = c['11']
    c['42'] = c['32']
    c['22'] = temp42
    c['41'] = temp31
    c['11'] = temp21
    c['32'] = temp12
    temp10 = c['10']
    temp40 = c['40']
    c['10'] = c['20']
    c['40'] = c['30']
    c['20'] = temp40
    c['30'] = temp10

def F2(c):
    temp12 = c['12']
    temp21 = c['21']
    temp22 = c['22']
    temp41 = c['41']
    c['12'] = c['42']
    c['21'] = c['31']
    c['22'] = c['32']
    c['41'] = c['11']
    c['42'] = temp12
    c['31'] = temp21
    c['32'] = temp22
    c['11'] = temp41
    temp10 = c['10']
    temp20 = c['20']
    c['10'] = c['40']
    c['20'] = c['30']
    c['40'] = temp10
    c['30'] = temp20

def ver1(c,cs,ps,j):
    if len(c)!=1 or c not in 'wyrobg' or cs.count(c)==4:
        return False
    pieces1 = [['w','b','r'],['w','r','g'],['w','o','b'],['w','g','o'],
               ['y','r','b'],['y','g','r'],['y','b','o'],['y','o','g']]
    oppc = {'w':'y', 'y':'w', 'r':'o', 'o':'r', 'b':'g', 'g':'b'}
    if ps[j] in ['31','42','70','80','51','62','12','21']:
        for i in range(len(cs)):
            if ps[j][0]==ps[i][0]:
                if cs[i]==c or cs[i]==oppc[c]:
                    return False
                break
    list1 = []           
    if j>15:
        for i in range(len(cs)):
            if ps[i][0]==ps[j][0]:
                list1.append(int(ps[i][1]))
        if list1!=[0,1] and list1!=[1,2] and list1!=[2,0]:
            list1.reverse()
        for i in pieces1:
            for k in range(3):
                if cs[ps.index(ps[j][0]+str(list1[0]))]==i[k]:
                    if cs[ps.index(ps[j][0]+str(list1[1]))]==i[(k+1)%3]:
                        rcolour = i[(k+2)%3]
        if c!=rcolour:
            return False
    return True

def ver2(c):
    sumor = 0
    for i in c:
        if c[i]=='w' or c[i]=='y':
            sumor += int(i[1])
    if sumor%3!=0:
        return False
    return True

def inputcase(case):
    intro_ascii ='''\t\t          +----+----+
    \t\t          | 13 | 14 |
    \t\t          | 15 | 16 |
    \t\t|----+----+----+----+----+----|
    \t\t| 17 | 18 |  1 |  2 | 21 | 22 |
    \t\t| 19 | 20 |  3 |  4 | 23 | 24 |
    \t\t|----+----+----+----+----+----|
    \t\t          |  5 |  6 |
    \t\t          |  7 |  8 |
    \t\t          +----+----+
    \t\t          |  9 | 10 |
    \t\t          | 11 | 12 |
    \t\t          +----+----+'''
    positions = ['10', '20', '30', '40', '31', '42', '72', '81', '70', '80', '50', '60', '51', '62', '12', '21', '52', '11', '71', '32', '22', '61', '41', '82']
    print('\n\n'+'-'*20+'2x2x2 RUBIK\'S CUBE SOLVER'+'-'*20+'\n\n')
    print(intro_ascii)
    print('\n\nEnter the colour of the piece beside the position given, referring to the picture.\n(w/y/r/o/b/g)\n')
    while True:
        colours = []
        for i in range(24):
            while True:
                colour = input(str(i+1)+': ').lower()
                if ver1(colour,colours,positions,i):
                    colours.append(colour)
                    case[positions[i]] = colour
                    break
                print('\nInvalid value\n')
        if ver2(case):
            break
        print('\nInvalid case\n')

def solve(case,solvedc,solution,num):
    moves = [R, Rp, R2, U, Up, U2, F, Fp, F2]
    oppmove = {R:Rp, Rp:R, R2:R2, U:Up, Up:U, U2:U2, F:Fp, Fp:F, F2:F2}
    grps = [[R, Rp, R2], [U, Up, U2], [F, Fp, F2]]
    if case==solvedc:
        return
    if solution!=[] and len(solution)==num:
        last = [F2,U2,F2,U2,F2,U2,F2,U2,F2,U2,F2][:len(solution)]
        if solution==last:
            num+=1
            for i in solution[::-1]:
                oppmove[i](case)
            solution.clear()
    if len(solution)==num or num==12:
        return
    for m in moves:
        if solution!=[]:
            for g in grps:
                if solution[-1] in g:
                    grp = g
            if m in grp:
                continue
        solution.append(m)
        m(case)
        solve(case,solvedc,solution,num)
        if case==solvedc:
            return
        if num==12:
            return
        if solution!=[]:
            solution.pop()
            oppmove[m](case)
    return
        
def main():
    case = {}
    solution = []
    grp = []
    num = 1
    oppc = {'w':'y', 'y':'w', 'r':'o', 'o':'r', 'b':'g', 'g':'b'}
    inputcase(case)
    solvedc = {'10':oppc[case['70']], '20':oppc[case['70']], '30':oppc[case['70']], '40':oppc[case['70']],
               '31':case['72'], '42':case['72'], '72':case['72'], '81':case['72'],
               '70':case['70'], '80':case['70'], '50':case['70'], '60':case['70'],
               '51':oppc[case['72']], '62':oppc[case['72']], '12':oppc[case['72']], '21':oppc[case['72']],
               '52':case['71'], '11':case['71'], '71':case['71'], '32':case['71'],
               '22':oppc[case['71']], '61':oppc[case['71']], '41':oppc[case['71']], '82':oppc[case['71']]}
    solve(case,solvedc,solution,num)
    if solution==[]:
        print('\nThe cube is already solved!')
        print()
    else:
        print('\n\nSolution:\n')
        for i in solution:
            print(i.__name__, end=' ')
        print('\n')

main()
