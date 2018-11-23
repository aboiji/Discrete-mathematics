
# 2진법으로 바꾸는 함수
def des2bin( num, bits = 16):
    binnum = list()

    while num > 0:
        binnum.insert(0,num%2)
        num = num//2
    
    lenbinnum = len(binnum)
    if lenbinnum < bits:
        binnum = [0]*(bits-lenbinnum) + binnum
    
    if lenbinnum > bits:
        print('숫자가 너무 큼')
        binnum = binnum[lenbinnum - bitss:]
    return binnum


# 10 -> 2 진법 함수
# 보수를 이용해 음수도 표현할 수 있음
# 0과 1로 된 비트수 길이의 리스트 리턴 
# num : 숫자 입력
# com : 1의 보수 = 1, 2의 보수 = 2 (기본 2의 보수)
# bits : 몇비트 (기본 16비트)
def new_des2bin( num, com = 2, bits = 16):
    if num < 0:
        num = -num
        binnum = des2bin( num, bits)
        if com == 1:
            binnum = complement( binnum, com = com, bits = bits)
        elif com == 2:
            binnum = complement( binnum, com = com, bits = bits)
    else:
        binnum = des2bin( num, bits)
    
    return binnum


# 이진법 더하는 함수
# 두개의 이진법 리스트를 더함

def bin_add( bin1, bin2, com = 2):
    len1 = len(bin1)
    len2 = len(bin2)


    if len1 < len2:
        bin1 =  [0]*(len2 - len1 ) + bin1
        biglen = len2

    else:
        bin2 = [0]*(len1 - len2 ) + bin2
        biglen = len1

    new_bin = [0]*(biglen + 1)

    for i in range(biglen, 0, -1):
        num = new_bin[i] + bin1[i-1] + bin2[i-1]
        new_bin[i] = num % 2
        new_bin[i - 1] += num // 2      
    
    if com == 1 and new_bin[0] == 1:
        new_bin = bin_add(new_bin, [1], com = com)
    new_bin = new_bin[1:]
    
    return new_bin


#보수를 취해주는 함수
def complement(binnum, com = 2, bits = 16):
    if com == 1 :
        binnum = [(1,0)[bit] for bit in binnum]
    else:
        binnum = bin_add(complement(binnum, com = 1), [1], bits)
    return binnum


# 이진법을 정수로 변환 해준다.
def bin2dec(binnum, com = 2):
    if binnum[0] == 1:
        binnum = complement(binnum, com = com, bits = len(binnum))
        num = 0
        binlen = len(binnum)
        for x in range(binlen):
            num += binnum[binlen-x-1] * 2**x
        
        return -num
    else:
        num = 0
        binlen = len(binnum)
        for x in range(binlen):
            num += binnum[binlen-x-1] * 2**x
        return num


def main():
    num1 = int(input("첫번쨰 숫자를 입력하세요 : "))
    num2 = int(input("두번째 숫자를 입력하세요 : "))
    bits = 16

    print("1의 보수로 연산")
    num1_com1 = new_des2bin(num1, com = 1, bits = bits)
    num2_com1 = new_des2bin(num2, com = 1, bits = bits)
    sum_com1 = bin_add(num1_com1, num2_com1, com = 1)
    print(bin2dec(sum_com1, com = 1))

    print("2의 보수로 연산")
    num1_com2 = new_des2bin(num1, com = 2, bits = bits)
    num2_com2 = new_des2bin(num2, com = 2, bits = bits)
    sum_com2 = bin_add(num1_com2, num2_com2, com = 2)
    print(bin2dec(sum_com2, com = 2))

if __name__ == "__main__":
    main()
    print(" 1801127 김민수")





    


