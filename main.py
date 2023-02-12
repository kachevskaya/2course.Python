from class_and_def import *

text_mass_2 = mass_2
text_mass_3 = mass_3

all_cube = [cube_1, cube_2, cube_3, line_1, line_2, line_3, line_4, line_5, platform_1, platform_2, platform_3]

while True:

    pygame.time.Clock().tick(FPS)
    window.fill((255, 255, 255))

    button1 = Button(50, 200, 25, 25, color14, (128, 128, 128), "-", minus1)
    button2 = Button(150, 200, 25, 25, color14, (128, 128, 128), "+", plus1)
    button3 = Button(350, 200, 25, 25, color14, (128, 128, 128), "-", minus2)
    button4 = Button(450, 200, 25, 25, color14, (128, 128, 128), "+", plus2)
    button5 = Button(650, 200, 25, 25, color14, (128, 128, 128), "-", minus3)
    button6 = Button(750, 200, 25, 25, color14, (128, 128, 128), "+", plus3)
    button7 = Button(850, 200, 70, 70, color14, (128, 128, 128), "Return", return_)

    for event in pygame.event.get():  # Проверка события
        if event.type == pygame.QUIT:
            pygame.quit()

    if cube_3.y < 830:
        cube_3.move_ip(0, ax3)      # Цикл изменения позиции у cube_3
        line_5.height += 1
    elif cube_3.y > 705:
        cube_3.move_ip(0, 0)

    if cube_2.x > 690:
        cube_2.move_ip(-ax2, 0)  # Цикл изменения позиции у cube_2
        if line_2.width + line_2.x > 790:
            line_2.width -= 1

    if cube_1.x < 260:
        cube_1.move_ip(ax1, 0)  # Цикл изменения позиции у cube_1
        if line_4.x < 280:
            line_4.width -= 1
            line_4.x += 1

    elif cube_1.x > 260:
        cube_1.move_ip(0, 0)

    all_button = [button1, button2, button3, button4, button5, button6, button7]
    all_string = [platform_1, platform_2, platform_3, line_1, line_2, line_3, line_4,
                  line_5]

    for button in all_button:   #Отрисовка всех кнопок
        button.draw()

    for g in all_cube:
        pygame.draw.rect(window, color14, g)   #Отрисовка кубов
    draw_text("Масса 1", 75, 170, (128, 128, 128))
    draw_text("Масса 2", 375, 170, (128, 128, 128))
    draw_text("Масса 3", 675, 170, (128, 128, 128))
    pygame.draw.circle(window, color14, circle_1, 20)  # Отрисовка кругов
    pygame.draw.circle(window, color14, circle_2, 40)
    pygame.display.update()
    pygame.display.flip()
