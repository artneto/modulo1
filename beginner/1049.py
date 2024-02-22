#you must read 3 words that define the type of possible animal according
#  to the diagram below, from left to right. Then conclude which of the following
#  animals was chosen, using the three words provided.
animals = {
    'aguia': {'carnivoro', 'ave', 'vertebrado'},
    'pomba': {'onivoro', 'ave', 'vertebrado'},
    'homem': {'onivoro', 'mamifero', 'vertebrado'},
    'vaca': {'herbivoro', 'mamifero', 'vertebrado'},
    'pulga': {'hematofago', 'inseto', 'invertebrado'},
    'lagarta': {'herbivoro', 'inseto', 'invertebrado'},
    'sanguessuga': {'hematofago', 'anelideo', 'invertebrado'},
    'minhoca': {'onivoro', 'anelideo', 'invertebrado'}
}

descricao_animal1 = str(input())
descricao_animal2 = str(input())
descricao_animal3 = str(input())

#The items() method returns a view object.
for animal, descricao in animals.items():
    if descricao_animal1 in descricao and descricao_animal2 in descricao and descricao_animal3 in descricao:
        print(animal)
        break
else:
    print("Nenhum animal corresponde às características fornecidas.")