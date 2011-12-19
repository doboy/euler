from ast import literal_eval
from subprocess import check_output
import sys, time

sys.stderr = sys.stdout
# Unsolved, Solved
# Wrong Output, In Progress

Summary = { "Solved": 0,
            "Unsolved": 0,
            "In Progress": 0,
            "Wrong Output" : 0
}

def check( prob, answer ):
    if not answer:
        return "Unsolved",
    else:
        try:
            start = time.time()
            output = check_output( ["python", "p%s.py" % prob] )
            if not output:
                return "In Progress",
            elif answer == literal_eval( output ):
                return "Solved", ( time.time() - start ) * 1000
            else:
                return "Wrong Output",
        except:
            return "In Progress",

for line in open( "../txt/check" ):
    prob, answer = line.split()
    result = check( prob, literal_eval( answer ) )
    outcome = result[ 0 ]
    print "    problem %s: %s" % ( prob, outcome ),
    if outcome == "Solved":
        print "in %0.4fms" % result[ 1 ]
    else:
        print
    Summary[ outcome ] += 1

print "    Summary:"
for k, v in Summary.items():
    print "        %s: %s" % ( k, v )
