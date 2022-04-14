from random import choice

class Wordlee:
    def __init__(self):
        self.palabras = []
        length = int(input("Longitud de la palabra: "))
        self.load_words(length)
        while True:
            print("1)Existe letra y sé su posición\n2)Existe letra pero no sé su posición\n3)No existe\n4)Ver palabras actuales\n5)Exportar a txt\n6)Sugerir palabra")
            try:
                option = int(input("Opción: "))
            except KeyboardInterrupt:
                exit()
            except:
                option = ''
            if option == 1:
                letra = input("Introduce la letra: ")
                posicion = int(input("Posición: "))
                self.letter_and_position(letra, posicion)
                
            elif option == 2:
                letras = input("Introduce las letras: ").split(',')
                self.letter_without_position(letras)

            elif option == 3:
                letras = input("Introduce las letras: ").split(',')
                self.no_letter(letras)

            elif option == 4:
                print(self.palabras)
                print(len(self.palabras))

            elif option == 5:
                name = input("Nombre del archivo: ")
                f= open(name,"w+")
                for palabra in self.palabras:
                    f.write(palabra+'\n')
                f.close()
                print("Palabras exportadas.\n")

            elif option == 6:
                print(choice(self.palabras))
            
            elif option == 7:
                exit()

    def letter_and_position(self, letra:str, posicion:int):
        palabras_aux = []
        for i in self.palabras:
            if letra != str(list(i)[posicion - 1]):
                palabras_aux.append(i)
        for _palabra in palabras_aux:
            self.palabras.remove(_palabra)
        print(f"Palabras restantes: {str(len(self.palabras))}. Palabras eliminadas: {str(len(palabras_aux))}")

    def letter_without_position(self, letras:list):
        palabras_aux = []
        for letra in letras:
            for palabra in self.palabras:
                if letra not in palabra:
                    palabras_aux.append(palabra)
        for _palabra in palabras_aux:
            self.palabras.remove(_palabra)
        print(f"Palabras restantes: {str(len(self.palabras))}. Palabras eliminadas: {str(len(palabras_aux))}")

    def no_letter(self, letras:list):
        palabras_aux = []
        for letra in letras:
            for palabra in self.palabras:
                if letra in palabra:
                    palabras_aux.append(palabra)
        for _palabra in palabras_aux:
            try:
                self.palabras.remove(_palabra)
            except:
                pass
        print(f"Palabras restantes: {str(len(self.palabras))}. Palabras eliminadas: {str(len(palabras_aux))}")

    def load_words(self, length:int):
        f = open("palabras.txt", "r")
        for line in f:
            if len(line.strip()) == length:
                self.palabras.append(line.strip())
        f.close()
        print("Palabras cargadas: "+str(len(self.palabras)))


if __name__ == '__main__':
    Wordlee()