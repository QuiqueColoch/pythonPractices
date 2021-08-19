def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num% i == 0:
            divisors.append(i)
        
    return divisors
    

def run():
    num_ok=True
    while(num_ok):
        num = input("Ingresa un numero: ")
        assert num.isnumeric(),"Debes ingresar un numero"
        assert num<0, "Debes ingresar un numero positivo"
        

    print(divisors(int(num)))
    print("Termino mi programa")    
    
if __name__ == "__main__":
    run() 