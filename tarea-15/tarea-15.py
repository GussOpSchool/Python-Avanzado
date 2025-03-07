import pygame, random, sys, time

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 200)
ROJO = (200, 0, 0)

ANCHO_VENTANA = 600
ALTO_VENTANA = 600
TAMCELDA = 100
OFFSETX = (ANCHO_VENTANA - (3 * TAMCELDA)) // 2
OFFSETY = (ALTO_VENTANA - (3 * TAMCELDA)) // 2

pygame.init()
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tres en Raya")
fuenteTitulo = pygame.font.Font(None, 72)
fuenteBoton = pygame.font.Font(None, 36)
fuenteFicha = pygame.font.Font(None, 100)

class Boton:
    def __init__(self, rect, texto):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.color = AZUL
        self.superficieTexto = fuenteBoton.render(texto, True, BLANCO)
        self.rectTexto = self.superficieTexto.get_rect(center=self.rect.center)
    def dibujar(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        surface.blit(self.superficieTexto, self.rectTexto)
    def esClic(self, pos):
        return self.rect.collidepoint(pos)

estado = "menu"  
modoJuego = None
tablero = [[" " for _ in range(3)] for _ in range(3)]
jugadorActual = "X"
animaciones = {}
DURACION_ANIM = 300
tiempoVictoria = None
lineaVictoria = None
tiempoIA = None

jugadorHumano = None 
letraHumano = None
letraIA = None

botonHumano = Boton((ANCHO_VENTANA//2 - 125, 250, 250, 60), "Humano vs Humano")
botonHumanoIA = Boton((ANCHO_VENTANA//2 - 125, 330, 250, 60), "Humano vs IA")

botonReiniciar = Boton((ANCHO_VENTANA//2 - 100, ALTO_VENTANA - 80, 200, 50), "Jugar Otra Vez")

def dibujarMenu():
    ventana.fill(BLANCO)
    titulo = fuenteTitulo.render("Tres en Raya", True, NEGRO)
    rectTitulo = titulo.get_rect(center=(ANCHO_VENTANA//2, 150))
    ventana.blit(titulo, rectTitulo)
    botonHumano.dibujar(ventana)
    botonHumanoIA.dibujar(ventana)

def dibujarSeleccion():
    ventana.fill(BLANCO)
    titulo = fuenteTitulo.render("Elige tu ficha", True, NEGRO)
    rectTitulo = titulo.get_rect(center=(ANCHO_VENTANA//2, 150))
    ventana.blit(titulo, rectTitulo)
    botonX = Boton((ANCHO_VENTANA//2 - 150, 250, 120, 60), "X (roja)")
    botonO = Boton((ANCHO_VENTANA//2 + 30, 250, 120, 60), "O (azul)")
    botonX.dibujar(ventana)
    botonO.dibujar(ventana)
    return botonX, botonO

def dibujarTablero():

    for fila in range(3):
        for col in range(3):
            x = OFFSETX + col * TAMCELDA
            y = OFFSETY + fila * TAMCELDA
            pygame.draw.rect(ventana, NEGRO, (x, y, TAMCELDA, TAMCELDA), 3)

def dibujarFichas():
    ahora = pygame.time.get_ticks()
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] != " ":

                tiempoInicio = animaciones.get((fila, col), None)
                if tiempoInicio is not None:
                    progreso = min(1, (ahora - tiempoInicio) / DURACION_ANIM)
                else:
                    progreso = 1

                colorFicha = ROJO if tablero[fila][col] == "X" else AZUL
                fichaTexto = fuenteFicha.render(tablero[fila][col], True, colorFicha)
                tamOriginal = fichaTexto.get_size()
                nuevoAncho = int(tamOriginal[0] * progreso)
                nuevoAlto = int(tamOriginal[1] * progreso)
                fichaEscalada = pygame.transform.smoothscale(fichaTexto, (nuevoAncho, nuevoAlto))

                x = OFFSETX + col * TAMCELDA + (TAMCELDA - nuevoAncho) // 2
                y = OFFSETY + fila * TAMCELDA + (TAMCELDA - nuevoAlto) // 2
                ventana.blit(fichaEscalada, (x, y))
                
def obtenerCasilla(pos):
    x, y = pos
    if OFFSETX <= x <= OFFSETX + 3 * TAMCELDA and OFFSETY <= y <= OFFSETY + 3 * TAMCELDA:
        fila = (y - OFFSETY) // TAMCELDA
        col = (x - OFFSETX) // TAMCELDA
        return (fila, col)
    return None

def verificarGanador():

    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    return None

def obtenerLineaGanadora():

    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            y = OFFSETY + i * TAMCELDA + TAMCELDA // 2
            inicio = (OFFSETX + 10, y)
            fin = (OFFSETX + 3 * TAMCELDA - 10, y)
            return inicio, fin
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            x = OFFSETX + i * TAMCELDA + TAMCELDA // 2
            inicio = (x, OFFSETY + 10)
            fin = (x, OFFSETY + 3 * TAMCELDA - 10)
            return inicio, fin
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        inicio = (OFFSETX + 10, OFFSETY + 10)
        fin = (OFFSETX + 3 * TAMCELDA - 10, OFFSETY + 3 * TAMCELDA - 10)
        return inicio, fin
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        inicio = (OFFSETX + 3 * TAMCELDA - 10, OFFSETY + 10)
        fin = (OFFSETX + 10, OFFSETY + 3 * TAMCELDA - 10)
        return inicio, fin
    return None

def minimax(tab, prof, esMax):
    ganador = verificarGanador()
    if ganador == letraHumano:
        return -10 + prof
    elif ganador == letraIA:
        return 10 - prof
    elif all(tab[f][c] != " " for f in range(3) for c in range(3)):
        return 0
    if esMax:
        mejor = -float("inf")
        for f in range(3):
            for c in range(3):
                if tab[f][c] == " ":
                    tab[f][c] = letraIA
                    valor = minimax(tab, prof+1, False)
                    tab[f][c] = " "
                    mejor = max(mejor, valor)
        return mejor
    else:
        mejor = float("inf")
        for f in range(3):
            for c in range(3):
                if tab[f][c] == " ":
                    tab[f][c] = letraHumano
                    valor = minimax(tab, prof+1, True)
                    tab[f][c] = " "
                    mejor = min(mejor, valor)
        return mejor

def mejorMovimiento():
    mejorVal = -float("inf")
    movimiento = None
    for f in range(3):
        for c in range(3):
            if tablero[f][c] == " ":
                tablero[f][c] = letraIA
                valor = minimax(tablero, 0, False)
                tablero[f][c] = " "
                if valor > mejorVal:
                    mejorVal = valor
                    movimiento = (f, c)
    return movimiento

def reiniciarJuego():
    global tablero, jugadorActual, animaciones, tiempoVictoria, lineaVictoria, tiempoIA
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadorActual = "X"
    animaciones = {}
    tiempoVictoria = None
    lineaVictoria = None
    tiempoIA = None

clock = pygame.time.Clock()
while True:
    if estado == "menu":
        dibujarMenu()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonHumano.esClic(evento.pos):
                    modoJuego = "humano"
                    reiniciarJuego()
                    estado = "juego"
                elif botonHumanoIA.esClic(evento.pos):
                    modoJuego = "humanoIA"
                    estado = "seleccion"
        pygame.display.flip()

    elif estado == "seleccion":
        botonX, botonO = dibujarSeleccion()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botonX.esClic(evento.pos):
                    letraHumano = "X"
                    letraIA = "O"
                    jugadorHumano = "X"
                    reiniciarJuego()

                    jugadorActual = "X"
                    estado = "juego"
                elif botonO.esClic(evento.pos):
                    letraHumano = "O"
                    letraIA = "X"
                    jugadorHumano = "O"
                    reiniciarJuego()

                    jugadorActual = "X"
                    estado = "juego"
        pygame.display.flip()

    elif estado == "juego":
        ventana.fill(BLANCO)
        dibujarTablero()
        dibujarFichas()
    
        if not verificarGanador() and any(tablero[f][c] == " " for f in range(3) for c in range(3)):
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if (modoJuego == "humano") or (modoJuego == "humanoIA" and jugadorActual == jugadorHumano):
                        casilla = obtenerCasilla(evento.pos)
                        if casilla and tablero[casilla[0]][casilla[1]] == " ":
                            tablero[casilla[0]][casilla[1]] = jugadorActual
                            animaciones[casilla] = pygame.time.get_ticks()
                            # Alterna turno
                            jugadorActual = "O" if jugadorActual == "X" else "X"
        else:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if botonReiniciar.esClic(evento.pos):
                        estado = "menu"
        
        if modoJuego == "humanoIA" and jugadorActual != jugadorHumano and not verificarGanador():
            ahora = pygame.time.get_ticks()
            if tiempoIA is None:
                tiempoIA = ahora + 300  # 300 ms de espera antes de mover
            elif ahora >= tiempoIA:
                mov = mejorMovimiento()
                if mov:
                    tablero[mov[0]][mov[1]] = letraIA
                    animaciones[mov] = pygame.time.get_ticks()
                    jugadorActual = jugadorHumano
                tiempoIA = None
        
        ganador = verificarGanador()
        if ganador or all(tablero[f][c] != " " for f in range(3) for c in range(3)):
            if not tiempoVictoria:
                tiempoVictoria = pygame.time.get_ticks()
                lineaVictoria = obtenerLineaGanadora()
            if lineaVictoria:
                ahora = pygame.time.get_ticks()
                progreso = min(1, (ahora - tiempoVictoria) / 500)
                (xi, yi), (xf, yf) = lineaVictoria
                xFinal = xi + (xf - xi) * progreso
                yFinal = yi + (yf - yi) * progreso
                pygame.draw.line(ventana, ROJO, (xi, yi), (xFinal, yFinal), 8)
            if ganador:
                mensaje = f"Ganador: {ganador}"
            else:
                mensaje = "Empate"
            mensajeTexto = fuenteTitulo.render(mensaje, True, ROJO)
            rectMensaje = mensajeTexto.get_rect(center=(ANCHO_VENTANA//2, 50))
            ventana.blit(mensajeTexto, rectMensaje)
            botonReiniciar.dibujar(ventana)
        
        pygame.display.flip()
        clock.tick(60)
