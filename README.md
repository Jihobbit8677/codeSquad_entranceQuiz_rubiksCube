# codeSquad_entranceQuiz_rubiksCube
 implementing Rubik's cube

step-3)

각 면이 회전할 떄(user input 별로)
다른 면들은 어떻게 영향을 받나 행/열 넘버 조심하면서, 각 면마다 행인지 열인지 직접 따져준다(#1,2의 push() rotate() 적절히 이용해서 맨 윗줄에 정렬 후 원상태로 되돌려주기)

user input에서 "'"와 숫자를 이전 인덱스 dir과 묶어서 생각한다.

구동 횟수(count)를 세고,  user input 시작과 끝 시간의 차이로 실행 시간을 측정한다
