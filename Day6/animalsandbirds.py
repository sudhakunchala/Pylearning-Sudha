# we have created same functions in animals module and birds module
# we need to use those functions in animalandbirds module

#Approch1:
# import animals
# import birds
# animals.fly()
# animals.color()
# birds.fly()
# birds.color()


#Approch2:
from animals import fly,color
fly()
color()
from birds import fly,color
fly()
color()


