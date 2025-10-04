from logging import exception

from person import Person

def main():
    print("Hello World")
    example_name = "Pelda"

    people = []
    while len(Person.example_names) != 0:
        example_name = Person.example_names.pop()
        pe = Person("Id",example_name,27,False)
        people.append(pe)

    print(people)
    #if len(Person.example_names) != 0:
    #    example_name = Person.example_names.pop(0)


    p1 = Person("p1", example_name, 45, False)
    p2 = Person("p2", "Barbara", 20, True)
    p3 = Person("p1", "Csaba", 26, True)


   #print(p1)
   #print(p2.id)

   #print(Person.is_adult(p1))
   #print(Person.num_of_people)

   #print(p1.getId())
   #print(p1.getName())

    try:
        p1.age = 16
    except ValueError:
        print("Invalid age")
    except Exception:
        print("Invalid type")

    print(p1.name)

if __name__ == '__main__':
    main()