from models.calcular import Calcular


def main() -> None:
    print('Bem-vindo ao Math Game!\nO jogo possui quatro níveis de dificuldade (1 a 4) e cada acerto te garante '
          'pontos de acordo com a dificuldade selecionada.')
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade = None
    while True:
        try:
            dificuldade = int(input('\nInforme o nível de dificuldade desejado [1, 2, 3 ou 4]: '))
            x = 0
        except ValueError:
            print('O valor precisa ser numérico.')
            x = 1
        if x == 0 and dificuldade != 1 and dificuldade != 2 and dificuldade != 3 and dificuldade != 4:
            print('O valor precisa ser 1, 2, 3 ou 4.')
        elif x == 0 and (dificuldade == 1 or dificuldade == 2 or dificuldade == 3 or dificuldade == 4):
            break

    calc: Calcular = Calcular(dificuldade)

    print('\nInforme o resultado para a seguinte operação:')

    resultado = 0
    while True:
        try:
            calc.mostrar_operacao()
            resultado: int = int(input())
            x = 0
        except ValueError:
            print('O valor precisa ser numérico.')
            x = 1
        if x == 0:
            break

    if calc.checar_resultado(resultado):
        if calc.dificuldade == 1:
            pontos += 1
        elif calc.dificuldade == 2:
            pontos += 2
        elif calc.dificuldade == 3:
            pontos += 3
        else:
            pontos += 4
    print(f'\nVocê tem {pontos} ponto(s).')

    continuar = 0
    while True:
        try:
            continuar: int = int(input('Deseja continuar no jogo? [1 - Sim | 0 - Não] '))
            x = 0
        except ValueError:
            print('O valor precisa ser numérico.')
            x = 1
        if x == 0 and continuar != 0 and continuar != 1:
            print('O valor precisa ser 0 ou 1.')
        elif x == 0 and (continuar == 0 or continuar == 1):
            break

    if continuar:
        jogar(pontos)
    else:
        print(f'\nVocê finalizou com {pontos} ponto(s).\nAté a próxima!')


if __name__ == '__main__':
    main()
