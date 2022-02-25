def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = input("Enter a number: ")
    if int(in_num) > 21:
        diff = abs((int(in_num) - 21) * 2)
    else:
        diff = abs(int(in_num) - 21)
    print(diff)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()