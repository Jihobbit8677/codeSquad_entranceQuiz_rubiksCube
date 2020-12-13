#step3 

def push(str, num, dir):
    idx = int(num) * dir % len(str)
    return str[idx:] + str[:idx]


def rotate(cube, dir):
    newcube = [[]] * 3
    if dir == 1:
        newcube[0] = cube[2][0] + cube[1][0] + cube[0][0]
        newcube[1] = cube[2][1] + cube[1][1] + cube[0][1]
        newcube[2] = cube[2][2] + cube[1][2] + cube[0][2]
    elif dir == -1:
        newcube[0] = cube[0][2]+cube[1][2]+cube[2][2]
        newcube[1] = cube[0][1]+cube[1][1]+cube[2][1]
        newcube[2] = cube[0][0]+cube[1][0]+cube[2][0]
    return newcube

# {face-index : {front : 0}, {up : 1}, {right : 2}, {down : 3}, {left : 4}, {back : 5}}

def F(cube, rdir): #  앞면 시계방향 => 1,2,3,4면 마지막 행 오른쪽(default 방향 반대 방향)으로 push()
    cube[0] = rotate(cube[0], rdir) #앞 면 시계방향 회전
    D = [cube[1][-1], cube[2][-1], cube[2][-1], cube[4][-1]] 
    cube[1][-1], cube[2][-1], cube[3][-1], cube[4][-1] = push(D, 1, -rdir) #한 행 으로 정렬시킨 후 push해서 대응 시킨다
    return cube


def B(cube, rdir): # 뒷면 시계방향 => 1,2,3,4면 왼쪽으로 push()
    cube[5] = rotate(cube[5], rdir) 
    D = [cube[1][0], cube[2][0], cube[3][0], cube[4][0]]
    cube[1][0], cube[2][0], cube[3][0], cube[4][0] = push(D, 1, rdir)
    return cube


def U(cube, rdir): #윗면 시계방향 => 0, 2, 4, 5면 (행/열 넘버 가로/세로 조심!) push()
    cube[1] = rotate(cube[1],rdir)
    cube[2] = rotate(cube[2],1)
    cube[4] = rotate(cube[4],-1)
    cube[5] = rotate(rotate(cube[5],1),1)
    #push()할 행들 맨 윗줄에 정렬

    D = [cube[0][0],cube[2][0],cube[5][0],cube[4][0]]
    cube[0][0], cube[2][0], cube[5][0], cube[4][0] = push(D,1,rdir)
    
    cube[2] = rotate(cube[2],-1)
    cube[4] = rotate(cube[4],1)
    cube[5] = rotate(rotate(cube[5],1),1)
    #맨 윗줄에 정렬 해 놓았던 과정 다시 원상태로 돌려주기
    return cube

def D(cube, rdir): #아래면 시계방향 => 0, 2, 4, 5 면(행/열 넘버 가로/세로 조심!) 회전
    cube[3] = rotate(cube[3], rdir)
    cube[4] = rotate(cube[4], 1)
    cube[2] = rotate(cube[2], -1)
    cube[0] = rotate(rotate(cube[0], 1) ,1)

    D = [cube[5][0],cube[4][0],cube[0][0],cube[2][0]]
    cube[5][0], cube[4][0], cube[0][0], cube[2][0] = push(D, 1, -rdir)

    cube[4] = rotate(cube[4],-1)
    cube[2] = rotate(cube[2],1)
    cube[0] = rotate(rotate(cube[0],1),1)
    return cube


def L(cube, ridr): # 왼쪽면 시계 방향 => 0, 1, 3, 5면 영향(행/열 넘버 가로/세로 조심!) 회전
    cube[4] = rotate(cube[4], rdir)
    cube[0] = rotate(cube[0],1)
    cube[1] = rotate(cube[1],1)
    cube[5] = rotate(cube[5],1)
    cube[3] = rotate(cube[3],-1)

    D = [cube[5][0],cube[1][0],cube[0][0],cube[3][0]]
    cube[5][0], cube[1][0], cube[0][0], cube[3][0] = push(D, 1, -rdir)
    
    cube[0] = rotate(cube[0],-1)
    cube[1] = rotate(cube[1],-1)
    cube[5] = rotate(cube[5],-1)
    cube[3] = rotate(cube[3],1)
    return cube


def R(cube, rdir): #오른쪽 면 시계방향 => 0, 1, 3, 5면 영향(행/열 넘버 가로/세로 조심!) 회전
    cube[2] = rotate(cube[2], rdir)
    cube[0] = rotate(cube[0], -1)
    cube[1] = rotate(cube[1], -1)
    cube[5] = rotate(cube[5], -1)
    cube[3] = rotate(cube[3], 1)

    D = [cube[5][0], cube[1][0], cube[0][0], cube[3][0]]
    cube[5][0], cube[1][0], cube[0][0], cube[3][0] = push(D,1, rdir)

    cube[0] = rotate(cube[0],1)
    cube[1] = rotate(cube[1],1)
    cube[5] = rotate(cube[5],1)
    cube[3] = rotate(cube[3],-1)
    return cube



def all(cube, dir): 
    rdir = "'" not in dir or -1 #dir에 ' 포함 되어 있으면 1(시계 방향), 포함 안 되어 있으면 -1(반 시계 방향)
    if "F" in dir:
        cube = F(cube, rdir)
    elif "B" in dir:
        cube = B(cube, rdir)
    elif "U" in dir:
        cube = U(cube, rdir)
    elif "D" in dir:
        cube = D(cube, rdir)
    elif "L" in dir:
        cube = L(cube, rdir)
    elif "R" in dir:
        cube = R(cube, rdir)

    return cube

def print_cube(cube):
    print('\n'.join(cube[5]) + '\n') #join() 써서 행별로 줄 바꿔주기
    for i in range(3):
        print('\t'.join([cube[1][i], cube[2][i], cube[3][i], cube[4][i]])) #큐브 행별로 프린트 찍기
    print('\n' + '\n'.join(cube[0]) + '\n')

cube = [['RRR','RRR','RRR'], ['WWW','WWW','WWW'], ['OOO','OOO','OOO'], ['GGG','GGG','GGG'], ['YYY','YYY','YYY'], ['BBB','BBB','BBB']]
print_cube(cube)


import time
x = input ('CUBE>')
fdir = '' #former direction temporary variable 저장
start = time.time()
count = 0 #count default
while x != "Q":
    i = 0 #index default value
    while i < len(x): #아래부터 #2와 원리 동일 "'" 포함 되어 있으면 한 큐에 dir로 묶어서 처리
        dir = x[i]
        if i < len(x)-1:
            if x[i+1] == "'":
                dir += "'"
                i += 1
        if dir.isdigit(): #알파벳 이후 숫자는 앞의 func (그 숫자 -1)만큼 반복
            n = int(dir) - 1
            dir = fdir  #for문에서 반복 시키기 위해서 temp var 저장
            
            for _ in range(n):
                count += 1
                cube = all(cube, dir)
                print(dir + '\n')
                print_cube(cube)
        else:
            count += 1
            cube =all(cube,dir)
            print(dir+'\n')
            print_cube(cube)
        fdir = dir
        i += 1
    x = input('CUBE>')
 
print('경과시간 : ', round(time.time() - start, 2))
print(count)
print('이용해주셔서 감사합니다. 뚜뚜뚜.')
