import numpy

set1 = set(("A", "B", "C", "D"))
set2 = set(("C", "D", "E", "F"))

# 합집합
def union( s1, s2):
    return s1|s2

# 교집합
def intersection( s1, s2):
    return s1&s2

# 차집합
def complement( s1, s2):
    return set1 - set2

# 대칭 차집합
def sym_diff( s1, s2):
    return set1 ^ set2

arr1 = numpy.array([[1,2],[3,4]])
matrix = numpy.asmatrix(arr1)


def main():
    print("집합 연산\n")
    print("set1 :", set1)
    print("set2 :", set2)
    print()

    for f in [ union, intersection, complement, sym_diff]:
        print("{} {}".format( f.__name__, f( set1, set2)))
    
    print("\n\n 행렬 연산\n")
    print("배열\n", arr1)
    print("행렬\n", matrix)
    print("행렬 곱 \n{}\n".format( matrix*matrix))
    print("전치 행렬\n{}".format( matrix.T))



if __name__ == "__main__":
    main()
    print("1801127 김민수")
