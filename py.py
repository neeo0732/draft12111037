

origin=(input("변환할 정수를 입력하십시오")) # 사용자가 원본 정수 입력
originFlag=(int(input("어떤 진수인지 입력하여 주십시오 (예, 10진수->10)"))) # 사용자가 출발 진수 입력
cnvrt=(int(input("어떤 진수로 변환할지 입력하십시오 (예, 2진법->2)"))) # 사용자가 도착 진수 입력
fin='' # 변환된 진수 저장소

if originFlag==10: # 출발 진수가 10진수
    if cnvrt==2: #2진수 변환
       fin=(bin(int(origin))[2:])
    elif cnvrt==8: #8진수 변환
       fin=(oct(int(origin))[2:])
    elif cnvrt==10: #10진수 변환
       print("And Don't you know how it sweet it tastes?") # NewJeans - How Sweet
       fin=origin
    elif cnvrt==12: #12진수 변환
         def duodemic(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
         fin=(duodemic(int(origin), 12))
    elif cnvrt==16: #16진수 변환
        fin=(hex(int(origin))[2:])
    elif cnvrt==60: #60진법 변환
        def sexage(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
             fin=(sexage(int(origin), 60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")
print(fin)