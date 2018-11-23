import chi_no # 전과제에서 만든 2진법 더하기 함수 bin_add 함수가 구현되어 있습니다.

############## 이산수학 진볍 변환기 ###############

class my_num( int):
    def __init__( self, num, base = 10, ):
        int().__init__(self, num, base)
        self.row_text = num
    
    
    def convert( self, n = 10, t = "0123456789abcdefghijklmnopqrstuvwxyz"):
        new_num = list()
        temp_num = self
        if temp_num < 0:
            new_num.append("-")
            temp_num *= -1
                                
        while temp_num:                                 
            new_num.insert(0, t[temp_num%n])
            temp_num = temp_num//n
        
        return "".join(new_num)
    
    def complement( self, num):
        tempnum = ''.join(['1',"0"][int(bit)] for bit in self.row_text)
        if num == 2:
            tempnum = chi_no.bin_add(tempnum, '1')
        return tempnum

        


'''
(1,2)의 보수를 정할떄 자릿수는 입력한 문자열의 길이에 따라 변합니다.
예를 들어 0001은 4비트로 인식하여 1의 보수는 1110 이 됩니다.
         000001은 6비트로 인식하여 1의 보수는 111110 이 됩니다.
앞에 0을 삽입하여 자릿수를 정해줘야 정상 작동됩니다
'''

def main():
    num = my_num(input("2진법 숫자를 입력하세요 : "), base = 2)
    num1 = num.complement(1)
    num2 = num.complement(2)
    
    print("1의 보수 : {}\n2의 보수 : {}".format(num1, num2))

if __name__ == "__main__":
    main()
    print("1801127 김민수")

