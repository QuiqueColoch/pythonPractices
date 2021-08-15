def run():
    my_list = [1,"Hello",True,4.5]
    my_dict = {"firstname" : "Facundo","lastname" : "Garcia"}

    super_list = [
        {"firstname" : "Facundo","lastname" : "Garcia"},
        {"firstname" : "Pepe","lastname" : "Lopez"},
        {"firstname" : "Marlon","lastname" : "Garcia"},
        {"firstname" : "Maribel","lastname" : "Primero"},
        {"firstname" : "Enrique","lastname" : "Coloch"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5,6],
        "integer_nums" : [-1,2,3,-1,3],
        "floating_nums" : [34.2,412.23,42.1,55,2]
    }

    for key, value in super_dict.items():
        print(key, ":", value)

    for i in super_list:
        print(i)

if __name__== '__main__':
    run()