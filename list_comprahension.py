def run():
    #squares = []
    #for i in range(1,100):
    #    if i%3 !=0:           
    #        squares.append(i**2)
    squares = [i**2 for i in range(1,101) if i%3 !=0]  
    list_challenge = [ i for i in range(1, 100000) if i % 36 == 0]
    #print(squares)
    for i in range(0,10):
        print(list_challenge[i])

    my_list = [1,2,3,4,5]
    list_challenge2 = [i**2 for i in my_list]
    print ("Lista 2: " + str(list_challenge2))

    

if __name__ == '__main__':
    run()