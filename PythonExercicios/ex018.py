print('\033[34m=\033[m'*12, '\033[1;33mSeno, Cosseno e Tangente\033[m', '\033[34m=\033[m'*12)
import math
angulo = float(input('\033[31mDigite o ângulo que você deseja: '))
radiano = math.radians(angulo)
seno = math.sin(radiano)
cos = math.cos(radiano)
tan = math.tan(radiano)
print('\033[4;33mO ângulo de \033[4;34m{}\033[4;33m tem o SENO de \033[4;34m{:.2f}'.format(angulo, seno))
print(f'\033[4;33mO ângulo de \033[4;34m{angulo} \033[4;33mtem o COSSENO de \033[4;34m{cos:.2f}')
print(f'\033[4;33mO ângulo de \033[4;34m{angulo} \033[4;33mtem a TANGENTE de \033[4;34m{tan:.2f}')