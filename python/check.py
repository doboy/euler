import re
from subprocess import check_output
import sys, time
import os.path

def check( prob, answer ):
    answer = answer.strip()
    if answer == "None":
        return "Unsolved"
    elif not os.path.isfile( "python/p%s.py" % prob ):
        return "Unwritten"
    else:
        try:
            start = time.time()
            output = check_output([ "python", "python/p%s.py" % prob ])
            end = time.time()

            if not output:
                return "In Progress"
            elif answer == output.strip():
                return "Solved in %0.2fms" % (end - start)
            else:
                return "Wrong Output, expected [%s] got [%s]" % (
                    answer, output.strip())

        except:
            return "Error"

def main():
    prob = sys.argv[1]
    if prob == 'Makefile':
        exit()
    answers = open( "txt/check" ).read()
    answer = answers.split()[int(prob) * 2 - 1]
    output = check( prob, answer )
    print "    problem %s:" % prob,
    for out in (sys.stderr, sys.stdout):
        print >>out, output

if __name__ == '__main__':
    main()


