

origin=(input("변환할 정수를 입력하십시오")) # USER_INPUT_VAL
originFlag=(int(input("어떤 진수인지 입력하여 주십시오 (예, 10진법->10)"))) # ORIGIN_VAL_EVAL
cnvrt=(int(input("어떤 진수로 변환할지 입력하십시오 (예, 2진법->2)"))) # origin TO
fin=() # CONVERTED_VAL

if originFlag==10: # 출발 진수가 10진수
    if cnvrt==2: #2진수
       fin=(bin(int(origin))[2:])
    elif cnvrt==8: #8진수
       print("8")
    elif cnvrt==10: #10진수
       print("10")
    elif cnvrt==12: #12진수
        print("12")
    elif cnvrt==16: #16진수
        print("16")
    elif cnvrt==60: #60진법
        print("60")
    else:
        print("지원하지 않는 진법이거나 내부 오류가 발생했습니다.")
print(fin)