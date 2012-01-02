from math import log10

def concealSquare():
    
    def satisfy( num ):
        num = num * num
        for r in xrange( 10, 0, -1 ):
            if num % 10 != r % 10:
                return False
            num //= 100
        return True
    
    def require( num ):
        num = num * num
        r = 10
        while num:
            if num % 10 != r % 10:
                print "require", num, "failed"
                return False
            num //= 100
            r -= 1
        print "require", num, "passed"
        return True

    def helper( sofar, index ):

        if satisfy( sofar ):
            return sofar

        for i in xrange( 10 ):
            next = i * 10 ** index + sofar

            print next, i
            # raw_input()

            if not require( next ):
                continue

            else:
                ret = helper( next, index + 1 )
                if ret:
                    return ret

    return helper( 0, 0 )

# print concealSquare()
