from models.Calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Selecione Dificuldade de 1 a 4: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe Resultado Da Operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} Ponto(s).')

    continuar: int = int(input('Deseja COntinuar? 1 Para S 0 Para Ñ'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Finalizou com {pontos} Pontos')
        print('See you !')

if __name__ == '__main__':
    main()

