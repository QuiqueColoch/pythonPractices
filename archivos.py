def write():
    names = ["Martin","Jose","Manuel", "Pepé","Christian", "Manolo"]
    with open("./archivos/names.txt","a",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def read():
    numbers =[]
    with open("./archivos/numbers.txt","r",encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def run():
   write()

if __name__ == '__main__':
    run()