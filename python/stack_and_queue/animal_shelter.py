from stack_and_queue.node  import Node
# from node  import Node


class Animal:
    """
    Animal class creates Animals objects.

     Arguments:
     pref : str
    """
    def __init__(self, name, specie, next_ = None):
        self.name = name
        self.specie = specie
        self.next = next_


class Cat(Animal):
    """
    Cat class creates Cats.

     Arguments:
     name : str
    """
    def __init__(self, name):
        super().__init__(name, specie = "cat")



class Dog(Animal):
    """
    Dog class creates Dogs.

     Arguments:
     name : str
    """
    def __init__(self, name):
        super().__init__(name, specie = "dog")


class Mouse(Animal):
    """
    Mouse class creates Mice.

     Arguments:
     name : str
    """
    def __init__(self, name):
        super().__init__(name, specie = "mouse")


class Horse(Animal):
    """
    Horse class creates Horses.

     Arguments:
     name : str
    """
    def __init__(self, name):
        super().__init__(name, specie = "horse")



class AnimalShelter:
    """
    AnimalShelter class queues cats and dogs.

     Arguments:
     front: Node
     back: Node
    """


    def __init__(self, front = None, back = None):
        self.front = front
        self.back = back


    def enqueue(self, animal:Animal):
        """
        This method adds a Cat/Dog object to the AnimalShelter queue.

        Arguments:
        animal: Cat or Dog object
        """
        if animal.specie == "dog" or animal.specie == "cat":
            if not self.front:
                self.front = Node(animal)
                self.back = self.front
            else:
                self.back.next = Node(animal)
                self.back = self.back.next
        else:
            print("Shelter can only take in cats and dogs.")
            return False


    def dequeue(self, pref):
        """
        This method removes a Cat/Dog object to the AnimalShelter queue.

        Arguments:
        pref : Cat or Dog object

        Return: Dequeued object / None
        """
        if pref == "dog" or pref == "cat":

            if not self.front:
                raise Exception("Queue is empty.")



            if pref == self.front.value.specie:
                dispose = self.front
                self.front = self.front.next
                dispose.next = None

                if dispose == self.back:
                    self.back == None
                return dispose.value.name


            else:
                previous = self.front
                current = self.front
                dispose = current


                while pref != dispose.value.specie:
                    previous = current
                    current = current.next
                    dispose = current



                current = current.next
                previous.next = current
                dispose.next = None

                if dispose == self.back:
                    self.back == None

            return dispose.value.name



        else:
            print("Shelter has only cats and dogs.")
            return None




if __name__ == '__main__':
    shelter = AnimalShelter()
    dog = Dog("dog")
    cat = Cat("cat")
    mouse = Mouse("mouse")
    mat = Cat("mat")
    pat = Cat("pat")
    bog = Dog("bog")
    sog = Dog("sog")

    shelter.enqueue(mat)
    shelter.enqueue(dog)
    shelter.enqueue(bog)
    shelter.enqueue(sog)
    shelter.enqueue(cat)
    shelter.enqueue(pat)

    print("before", shelter.front.value.name)
    print("before", (shelter.front.next).value.name)
    print("before", (shelter.front.next).next.value.name)

    shelter.dequeue("dog")

    print("after", (shelter.front.value.name))
    print("after", (shelter.front.next).value.name)
    print("after", (shelter.front.next).next.value.name)


