from DLS import *

# Класс кнопки
class Button:
    global mass_1, mass_2, mass_3

    def __init__(self, x, y, height, width, color, color1=None, text="", ancient=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text

        if ancient is not None:
            self.ancient = ancient
        if color1 is not None:
            self.color1 = color1
        self.pos = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed(3)

    def draw(self):
        if self.x < self.pos[0] < self.x + self.height and self.y < self.pos[1] < self.y + self.width and self.mouse[0] == True:

            pygame.draw.rect(window, self.color, (self.x, self.y, self.height, self.width))
            text = pygame.font.Font(None, 30).render(self.text, False, self.color1)
            window.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
            self.ancient()
        else:
            pygame.draw.rect(window, self.color1, (self.x, self.y, self.height, self.width))
            text1 = pygame.font.Font(None, 30).render(self.text, False, self.color)
            window.blit(text1, (
            self.x + (self.width / 2 - text1.get_width() / 2), self.y + (self.height / 2 - text1.get_height() / 2)))
            gr = font.render(str(mass_1), None, (128, 128, 128))
            window.blit(gr, ((60 + 50), (200)))
            gr = font.render(str(mass_2), None, (128, 128, 128))
            window.blit(gr, ((360 + 50), (200)))
            gr = font.render(str(mass_3), None, (128, 128, 128))
            window.blit(gr, ((660 + 50), (200)))
    #Функция отрисовки кнопок



def plus1():
    global mass_1
    if pygame.mouse.get_pressed()[0]:
        mass_1 += 1
        if mass_1 > 30:
            mass_1 = 30
        gr = font.render(str(mass_1), True, (128, 128, 128))
        window.blit(gr, ((60 + 50), (200)))
        pygame.time.delay(150)
#Функция увеличения массы 1

def minus1():
    global mass_1
    if pygame.mouse.get_pressed()[0]:
        mass_1 -= 1
        if mass_1 < 1:
            mass_1 = 1
        gr = font.render(str(mass_1), True, (128, 128, 128))
        window.blit(gr, ((60 + 50), (200)))
        pygame.time.delay(150)
#Функция уменьшения массы 1

def plus2():
    global mass_2
    if pygame.mouse.get_pressed()[0]:
        mass_2 += 1
        if mass_2 > 30:
            mass_2 = 30
        gr = font.render(str(mass_2), True, (128, 128, 128))
        window.blit(gr, ((360 + 50), (200)))
        pygame.time.delay(150)
#Функция увеличения массы 2

def minus2():
    global mass_2
    if pygame.mouse.get_pressed()[0]:
        mass_2 -= 1
        if mass_2 < 1:
            mass_2 = 1
        gr = font.render(str(mass_2), True, (128, 128, 128))
        window.blit(gr, ((360 + 50), (200)))
        pygame.time.delay(150)
#Функция уменьшение массы 2

def plus3():
    global mass_3
    if pygame.mouse.get_pressed()[0]:
        mass_3 += 1
        if mass_3 > 30:
            mass_3 = 30
        gr = font.render(str(mass_3), True, (128, 128, 128))
        window.blit(gr, ((660 + 50), (200)))
        pygame.time.delay(150)
#Функция увеличения массы 3

def minus3():
    global mass_3
    if pygame.mouse.get_pressed()[0]:
        mass_3 -= 1
        if mass_3 < 1:
            mass_3 = 1
        gr = font.render(str(mass_3), True, (128, 128, 128))
        window.blit(gr, ((660 + 50), (200)))
        pygame.time.delay(150)
#Функция уменьшение массы 3

def return_():
    global cube_3, cube_2, cube_1, ax1, ax2, ax3, mass_1, mass_2, mass_3
    if pygame.mouse.get_pressed()[0]:
        cube_3.y = 665
        cube_2.x = 850
        cube_1.x = 100
        line_2.width = 225
        line_4.x = 200
        line_4.width = 424
        line_5.height = 250
        ax1 = (((2 * mass_3 * (4 * mass_1 + mass_2) * (mass_3 + mass_1) * g) /
                (mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3)) - mass_3 * g + (
                       (g * mass_3 * (4 * mass_1 + mass_2)) / (
                       mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3))) / dt
        ax2 = (((2 * mass_3 * (4 * mass_1 + mass_2) * (mass_3 + mass_1) * g) / (
                mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3)) - mass_3 * g) / dt
        ax3 = ((g * mass_3 * (4 * mass_1 + mass_2)) / (mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3)) / 5.1
        print(mass_1, mass_2, mass_3)
        print(ax1, ax2, ax3)
#Функция возврата на начальную позицию всех объектов

def draw_text(text, x, y, color):
    gr = font.render(str(text), None, color)
    window.blit(gr, (x, y))

