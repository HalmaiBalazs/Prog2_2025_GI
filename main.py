from drink import Drink

def main():
    cola = Drink('Cola',"5 dl", 50)
    fanta = Drink('Fanta',"1 liter", 100)
    mirinda = Drink('Mirinda',"1 liter", 100)

    print(fanta)
    print(cola.size)
if __name__ == '__main__':
    main()