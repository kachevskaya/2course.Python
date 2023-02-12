import pygame

pygame.init()
line_1 = pygame.Rect(500, 355, 2, 70)
line_2 = pygame.Rect(625, 435, 225, 2)
line_3 = pygame.Rect(500, 395, 125, 2)
line_4 = pygame.Rect(200, 473, 424, 2)                      # Недвижущиеся платформы
line_5 = pygame.Rect(480, 415, 2, 250)
platform_1 = pygame.Rect(0, 500, 370, 5)
platform_2 = pygame.Rect(670, 500, 350, 5)
platform_3 = pygame.Rect(400, 350, 200, 5)

Height, Wight = 1000, 1000  # Размеры окна

FPS = 30 #Кол-во кадров в секунду

mass_1 = 2
mass_2 = 4  # Массы объектов
mass_3 = 1

window = pygame.display.set_mode((Height, Wight))

g = 10  # Ускорение свободного падения

dt = 0
dt += 25

x1, y1 = 100, 450
cube_1 = pygame.Rect(x1, y1, 100, 50)
x2, y2 = 850, 400
cube_2 = pygame.Rect(x2, y2, 100, 100)  # Размеры объектов
x3, y3 = 455, 665
cube_3 = pygame.Rect(x3, y3, 50, 50)

font = pygame.font.Font('C:\Windows\Fonts\Verdana.ttf', 20) #Шрифт и его размер

circle_1 = (500, 415)
circle_2 = (625, 435)  # Круги

color14 = (0, 0, 0)

ax1 = (((2 * mass_3 * (4 * mass_1 + mass_2) * (mass_3 + mass_1) * g) / (
            mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3)) - mass_3 * g + (
                   (g * mass_3 * (4 * mass_1 + mass_2)) / (
                       mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3))) / dt
ax2 = (((2 * mass_3 * (4 * mass_1 + mass_2) * (mass_3 + mass_1) * g) / (
            mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3)) - mass_3 * g) / dt
ax3 = ((g * mass_3 * (4 * mass_1 + mass_2)) / (mass_1 * mass_2 + mass_2 * mass_3 + 4 * mass_1 * mass_3)) / 5.1
