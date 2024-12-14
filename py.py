
origin=(input("변환할 정수를 입력하십시오: ")) # 사용자가 원본 정수 입력
originFlag=(int(input("어떤 진수인지 입력하여 주십시오 (예, 10진법->10): "))) # 사용자가 출발 진법 입력
cnvrt=(int(input("어떤 진법으로 변환할지 입력하십시오 (예, 2진법->2): "))) # 사용자가 도착 진법 입력
fin='' # 변환된 결과값 저장소

def RadixCalc(q,w): # 사용자정의함수 `RadixCalc` 정의
    revBase=''
    while q>0:
         q,mod=divmod(q,w)
         revBase+=str(mod)
         return revBase[::-1]

if originFlag==10: # 출발 진수 10진법
    if cnvrt==2: # 2진법 변환
       fin=(bin(int(origin))[2:])
    elif cnvrt==8: # 8진법 변환
       fin=(oct(int(origin))[2:])
    elif cnvrt==10: # 10진법 변환
       print("연산에 실패함: 출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin), 12))
    elif cnvrt==16: # 16진법 변환
        fin=(hex(int(origin))[2:])
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin), 60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==2: # 출발 진수가 2진법
    if cnvrt==2: # 2진법 변환
       print("연산에 실패함: 출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,2),8))
    elif cnvrt==10: # 10진법 변환
       fin=int(origin,2)
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,2),12))
    elif cnvrt==16: # 16진법 변환
        fin=(RadixCalc(int(origin,2),16))
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,2),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")


if originFlag==8: # 출발 진수가 8진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,8),2))
    elif cnvrt==8: # 8진법 변환
       print("연산에 실패함: 출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,8),10))
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,8),12))
    elif cnvrt==16: # 16진법 변환
        fin=(RadixCalc(int(origin,8),16))
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,8),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==12: # 출발 진수가 12진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,12),2))
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,12),8))
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,12),10))
    elif cnvrt==12: # 12진법 변환
       print("연산에 실패함: 출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==16: # 16진법 변환
        fin=(RadixCalc(int(origin,12),16))
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,12),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==16: # 출발 진수가 16진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,16),2))
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,16),8))
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,16),10))
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,16),12))
    elif cnvrt==16: # 16진법 변환
        print("연산에 실패함: 출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
        fin=origin
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,16),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

if originFlag==60: # 출발 진수가 60진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,60),2))
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,60),8))
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,60),10))
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,60),12))
    elif cnvrt==16: # 16진법 변환
        print("연산에 실패함: 출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
        fin=origin
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,60),60))
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")

print(fin) # 변환값 출력
