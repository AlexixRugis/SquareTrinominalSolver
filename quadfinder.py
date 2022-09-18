import math, re, os

def Solve(a, b, c):
    D = b*b - 4 * a * c

    print('D = ' + str(D))

    if D < 0:
        print("Дествительных корней нет")
    elif D ==0:
        print('x = ' + str(-(b/2 / a)))
    elif D > 0:
        print('x = ' + str((-b+math.sqrt(D))/2/a) + '; ' + str((-b-math.sqrt(D))/2/a))


if __name__ == '__main__':
    while True:
        os.system('cls')
        choice = input('''
           Меню:
        1-Ввести уравнение
        2-Ввести коофициенты
        3-Выход
        
        Ваш выбор: ''')
        if choice == '3':
            exit(0)
        elif choice == '2':
            os.system('cls')
            while True:
                inp = input(
                    'Пожалуйста, введите коофициенты вручную через пробел: ').split()
                try:
                    int(inp[0])
                    int(inp[1])
                    int(inp[2])
                    break
                except:
                    continue
            Solve(int(inp[0]), int(inp[1]), int(inp[2]))
            input()
        elif choice == '1':
            os.system('cls')
            inp = input("Пожалуйста, введите квадратное уравнение в стандартном виде(ax^2 + bx + c = 0): ")
            inp = inp.replace(' ', '')
            inp = ' ' + inp
            inp = re.sub(r'\-[a-zA-Z]', '-1x', inp)
            inp = re.sub(r'[\+|\s][a-zA-Z]', '+1x', inp)
            inp = re.findall(r'[\+|\-|\s]\d+', inp)

            if len(inp) != 3:
                while True:
                    inp = input('Не удалось автоматически обнаружить коофициенты. Пожалуйста, введите их вручную через пробел: ').split()
                    try:
                        int(inp[0])
                        int(inp[1])
                        int(inp[2])
                        break
                    except:
                        continue
            Solve(int(inp[0]), int(inp[1]), int(inp[2]))
            input()


