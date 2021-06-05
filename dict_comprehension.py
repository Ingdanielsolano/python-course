import math
def run():
    dictComprehension = { i: i**3 for i in range(1,101) if i % 3 != 0}

   # print(dictComprehension)

    dictChallenge = {i: math.sqrt(i) for i in range (1,1000)}

    print(dictChallenge)

if __name__ == '__main__':
    run()
