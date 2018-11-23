def my_sum( l):
    sum = 0
    for x in l:
        sum += x
    return sum

def average( l):
    return sum(l) / len(l)

def mod( n, d):]
    return n - (n//d)*d

def main():
    a = input("입력하세요 : ")
    l = map( int, a.split())
    print( "결과 :", mod( *l))

if __name__ == "__main__":
    main()
    print("copyright 1801127 김민수")