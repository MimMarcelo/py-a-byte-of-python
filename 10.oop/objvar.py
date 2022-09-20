class Robot:
    """Representa um robô, com um nome."""

    # Variável de classe, conta o número de robôs
    population = 0

    def __init__(self, name):
        """Inicia os dados de um novo objeto"""
        self.name = name
        print("Initializing {}".format(self.name))

        # Quando este robô é criado
        # Adicionar 1 à população
        Robot.population += 1

    def die(self):
        """Um robô morre"""
        print(f"{self.name} is being destroyed")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots working")

    def say_hi(self):
        """Saudação feita pelo robô
        
        Sim, eles podem fazer isso"""
        print(f"Greetings, my masters call me {self.name}")

    @classmethod
    def how_many(cls):
        """Imprime a população atual"""
        print(f"We have {cls.population} robots")

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here\n")

print("Robots have finished their work. So let's destroy them")
droid1.die()
droid2.die()

Robot.how_many()
print(Robot.__doc__)