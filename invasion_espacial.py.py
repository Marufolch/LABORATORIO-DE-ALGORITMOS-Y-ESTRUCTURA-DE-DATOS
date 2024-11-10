
import pygame
import math
import random
# Inicializar pygame
pygame.init()

# Configurar la pantalla
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Cargar fondo
fondo = pygame.image.load("Fondo.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))  # Asegúrate de que el fondo tenga las dimensiones correctas

# Música de fondo
from pygame import mixer
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Configuración del jugador
img_jugador = pygame.image.load("spaceship.png")
img_jugador = pygame.transform.scale(img_jugador, (60, 60))
jugador_x = 350
jugador_y = 550
jugador_x_cambio = 0

# Enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8
for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# Configuración de las balas
balas = []
img_bala = pygame.image.load("bala.png")

# Configuración del puntaje
puntaje = 0
fuente = pygame.font.Font(None, 32)
texto_x = 10
texto_y = 10

# Funciones de renderizado
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x, y):
    pantalla.blit(img_bala, (x + 16, y + 10))

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    return distancia < 27

# Ciclo de juego
se_ejecuta = True
while se_ejecuta:
    # Dibujar el fondo primero
    pantalla.blit(fondo, (0, 0))
    
    # Procesar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                nueva_bala = {"x": jugador_x, "y": jugador_y, "velocidad": -5}
                balas.append(nueva_bala)
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                jugador_x_cambio = 0
    
    # Actualizar la posición del jugador
    jugador_x += jugador_x_cambio
    jugador_x = max(0, min(jugador_x, 736))  # Limitar al borde

    # Actualizar la posición de los enemigos
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]
        if enemigo_x[e] <= 0 or enemigo_x[e] >= 736:
            enemigo_x_cambio[e] *= -1
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # Detectar colisiones con balas
        for bala in balas:
            if hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"]):
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e], enemigo_y[e] = random.randint(0, 736), random.randint(20, 200)
    
    # Actualizar la posición de las balas
    for bala in balas:
        bala["y"] += bala["velocidad"]
        if bala["y"] < 0:
            balas.remove(bala)
        else:
            disparar_bala(bala["x"], bala["y"])

    # Mostrar los elementos en la pantalla
    jugador(jugador_x, jugador_y)
    for e in range(cantidad_enemigos):
        enemigo(enemigo_x[e], enemigo_y[e], e)
    mostrar_puntaje(texto_x, texto_y)
    
    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()