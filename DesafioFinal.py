class Heroi():
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    def atacar(self):
        ataque = ""

        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'um ataque desconhecido'

        print(f"O {self.tipo} de nome {self.nome} atacou usando {ataque}\n")

#exemplo
heroi1 = Heroi('Garem',30, 'guerreiro')
heroi2 = Heroi('Ryze', 150, 'mago')
heroi3 = Heroi('Lee', 70, 'monge')
heroi4 = Heroi('Xin', 70, 'ninja')
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
