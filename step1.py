# step1
str,num,dir = input('').split(' ') # input으로 받아온 것을 스페이스 기준으로 split해서 list 요소들 각각 변수에 할당
dir = dir.lower() == 'l' or -1  #+-1 부호로 자르는 index 위치 정하기(ternary)
 
idx = int(num) * dir % len(str) 
print(str[idx:] + str[:idx])