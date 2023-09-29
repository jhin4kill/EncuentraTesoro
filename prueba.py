import random
import keyboard

x, y = random.randint(0, 4), random.randint(0, 4)
#print('[', x, ']','[', y, ']')



objetos = {'POZO1': [3,4] , 'POZO2' : [2,3], 'TESORO' : [1,1], 'GUMPY' : [4,2]}

#for obj in objetos:
    #print(obj)

posicion = 0,0
matrizprueba = [[4,8],
                ['A','G']]
for fila in matrizprueba:
    print(fila)
    for casilla in fila:
        print(casilla)

print(objetos['POZO1'][1])

while True:
    if keyboard.is_pressed('p'):
        print('Presionaste p, adios!!')
        break