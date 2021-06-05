def run():
    squares = []

    for i in range(1,101):
        if(i%3!=0):
            squares.append(i**2)

    #print(squares)


    squaresNot3Multiple = []

    for i in range(1,101):
        if(i%3 != 0):
            squaresNot3Multiple.append(i**2)

    squaresComprehension = [i**2 for i in range(1,101) if i%3 != 0]


    squareChallenge = [i for i in range(1,10000) if i%4==0 and i%6 == 0 and i%9 == 0] 

    print(squareChallenge)

if __name__ == '__main__':
    run()
