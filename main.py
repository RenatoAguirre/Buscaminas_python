
pw = 25
ph = 25

import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import IPython.display
import keyboard
import time

perdi = False 
gane = False

fuente = PIL.ImageFont.truetype("ariblk.ttf", 18)
#cuadrado_negro = PIL.Image.new("RGB", (pw, ph)).text((4,0), "X", font=fuente, fill="white")

cursorx = 0
cursory = 0

piezas = []
for i in range(10):
    pieza = PIL.Image.new("RGB", (pw, ph))
    d = PIL.ImageDraw.Draw(pieza)
    if i == 9:
        d.text((4,0), "M", font=fuente, fill="white")
    else:
        d.text((6,0), str(i), font=fuente, fill="white")
    piezas.append(pieza)

for i in piezas[5:]:
    IPython.display.display(i)

piezas_azules = []
for i in range(10):
    pieza_azul = PIL.Image.new("RGB", (pw, ph))
    d = PIL.ImageDraw.Draw(pieza_azul)
    if i == 9:
        d.text((4,0), "M", font=fuente, fill="blue")
    else:
        d.text((6,0), str(i), font=fuente, fill="blue")
    piezas_azules.append(pieza_azul)
for i in piezas_azules[5:]:
    IPython.display.display(i)
    
piezas_rojas = []
for i in range(10):
    pieza_roja = PIL.Image.new("RGB", (pw, ph))
    d = PIL.ImageDraw.Draw(pieza_roja)
    if i == 9:
        d.text((4,0), "X", font=fuente, fill="red")
    else:
        d.text((6,0), str(i), font=fuente, fill="red")
    piezas_rojas.append(pieza_roja)
for i in piezas_rojas[5:]:
    IPython.display.display(i)
    
bandera_img = PIL.Image.new("RGB", (pw, ph))
b = PIL.ImageDraw.Draw(bandera_img)
b.text((4,0), "r", font=fuente, fill="red")
IPython.display.display(bandera_img)

bandera_azul_img = PIL.Image.new("RGB", (pw, ph))
b = PIL.ImageDraw.Draw(bandera_azul_img)
b.text((4,0), "r", font=fuente, fill="blue")
IPython.display.display(bandera_azul_img)

piezas_verdes = []
for i in range(10):
    pieza_verde = PIL.Image.new("RGB", (pw, ph))
    d = PIL.ImageDraw.Draw(pieza_verde)
    if i == 9:
        d.text((4,0), ":)", font=fuente, fill="green")
    else:
        d.text((6,0), str(i), font=fuente, fill="green")
    piezas_verdes.append(pieza_verde)
for i in piezas_rojas[5:]:
    IPython.display.display(i)

# %%
filas = 8
cols = 8
cantm = 10

def crear_matriz():
    global filas, cols, cantm
    
    import random

    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(cols):
            matriz[i].append(0)
    nueves = 0
    while nueves < cantm:
        x = random.randint(0, filas-1)
        y = random.randint(0, cols-1)
        if matriz[x][y] == 0:
            matriz[x][y] = 9
            nueves += 1
    for i in range(filas):
        for j in range(cols):
            if matriz[i][j] == 9:
                #arriba
                if (i-1) >= 0 and (j-1) >= 0 and matriz[i-1][j-1] != 9:
                    matriz[i-1][j-1] += 1
                if (i-1) >= 0 and matriz[i-1][j] != 9:
                    matriz[i-1][j] += 1
                if (i-1) >= 0 and (j+1) < cols and matriz[i-1][j+1] != 9:
                    matriz[i-1][j+1] += 1
                #centro
                if (j-1) >= 0 and matriz[i][j-1] != 9:
                    matriz[i][j-1] += 1
                if (j+1) < cols and matriz[i][j+1] != 9:
                    matriz[i][j+1] += 1
                #abajo
                if (i+1) < filas and (j-1) >= 0 and matriz[i+1][j-1] != 9:
                    matriz[i+1][j-1] += 1
                if (i+1) < filas and matriz[i+1][j] != 9:
                    matriz[i+1][j] += 1
                if (i+1) < filas and (j+1) < cols and matriz[i+1][j+1] != 9:
                    matriz[i+1][j+1] += 1
    return matriz
#matriz = crear_matriz()
#matriz

# %%
imgw = cols * (pw+2) + 2
imgh = filas * (ph+2) + 2

base_img = PIL.Image.new("RGB", (imgw, imgh))
for i in range(imgh):
    for j in range(imgw):
        base_img.putpixel((i,j), (150, 150, 150))
base_img

# %%
import time

"""for i in range(filas):
    for j in range(cols):
        num = matriz[i][j]
        #time.sleep(1)
        base_img.paste(piezas[num], ((pw+2)*j+2, (ph+2)*i+2))
IPython.display.clear_output(wait=True)
IPython.display.display(base_img)"""
        

# %%
def crear_matriz_inicial(w, h):
    inicial = []
    for i in range(h):
        inicial.append([])
        for j in range(w):
            inicial[i].append(-1)
    return inicial

# %%
#matriz_inicial = crear_matriz_inicial(8,8)
#matriz_inicial

# %%
#matriz

# %%
def despejar(i,j):
    global matriz, matriz_inicial, perdi
    if i < 0 or i >= 8:
        return
    if j < 0 or j >= 8:
        return
    if matriz_inicial[i][j] == -1:
        matriz_inicial[i][j] = matriz[i][j]
        #print(matriz_inicial[i][j])
        if matriz_inicial[i][j] == 9:
            #print("Perdi")
            perdi = True

        if matriz_inicial[i][j] == 0:
            despejar(i-1, j-1)
            despejar(i-1, j)
            despejar(i-1, j+1)
            despejar(i, j-1)
            despejar(i, j+1)
            despejar(i+1, j-1)
            despejar(i+1, j)
            despejar(i+1, j+1)

# %%
#despejar(6,2)

# %%
#matriz_inicial

# %%

def print_matriz():
    global matriz_inicial, base_img, piezas, cursorx, cursory, piezas_azules, pw, ph
    #print(cursorx, cursory)
    if cursorx > 7:
        cursorx = 0
    if cursorx < 0:
        cursorx = 7
    if cursory > 7:
        cursory = 0
    if cursory < 0:
        cursory = 7
        
    for i in range(filas):
        for j in range(cols):
            num = matriz_inicial[i][j]
            #time.sleep(0.1)
            base_img.paste(piezas[num], ((pw+2)*j+2, (ph+2)*i+2))
    #print(piezas_azules[matriz_inicial[cursorx][cursory]])
    #print(bandera_img)
    #print(cursorx, cursory)
    base_img.paste(piezas_azules[matriz_inicial[cursorx][cursory]], ((pw+2)*cursory+2, (ph+2)*cursorx+2)) #esta linea es para poner el cursor
    #if len(banderas) >=1:
        #print(banderas[0])
        #base_img.paste(bandera_img, ((pw+2)*5+2, (ph+2)*5+2))
    if len(banderas) >=1:
        for bandera in banderas:
            if bandera[1] == cursory and bandera[0] == cursorx:
                base_img.paste(bandera_azul_img, ((pw+2)*bandera[1]+2, (ph+2)*bandera[0]+2))
            else:
                base_img.paste(bandera_img, ((pw+2)*bandera[1]+2, (ph+2)*bandera[0]+2))
            
    IPython.display.clear_output(wait=True)
    IPython.display.display(base_img)
    
def print_matriz_roja():
    global matriz_inicial, base_img, piezas, cursorx, cursory, piezas_azules, pw, ph, piezas_rojas
    for i in range(filas):
        for j in range(cols):
            num = matriz_inicial[i][j]
            #time.sleep(0.1)
            base_img.paste(piezas_rojas[num], ((pw+2)*j+2, (ph+2)*i+2))
    #base_img.paste(piezas_azules[matriz_inicial[cursorx][cursory]], ((pw+2)*cursory+2, (ph+2)*cursorx+2)) #esta linea es para poner el cursor
    IPython.display.clear_output(wait=True)
    IPython.display.display(base_img)
    
def print_matriz_verde():
    global matriz_inicial, base_img, piezas, cursorx, cursory, piezas_azules, pw, ph, piezas_verdes
    for i in range(filas):
        for j in range(cols):
            num = matriz_inicial[i][j]
            #time.sleep(0.1)
            base_img.paste(piezas_verdes[num], ((pw+2)*j+2, (ph+2)*i+2))
    #base_img.paste(piezas_azules[matriz_inicial[cursorx][cursory]], ((pw+2)*cursory+2, (ph+2)*cursorx+2)) #esta linea es para poner el cursor
    IPython.display.clear_output(wait=True)
    IPython.display.display(base_img)
#print_matriz()

# %%
#despejar(1,1)
#print_matriz()

# %%
#despejar(0,0)
#print_matriz()

# %%
def checkear_win():
    global matriz, matriz_inicial, gane
   
    
    for i in range(filas):
        for j in range(cols):
            if matriz_inicial[i][j] != matriz[i][j]:
                if matriz_inicial[i][j] == -1 and matriz[i][j] != 9:
                    #print("hola")
                    return
     
    gane = True      
            
    
    
    

banderas = []
matriz = crear_matriz()
#for fila in matriz:
    #print(fila)
    
matriz_inicial = crear_matriz_inicial(8,8)
#for fila in matriz_inicial:
    #rint(fila)
#print(matriz_inicial)
print_matriz()
while True: 
    if perdi:
        #print_matrizroja
        print_matriz_roja()
        time.sleep(2)
        banderas = []
        matriz = crear_matriz()
        matriz_inicial = crear_matriz_inicial(8,8)
        print_matriz()
        
        perdi = False 
        

    if gane:
        print_matriz_verde()
        time.sleep(2)
        matriz = crear_matriz()
        banderas = []
        matriz_inicial = crear_matriz_inicial(8,8)
        print_matriz()
        gane = False
        

    if keyboard.is_pressed("up arrow"):
        #print("up arrow")
        cursorx -= 1
        print_matriz()
        time.sleep(0.1)
        
        print(cursory)
    if keyboard.is_pressed("down arrow"):
        #print("down arrow")
        cursorx += 1
        print_matriz()
        
        time.sleep(0.1)
    if keyboard.is_pressed("left arrow"):
        #print("left arrow")
        cursory -= 1
        print_matriz()
        time.sleep(0.1)
        
    if keyboard.is_pressed("right arrow"):
        #print("right arrow")
        cursory +=1
        print_matriz()
        time.sleep(0.1)
        
    if keyboard.is_pressed("enter"):
        despejar(cursorx, cursory)
        print_matriz()
        time.sleep(0.1)
        for fila in matriz:
            print(fila)
        print("--------------------------------------------")
        for fila in matriz_inicial:
            print(fila)
        
        checkear_win()
    if keyboard.is_pressed("r"):
        time.sleep(0.2)
        if (cursorx, cursory) not in banderas:
            banderas.append((cursorx, cursory))
        else:
            banderas.remove((cursorx, cursory))
        time.sleep(0.2)
        print_matriz()
        #for f in banderas:
            #print(f)
        time.sleep(0.1)
    if keyboard.is_pressed('esc'):
        break