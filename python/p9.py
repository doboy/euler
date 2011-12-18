from utils import triplesGen

for a, b, c in triplesGen():
    if a + b + c == 1000:
        print a * b * c
        break;
    

        
