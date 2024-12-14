
origin=(input("변환할 정수를 입력하십시오: ")) # 사용자가 원본 정수 입력
originFlag=(int(input("어떤 진수인지 입력하여 주십시오 (2/8/10/12/16/60) (예, 10진법->10): "))) # 사용자가 출발 진법 입력
cnvrt=(int(input("어떤 진법으로 변환할지 입력하십시오 (2/8/10/12/16/60) (예, 2진법->2): "))) # 사용자가 도착 진법 입력
fin='' # 변환된 결과값 저장소

def RadixCalc(q,w): # 사용자정의함수 `RadixCalc` 정의 / Python 내부에서 지원하지 않는 진법 변환의 경우 나눗셈/반복문/자릿수 뒤집기를 사용해 처리해야 함 / q=10진수 w=진법
    revBase='' # 자릿수를 역순으로 뒤집기 전 결과값 저장소
    while q>0: # 나눌 수 0 이상일 때 반복 (나눗셈 필요조건)
         q,mod=divmod(q,w) # 나눗셈 -> 몫 q / 나머지 mod 저장
         revBase+=str(mod) # 자릿수 뒤집기 위해 정수를 문자열로 변환
         return revBase[::-1] # 출력할 함수의 결괏값 정의 (자릿수 뒤집기)

if originFlag==10: # 출발 진수 10진법
    if cnvrt==2: # 2진법 변환
       fin=(bin(int(origin))[2:]) # Python 내장 bin 함수 사용 / [2:] -> 진법 표시 지우기
    elif cnvrt==8: # 8진법 변환
       fin=(oct(int(origin))[2:]) # Python 내장 oct 함수 사용 / [2:] -> 진법 표시 지우기
    elif cnvrt==10: # 10진법 변환
       print("출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin),12)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==16: # 16진법 변환
        fin=(hex(int(origin))[2:]) # Python 내장 hex 함수 사용 / [2:] -> 진법 표시 지우기
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin),60)) # 사용자 함수 RadixCalc 사용
    else:
        print("지원하지 않는 도착 진법이거나 내부 오류가 발생했습니다.")

elif originFlag==2: # 출발 진수가 2진법
    if cnvrt==2: # 2진법 변환
       print("출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,2),8)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==10: # 10진법 변환
       fin=int(origin,2) # Python 내장 int 함수의 10진법 변환 사용
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,2),12)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==16: # 16진법 변환
        fin=(RadixCalc(int(origin,2),16)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,2),60)) # 사용자 함수 RadixCalc 사용
    else:
        print("지원하지 않는 도착 진법이거나 내부 오류가 발생했습니다.")


elif originFlag==8: # 출발 진수가 8진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,8),2)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==8: # 8진법 변환
       print("출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,8),10)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,8),12)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==16: # 16진법 변환
        fin=(RadixCalc(int(origin,8),16)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,8),60)) # 사용자 함수 RadixCalc 사용
    else:
        print("지원하지 않는 도착 진법이거나 내부 오류가 발생했습니다.")

elif originFlag==12: # 출발 진수가 12진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,12),2)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,12),8)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,12),10)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==12: # 12진법 변환
       print("출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
       fin=origin
    elif cnvrt==16: # 16진법 변환
        fin=(RadixCalc(int(origin,12),16)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,12),60)) # 사용자 함수 RadixCalc 사용
    else:
        print("지원하지 않는 도착 진법이거나 내부 오류가 발생했습니다.")

elif originFlag==16: # 출발 진수가 16진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,16),2)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,16),8)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,16),10)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,16),12)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==16: # 16진법 변환
        print("출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
        fin=origin
    elif cnvrt==60: # 60진법 변환
        fin=(RadixCalc(int(origin,16),60)) # 사용자 함수 RadixCalc 사용
    else:
        print("지원하지 않는 도착 진법이거나 내부 오류가 발생했습니다.")

elif originFlag==60: # 출발 진수가 60진법
    if cnvrt==2: # 2진법 변환
       fin=(RadixCalc(int(origin,60),2)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==8: # 8진법 변환
       fin=(RadixCalc(int(origin,60),8)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==10: # 10진법 변환
       fin=(RadixCalc(int(origin,60),10)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==12: # 12진법 변환
        fin=(RadixCalc(int(origin,60),12)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==16: # 16진법 변환
        fin=(RadixCalc(int(origin,60),16)) # 사용자 함수 RadixCalc 사용
    elif cnvrt==60: # 60진법 변환
        print("출발 진법과 도착 진법이 동일합니다!") # 출발-도착 진법 동일
        fin=origin
    else:
        print("지원하지 않는 도착 진법이거나 내부 오류가 발생했습니다.")

else:
    print("지원하지 않는 출발 진법이거나 내부 오류가 발생했습니다.")

print(fin) # 변환값 출력
