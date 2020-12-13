# step2
# user input = URLB (+ "'") Q

def push(str, num, dir):
    idx = int(num) * dir % len(str)
    return str[idx:] + str[:idx]


def rotate(cube, dir):  #push default(dir == 1)가 왼쪽 이므로, push() 를 계속 써주기 위해서 시계/반시계 방향으로 적절히 회전시킨 후 push()하고, 원래 상태로 다시 회전시켜준다. 
    newcube = [[]] * 3

    if dir == 1: # 시계 방향 회전
        # for i in range(2):
        #    for j in reversed(range(2)):
        #         newcube[i] += cube[j][i]
        newcube[0] = cube[2][0]+cube[1][0]+cube[0][0]
        newcube[1] = cube[2][1]+cube[1][1]+cube[0][1]
        newcube[2] = cube[2][2]+cube[1][2]+cube[0][2]
    elif dir == -1: #반시계 방향 회전
        # for i in reversed(range(2)):
        #     for j in range(2):
        #         newcube[i] += cube[j][i]
        newcube[0] = cube[0][2]+cube[1][2]+cube[2][2]
        newcube[1] = cube[0][1]+cube[1][1]+cube[2][1]
        newcube[2] = cube[0][0]+cube[1][0]+cube[2][0]

    return newcube


def U(cube, dir): #맨 윗줄 왼쪽으로 한 칸 밀기
    cube[0] = push(cube[0], 1, dir) #맨 윗줄을 한 칸씩 dir(default 왼쪽) 따라서 밀기
    return cube


def B(cube, dir): #맨 아랫줄을 오른쪽으로 한 칸 밀기
    cube[2] = push(cube[2], 1, -dir) #맨 아랫줄을 한 칸씩 dir 반대 방향(왼쪽이 default니까) 따라서 밀기
    return cube

def R(cube, dir): # 가장 오른쪽 줄을 위로 한 칸 밀기 => 반시계 회전 후, 맨 윗줄 왼쪽으로 push, 시계 방향 회전으로 돌려주기
    cube = rotate(cube, -1)
    cube[0] = push(cube[0], 1, dir)
    cube = rotate(cube, 1)
    return cube

def L(cube, dir): #가장 왼쪽 줄을 아래로 한 칸 밀기 => 시계방향 회전 후, 맨 윗줄 왼쪽으로 push, 반시계 방향 회전으로 돌려주기
    cube = rotate(cube, 1)
    cube[0] = push(cube[0], 1, dir)
    cube = rotate(cube, -1)
    return cube


cube = ['RRW', 'GCW', 'GBB']
print('\n'.join(cube) + '\n') #cube모양으로 프린트 찍어주기

x = input('CUBE>')
while x != 'Q':
    i = 0 #user input index default
    
    while i < len(x): # to iterate index from start to the end
        dir = x[i] #각 인덱스마다 돌리는 방향 의미
        if i < len(x) -1: #마지막 이후에는 "'"가 올 수 없어서 
            if x[i + 1] == "'": #이후에 오는 문자가 "'"라면,
                dir += "'" #이전의 문자(알파벳)과 "'"를 한큐에 처리하겠다
                i += 1 #다음 인덱스로 넘어가기
        rdir = "'" not in x or -1 #user input에 "'" 안 들어 있으면, rdir(rotation direction) = 1(시계 방향), "'" 들어 있으면 rdir = -1(반시계 방향)

        if 'U' in dir:
            cube = U(cube,rdir)
        elif 'B' in dir:
            cube = B(cube, rdir)
        elif 'L' in dir:
            cube = L(cube, rdir)
        elif 'R' in dir:
            cube = R(cube, rdir)
        
        print(dir + '\n')
        print('\n'.join(cube) + '\n')
        

        i += 1
    
    x = input('CUBE>') #user input  re-collect

print('\nBye~')