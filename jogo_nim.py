
print('Bem-vindo ao jogo do NIM! Escolha:')
print()
print('1 - para jogar uma partida isolada')
escolha = int(input('2 - para jogar um campeonato:'))

def computador_escolhe_jogada(n,m):
    result = n % m
    if(result == 0):
        return m
    else:
        return m - 1

def usuario_escolhe_jogada(n,m):
    print()
    jogada = int(input('Quantas peças você vai tirar?'))
    while (jogada > m):
        print()
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        jogada = int(input('Quantas peças você vai tirar?'))
    return jogada

def partida():
    jogador = 0
    print()
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    resultado = n % (m + 1)
    if(resultado == 0):
        print()
        print('Você começa!')
        escolha = usuario_escolhe_jogada(n,m)
        print()
        n = n - escolha
        print('O usuário tirou',escolha,'peças')
        print('Agora restam',n,'peças no tabuleiro')
        jogador = 1
    else:
        print()
        print('Computador começa!')
        escolha = computador_escolhe_jogada(n,m)
        print()
        n = n - escolha
        print('O computador tirou',escolha,'peças')
        print('Agora restam',n,'peças no tabuleiro')
        jogador = 2
    jogada = jogador % 2
    while(n != 0):
        if(jogada == 0):
            escolha = usuario_escolhe_jogada(n,m)
            print()
            n = n - escolha
            print('O usuario tirou',escolha,'peças')
            print('Agora restam',n,'peças no tabuleiro')
            jogada = jogada + 1
        else:
            escolha = computador_escolhe_jogada(n,m)
            print()
            n = n - escolha
            print('O computador tirou',escolha,'peças')
            print('Agora restam',n,'peças no tabuleiro')
            jogada = jogada - 1
    if(jogada == 0):
        print()
        print('O computador ganhou!')
        return 1
    else:
        print()
        print('Você ganhou!')
        return 2

def campeonato():
    jogo = 1
    placarCpu = 0
    placarUser = 0
    while(jogo <= 3):
        print('**** Rodada',jogo,'****')
        resultado = partida()
        if( resultado == 1):
            placarCpu = placarCpu + 1
        else:
            placarUser = placarUser + 1
        jogo = jogo + 1
    print('Placar: Você',placarUser,'X',placarCpu,' Computador')

if (escolha == 1):
    print()
    print('Voce escolheu uma partida isolada!')
    partida()
else:
    print()
    print('Voce escolheu um campeonato!')
    campeonato()




    
        




