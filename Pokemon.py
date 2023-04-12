# definicao da classe Pokemon
class Pokemon():
    def __init__(self, name, generation, type1, type2, height, weight):
        self.name = name
        self.generation = generation
        self.type1 = type1
        self.type2 = type2
        self.height = height
        self.weight = weight

    def show(self):
        print('( '+str(self.name)+'\t'+
              str(self.generation)+'\t'+
              str(self.type1)+'\t'+
              str(self.type2)+'\t'+
              str(self.height)+'m'+'\t'+
              str(self.weight)+'Kg'+' )'
              )

    def get_pokemon_info(self):
        return '( '+'🟩 '+str(self.name)+'\t'+'🟩 '+str(self.generation)+'\t'+'🟩 '+str(self.type1)+'\t'+'🟩 '+str(self.type2)+'\t'+'🟩 '+str(self.height)+'m'+'\t'+'🟩 '+str(self.weight)+'Kg'+' )'
              
              
              
              
              