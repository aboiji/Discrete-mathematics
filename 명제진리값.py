# 논리합
def OR( p, q):
    return p|q

# 논리곱
def AND( p, q):
    return p&q

# 배타적 논리합
def XOR( p, q):
    return  ( not(p) and q ) or (p and not(q))

# 조건명제
def NOT( p):
    return not p


def main():
    for f in (OR, AND, XOR):
        print( "\n", f.__name__)
        for p, q in ( ( True, True), ( True, False), ( False, True), ( False, False)):
            print("{} {} {} = {}".format( p, f.__name__, q, f( p, q)))
    print("\n{} {} = {}".format("NOT", True, NOT(True)))
    print("{} {} = {}".format("NOT", False, NOT(False)))

if __name__ == "__main__":
    main()
    print("1801127 김민수")