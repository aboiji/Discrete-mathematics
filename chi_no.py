from gochiusa import my_num # gochiusa 에는 전 과제에서 만든 10진법을 2 진법으로 바꿔주는 my_num 클레스가 있습니다.

def bin_add( num1, num2):
    return my_num(my_num( num1, base =2) + my_num( num2, base =2)).convert(2)

def main():
    num1, num2 = input("첫번쩨 이진법 숫자 : "), input("두번쩨 이진법 숫자 : ")
    print(bin_add( num1, num2))


if __name__ == "__main__":
    main()
    print("1801127 김민수")