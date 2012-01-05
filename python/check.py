from ast import literal_eval
from subprocess import check_output, CalledProcessError
import sys, time, compileall
import os.path

Summary = {}
sys.stderr = sys.stdout
compileall.compile_dir( "." )


def check( prob, answer ):
    if answer.strip() == "None":
        return "Unsolved", None
    elif not os.path.isfile( "p%s.py" % prob ):
        return "Unwritten", None
    else:
        try:
            start = time.time()
            output = check_output([ "python", "p%s.pyc" % prob ])
            end = time.time()

            if not output:
                return "In Progress", None
            elif answer.strip() == output.strip():
                return "Solved", end - start
            else:
                return "Wrong Output", None

        except:
            return "Error", None

if len( sys.argv ) > 1:
    _, prob, answer = sys.argv
    outcome, duration = check( prob, answer )
    
    output = "    problem %s: %s" % ( prob, outcome )

    if outcome == "Solved":
        output += " in %0.2fms" % ( duration * 1000 )

    print output

else:    
    README = open( "README.md", "w" )
    for line in open( "../txt/check" ):
        prob, answer = line.split()
        outcome, duration = check( prob, answer )
    
        output = "    problem %s: %s" % ( prob, outcome )

        if outcome == "Solved":
            output += " in %0.2fms" % ( duration * 1000 )

        for out in ( README, sys.stdout ):
            print >>out, output

        Summary[ outcome ] = Summary.get( outcome, 0 ) + 1

    summary = "    Summary:\n"
    for k, v in Summary.items():
        summary += "      %s: %s\n" % ( k, v )

    for out in ( README, sys.stdout ):
        print >>out, summary
