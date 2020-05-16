max_int = 2**31 - 1
min_int = -2**31

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = list(str(x)[1:])
            x.reverse()
            x = ''.join(x)
            x = -int(x)
            if x < min_int:
                return 0
            else:
                return x
        else:
            x = list(str(x))
            x.reverse()
            x = ''.join(x)
            x = int(x)
            if x > max_int:
                return 0
            else:
                return x

    def reverse2(self, x: int) -> int:
        reversed_int = 0
        if x > 0:
            temp = x
            while temp != 0:
                reversed_int = reversed_int * 10 + temp % 10
                if max_int < reversed_int:
                    return 0
                temp //= 10
        else:
            temp = -x
            while temp != 0:
                reversed_int = reversed_int * 10 - temp % 10
                if min_int > reversed_int:
                    return 0
                temp //= 10
        return reversed_int
