from ast import literal_eval as eval
from subprocess import check_output
import sys
sys.stderr = sys.stdout

def check( prob, answer ):
    try:
        output = check_output( ["python", "p%s.py" % prob] )
        try:
            output = check_output( ["python", "p%s.py" % prob] )
            assert answer == eval( output )
            print "    problem %s: Passed" % prob
        except:
            print >>sys.stderr, "    problem %s:" \
                " \n        expected: %s" \
                " \n        got: %s" \
                " \n " % ( prob, answer, output or None)
    except:
        print >>sys.stderr, "    problem executing file %s" % prob
        # raw_input("uhh..")

for line in open( "../txt/check" ):
    prob, answer = line.split()
    check( prob, eval( answer ) ) if eval( answer ) else None
