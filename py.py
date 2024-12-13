
origin=(input("변환할 정수를 입력하십시오")) # 사용자가 원본 정수 입력
originFlag=(int(input("어떤 진수인지 입력하여 주십시오 (예, 10진수->10)"))) # 사용자가 출발 진수 입력
cnvrt=(int(input("어떤 진수로 변환할지 입력하십시오 (예, 2진법->2)"))) # 사용자가 도착 진수 입력
fin='' # 변환된 진수 저장소

if originFlag==10: # 출발 진수가 10진수
    if cnvrt==2: # 2진수 변환
       fin=(bin(int(origin))[2:])
    elif cnvrt==8: # 8진수 변환
       fin=(oct(int(origin))[2:])
    elif cnvrt==10: # 10진수 변환
       print("And Don't you know how it sweet it tastes?") # NewJeans - How Sweet
       fin=origin
    elif cnvrt==12: # 12진수 변환
         def duodemic(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
         fin=(duodemic(int(origin), 12))
    elif cnvrt==16: # 16진수 변환
        fin=(hex(int(origin))[2:])
    elif cnvrt==60: # 60진법 변환
        def sexage(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
             fin=(sexage(int(origin), 60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==2: # 출발 진수가 2진수
    def BinarySet(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
             fin=(BinarySet(int(origin), 60))
    if cnvrt==2: # 2진수 변환
       print("처음으로 나는 죽음을 맛보았다. 죽음은 쓴맛이었다. 왜냐하면 그것은 탄생이니까, 두려운 새 삶에 대한 불안과 걱정이니까.") # 데미안 - 헤르만 헤세
       fin=origin
    elif cnvrt==8: # 8진수 변환
       fin=(BinarySet(int(origin,2),8))
    elif cnvrt==10: # 10진수 변환
       fin=int(origin,2)
    elif cnvrt==12: # 12진수 변환
        fin=(BinarySet(int(origin,2),12))
    elif cnvrt==16: # 16진수 변환
        fin=(BinarySet(int(origin,2),16))
    elif cnvrt==60: # 60진법 변환
        fin=(BinarySet(int(origin,2),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")


if originFlag==8: # 출발 진수가 8진수
    def OctaSet(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
             fin=(OctaSet(int(origin), 60))
    if cnvrt==2: # 2진수 변환
       fin=(OctaSet(int(origin,8),2))
    elif cnvrt==8: # 8진수 변환
       print("lorem ipsum은, 디자인, 폰트와 같은 조형물을 테스트하는 데 사용되어지는 더미 텍스트입니다.") # Lorem Ipsum
       fin=origin
    elif cnvrt==10: # 10진수 변환
       fin=(OctaSet(int(origin,8),10))
    elif cnvrt==12: # 12진수 변환
        fin=(OctaSet(int(origin,8),12))
    elif cnvrt==16: # 16진수 변환
        fin=(OctaSet(int(origin,8),16))
    elif cnvrt==60: # 60진법 변환
        fin=(OctaSet(int(origin,8),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==12: # 출발 진수가 12진수
    def DuoSet(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
             fin=(DuoSet(int(origin), 60))
    if cnvrt==2: # 2진수 변환
       fin=(DuoSet(int(origin,12),2))
    elif cnvrt==8: # 8진수 변환
       fin=(DuoSet(int(origin,12),8))
    elif cnvrt==10: # 10진수 변환
       fin=(DuoSet(int(origin,12),10))
    elif cnvrt==12: # 12진수 변환
        print("lorem ipsum은, 디자인, 폰트와 같은 조형물을 테스트하는 데 사용되어지는 더미 텍스트입니다.") # Lorem Ipsum
        fin=origin
    elif cnvrt==16: # 16진수 변환
        fin=(DuoSet(int(origin,12),16))
    elif cnvrt==60: # 60진법 변환
        fin=(DuoSet(int(origin,12),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==16: # 출발 진수가 16진수
    def HexaSet(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
             fin=(HexaSet(int(origin), 60))
    if cnvrt==2: # 2진수 변환
       fin=(HexaSet(int(origin,16),2))
    elif cnvrt==8: # 8진수 변환
       fin=(HexaSet(int(origin,16),8))
    elif cnvrt==10: # 10진수 변환
       fin=(HexaSet(int(origin,16),10))
    elif cnvrt==12: # 12진수 변환
        fin=(HexaSet(int(origin,16),12))
    elif cnvrt==16: # 16진수 변환
        print("lorem ipsum은, 디자인, 폰트와 같은 조형물을 테스트하는 데 사용되어지는 더미 텍스트입니다.") # Lorem Ipsum
        fin=origin
    elif cnvrt==60: # 60진법 변환
        fin=(HexaSet(int(origin,16),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==60: # 출발 진수가 60진수
    def SexaSet(q, w):
             revBase=''
             while q>0:
              q,mod=divmod(q, w)
              revBase+=str(mod)
              return revBase[::-1]
             fin=(SexaSet(int(origin), 60))
    if cnvrt==2: # 2진수 변환
       fin=(SexaSet(int(origin,60),2))
    elif cnvrt==8: # 8진수 변환
       fin=(SexaSet(int(origin,60),8))
    elif cnvrt==10: # 10진수 변환
       fin=(SexaSet(int(origin,60),10))
    elif cnvrt==12: # 12진수 변환
        fin=(SexaSet(int(origin,60),12))
    elif cnvrt==16: # 16진수 변환
        print("lorem ipsum은, 디자인, 폰트와 같은 조형물을 테스트하는 데 사용되어지는 더미 텍스트입니다.") # Lorem Ipsum
        fin=origin
    elif cnvrt==60: # 60진법 변환
        fin=(SexaSet(int(origin,60),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")


else:
    print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

print(fin) # 변환값 출력
