class filled:
    def square(n):
        for i in range(n):
                print("*  " * n)

    def increasingTriangle(n):
        for i in range(n+1):
            print("* " * i)
        print()

    def decreasingTriangle(n):
        for i in range(n, -1, -1):
            print("* " * i)
        print()

    def pyramid(n):
        for i in range(1, n+1):
            print("  "*(n-i) + "* "*(2*i-1))
        print()

    def reversePyramid(n):
        for i in range(n, -1, -1):
            print("  "*(n-i) + "* "*(2*i-1))
        print()

    def diamond(n):
        for i in range(1, n+1):
            print("  "*(n-i) + "* "*(2*i-1))

        for i in range(n-1, 0, -1):
            print("  "*(n-i) + "* "*(2*i-1))
        print()

    def hourglass(n):
        for i in range(n, 0, -1):
            print("  "*(n-i) + "* "*(2*i-1))

        for i in range(2, n+1):
            print("  "*(n-i) + "* "*(2*i-1))
        print()

    def heart(n):
        print(f"n = {n}")
        top2 = n-2 // 2
        top1 = top2 - 2

        print(" " + "*"*top1 + " "*3 + "*"*top1)
        print("*"*top2 + " " + "*"*top2)

        for i in range(n, 0, -1):
            print(" "*(n-i) + "*"*(2*i-1))
        print()

class notFilled:
    def square(n):
        print("*  "*n)
        for i in range(1, n-1):
            print("*  " + "  "*(n-1) + " *")
        print("*  "*n)
        print()

    def increasingTriangle(n):
        for i in range(n+1):
            print("* "*i)
        print()

filled.square(5)
filled.increasingTriangle(5)
filled.decreasingTriangle(5)
filled.pyramid(3)
filled.reversePyramid(3)
filled.diamond(3)
filled.hourglass(3)
filled.heart(5)
filled.heart(7)
filled.heart(6)

notFilled.square(5)
notFilled.increasingTriangle(5)
