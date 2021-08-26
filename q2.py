from random import randint
import time

class Mago:
    def __init__(self, principal):
        if principal:
            self.nome = input("Insira o nome do seu personagem: ")
        self.vida = 100
        self.mana = 100
        self.recuperacao_de_mana = 15
        self.classe = 1

    def getClasse(self):
        return self.classe

    def getGolpes(self):
        self.golpes = ["Bola de Fogo", "Tiro Arcano", "Tiro Gelado"]
        return self.golpes
    
    def info_golpes(self):
        self.getBola_de_fogo()
        self.getTiro_arcano()
        self.getTiro_gelado()
    
    def usarAtaque(self, index, principal):
        rng = randint(1,100)
        if index == 1:
            if self.mana < 50  and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <50:
                return False
            else:
                self.mana = self.mana - 50
                if rng <= 65:
                    return 30
                else:
                    return 0
        if index == 2:
            if self.mana < 20 and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <20:
                return False
            else:
                self.mana = self.mana - 20
                if rng <= 80:
                    return 10
                else:
                    return 0
        if index == 3:
            if self.mana < 20 and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <20:
                return False
            else:
                self.mana = self.mana - 20
                if rng <= 70:
                    return 20
                else:
                    return 0

    def getBola_de_fogo(self):
        gasto_de_mana = 50
        dano = 30
        taxa_de_acerto = 65
        nome = "Bola de Fogo"
        print( f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")
    
    def getTiro_arcano(self):
        gasto_de_mana = 20
        dano = 10
        taxa_de_acerto = 80
        nome = "Tiro Arcano"
        print(f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")
    
    def getTiro_gelado(self):
        gasto_de_mana = 20
        dano = 20
        taxa_de_acerto = 70
        nome = "Tiro Gelado"
        print( f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")
    
    def getLoot(self):
        print("Você tem 20 % de chance de receber o Cajado de Jaina:")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        rng = randint(1,100)
        if rng <= 20:
            print("Você ganhou o Cajado de Jaina")
        else:
            print("Você não ganhou o Cajado de Jaina")

class Guerreiro:
    def __init__(self, principal):
        if principal:
            self.nome = input("Insira o nome do seu personagem: ")
        self.vida = 150
        self.mana = 70
        self.recuperacao_de_mana = 25
        self.classe = 2

    def getClasse(self):
        return self.classe

    def getGolpes(self):
        self.golpes = ["Cortar", "Empurrar", "Ultimato"]
        return self.golpes
    
    def info_golpes(self):
        self.getCortar()
        self.getEmpurrar()
        self.getUltimato()

    def usarAtaque(self, index, principal):
        rng = randint(1,100)
        if index == 1:
            if self.mana < 40  and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <40:
                return False
            else:
                self.mana = self.mana - 40
                if rng <= 70:
                    return 40
                else:
                    return 0
        if index == 2:
            if self.mana < 10  and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <10:
                return False
            else:
                self.mana = self.mana -10
                if rng <= 90:
                    return 15
                else:
                    return 0    
        if index == 3:
            if self.mana < 70  and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <70:
                return False
            else:
                self.mana = self.mana - 70
                if rng <= 50:
                    return 80
                else:
                    return 0
    
    def getCortar(self):
        gasto_de_mana = 40
        dano = 40
        taxa_de_acerto = 70
        nome = "Cortar"
        print( f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")
    
    def getEmpurrar(self):
        gasto_de_mana = 10
        dano = 15
        taxa_de_acerto = 90
        nome = "Empurrar"
        print(f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")

    def getUltimato(self):
        gasto_de_mana = 70
        dano = 80
        taxa_de_acerto = 50
        nome = "Ultimato"
        print( f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")
    
    def getLoot(self):
        print("Você tem 5 % de chance de receber o Machado de Garrosh:")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        rng = randint(1,100)
        if rng <= 5:
            print("Você ganhou o Machado de Garrosh")
        else:
            print("Você não ganhou o Machado de Garrosh")
    
class Bruxo:
    def __init__(self, principal):
        if principal:
            self.nome = input("Insira o nome do seu personagem: ")
        self.vida = 70
        self.mana = 100
        self.recuperacao_de_mana = 60
        self.classe = 3
    
    def getGolpes(self):
        self.golpes = ["Fragmento de Alma", "Seta Sombria", "Abraço Demoníaco"]
        return self.golpes
    
    def getClasse(self):
        return self.classe

    
    def info_golpes(self):
        self.getFragmento_de_alma()
        self.getSeta_sombria()
        self.getAbraco_demoniaco()

    def usarAtaque(self, index, principal):
        rng = randint(1,100)
        if index == 1:
            if self.mana < 80 and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <80:
                return False
            else:
                self.mana = self.mana - 80
                if self.vida + 45 > 70:
                    self.vida = 70
                else:
                    self.vida = self.vida + 45
        if index == 2:
            if self.mana < 60 and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <60:
                return False
            else:
                self.mana = self.mana - 60
                if rng <= 85:
                    return 30
                else:
                    return 0
        if index == 3:
            if self.mana < 100 and principal == True:
                print("Mana insuficiente")
                return False
            if self.mana <100:
                return False
            else:
                self.mana = self.mana - 100
                if rng <= 85:
                    return 75
                else:
                    return 0
    
    def getFragmento_de_alma(self):
        gasto_de_mana = 80
        recuperacao_de_vida = 45
        taxa_de_acerto = 100
        nome = "Fragmento de Alma"
        print(f"Nome do Golpe: {nome} | Recuperação de Vida {recuperacao_de_vida} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")

    def getSeta_sombria(self):
        gasto_de_mana = 60
        dano = 30
        taxa_de_acerto = 85
        nome = "Seta Sombria"
        print( f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")
    
    def getAbraco_demoniaco(self):
        gasto_de_mana = 100
        dano = 75
        taxa_de_acerto = 85
        nome = "Abraço Demoníaco"
        print( f"Nome do Golpe: {nome} | Dano: {dano} \n Taxa de Acerto: {taxa_de_acerto}% | Gasto De Mana: {gasto_de_mana}")

    def getLoot(self):
        print("Você tem 10 % de chance de receber a Mão de Gul'Dan:")
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        rng = randint(1,100)
        if rng <= 10:
            print("Você ganhou a Mão de Gul'Dan")
        else:
            print("Você não ganhou a Mão de Gul'Dan")

class Jogo:
    def __init__(self):
        self.principal = self.escolha_inicial()
        self.vilao = self.inimigo()
    
    def escolha_inicial(self):
        print("Escolha sua classe: ")
        print("1 - Guerreiro")
        print("2 - Mago")
        print("3 - Bruxo")
        escolha = int(input(""))
        if(escolha == 1):
            return Guerreiro(True)
        if(escolha == 2):
            return Mago(True)
        if(escolha == 3):
            return Bruxo(True)
        
    def inimigo(self):
        escolha = randint(1, 3)
        if(escolha == 1):
            return Guerreiro(False)
        if(escolha == 2):
            return Mago(False)
        if(escolha == 3):
            return Bruxo(False)

    def loop_jogo(self):
        while(self.principal.vida != 0 or self.vilao.vida != 0):
            if self.principal.vida <= 0:
                print("Você perdeu!")
                break
            if self.vilao.vida <= 0:
                print("Você venceu! É hora do loot!")
                self.vilao.getLoot()
                break
        
            self.jogo()

    def jogo(self):
        print(f"Você tem {self.principal.vida} pontos de vida e {self.principal.mana} pontos de mana.")
        print(f"Seu oponente tem {self.vilao.vida} pontos de vida.")
        golpes = self.principal.getGolpes()
        continuar = True
        
        while(continuar):
            time.sleep(2)

            print("O que você deseja fazer?")
            print(f"1 - Usar {golpes[0]}")
            print(f"2 - Usar {golpes[1]}")
            print(f"3 - Usar {golpes[2]}")
            print(f"4 - Esperar")
            print(f"5 - Informações sobre os golpes \n")
            escolha = int(input(""))
            if escolha == 1 or escolha == 2 or escolha == 3:
                funcionou = self.principal.usarAtaque(escolha, True)   

                if isinstance(funcionou, bool) == False:
                    continuar = False
                    self.vilao.vida = self.vilao.vida - funcionou
                    print(f"Você causou {funcionou} de dano no inimigo!")
            if escolha == 4:
                print("Você esperou")
                continuar = False

            if escolha == 5:
                self.principal.info_golpes()
        continuar_vilao = True
        while(continuar_vilao):
            rng = randint(1,4)
            funcionou = self.vilao.usarAtaque(rng, False)

            if(funcionou == None):
                funcionou = False

            if(funcionou == False):
                print("O inimigo esperou!")
                continuar_vilao = False
            
            if isinstance(funcionou, bool) == False:
                continuar_vilao = False
                self.principal.vida = self.principal.vida - funcionou
                print(f"Você recebeu {funcionou} de dano do inimigo!")

        self.principal.mana = self.principal.mana + self.principal.recuperacao_de_mana
        self.vilao.mana = self.vilao.mana + self.vilao.recuperacao_de_mana


Jogo().loop_jogo()
