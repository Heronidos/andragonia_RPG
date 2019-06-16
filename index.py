import random
import sys
import time
#Status de NPC's e player:
# HP, ATK, DEF, MAGI e INICIATIVA
player = [12, 3, 4, 0, 5, 0]
ciclope = [17, 4, 5, 0, 7]
lobisomem = [13, 6, 5, 0, 7]
elemental = [15, 4, 7, 2, 7]
cont_boss = [0, 0, 0]
cont_mercy = [0, 0, 0]
cont_lugar_passagem = [0, 0, 0]
escolha = ''

# HP -  (12 + 2)
# DEF - (5 + 2)

def validador_3(a, b, c):
    escolha = ''
    while escolha != a and escolha != b and escolha != c and escolha is not None:
        escolha = int(input())
        if escolha != a and escolha != b and escolha != c and escolha is not None:
            print('OPÇÃO INVÁLIDA!!!')
    return escolha
def validador_2(a, b):
    escolha = ''
    while escolha != a and escolha != b and escolha is not None:
        escolha = int(input())
        if escolha != a and escolha != b and escolha is not None:
            print('OPÇÃO INVÁLIDA!!!')
    return escolha

def validador_choice(x,y):
    choice = ''
    while choice != x and choice != y and choice is not None:
        choice = int(input('>>>> '))
        if choice != x and choice != y and choice is not None:
            print('OPÇÃO INVÁLIDA!!!')
    return choice

def logar():
    stts = []
    cont_boss = []
    escolha = int
    cont_lugar = []
    choice = int
    #retorna o stts do personagem e o local onde ele estava
    arq_stts = open('save_stts.txt', 'r')
    stts_temporario = arq_stts.readlines()
    for linha in range(len(stts_temporario)):
        if linha == 5:
            escolha = int(stts_temporario[linha])
        else:
            stts.append(int(stts_temporario[linha]))
    #retorna se o jogador já matou tais monstros
    arq_cont = open('save_cont.txt', 'r')
    stts_temporario = arq_cont.readlines()
    for linha in stts_temporario:
        cont_boss.append(int(linha))
    arq_stts.close()
    #retorna se o jogador já passou pelo local e ...
    arq_lugar = open('save_lugar.txt', 'r')
    stts_temporario = arq_lugar.readlines()
    for linha in range(len(stts_temporario)):
        if linha == 3:
            choice = int(stts_temporario[linha])
        else:
            cont_lugar.append(int(stts_temporario[linha]))




    return [stts, cont_boss, escolha, cont_lugar, choice]
def salvar(stts, cont_boss, escolha, cont_lugar_passagem, choice):
    save_stts = [str(stts[0]) + '\n', str(stts[1]) + '\n', str(stts[2]) + '\n', str(stts[3]) + '\n', str(stts[4]) + '\n', str(escolha)]
    save_cont_boss = [str(cont_boss[0]) + '\n', str(cont_boss[1]) + '\n', str(cont_boss[2])]
    save_lugar_passagem = [str(cont_lugar_passagem[0]) + '\n', str(cont_lugar_passagem[1]) + '\n', str(cont_lugar_passagem[2]) + '\n', str(choice)]

    arq_stts = open('save_stts.txt', 'w')
    arq_stts.writelines(save_stts)
    arq_stts.close()

    arq_cont = open('save_cont.txt', 'w')
    arq_cont.writelines(save_cont_boss)
    arq_cont.close()

    arq_stts = open('save_lugar.txt', 'w')
    arq_stts.writelines(save_lugar_passagem)
    arq_stts.close()

def escolhaFunction():
    print('Qual caminho escolhe?')
    escolha = input('>>> ')
    return escolha
def mostra(texto, velocidade):
    texto = texto
    for l in texto:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(velocidade)
def acaoPrimaria():
    print('''O que você faz?
[ 1 ] - Atacar
[ 2 ] - Observar oponente
''')
    acao2 = input('>>>')
    return acao2
def acaoRevidar():
    print('''O que você faz?
[ 1 ] - Atacar
[ 2 ] - Defender
[ 3 ] - Esquiva''')
    acao2 = input('>>>')
    return acao2
def mostrarHP(stts1, stts2):
    print('▀' * 22)
    print('HP do Player: {}.'.format(stts1[0] * '♥'))
    print('HP do Chefe: {}.'.format(stts2[0] * '♥'))
    print('▀' * 22)
def battleMecanism(stts1, stts2, nomeChefe, nomePlayer, escolha):
    esquiva = 3
    esquivaChefe = 4
    rodada = 1
    while True:
        print('Rodada {}\n'.format(rodada))
        if stts1[0] <= 0 or stts2[0] <= 0:
            if stts1[0] > stts2[0]:
                print('Parabéns, você derrotou {}!!!'.format(nomeChefe.upper()))
                if cont_boss[0] + cont_boss[2] == 1:
                    stts1[0] = 14
                elif cont_boss[0] + cont_boss[2] == 2:
                    stts1[0] = 16
                else:
                    stts1[0] = 12
                return 1
                break
            else:
                resposta = ''
                while resposta != 'S' and resposta != 'N' and resposta is not None:
                    resposta = (input('Quer tentar de novo, {}?(S/N) '.format(nomePlayer))).upper()
                    if resposta != 'S' and resposta != 'N' and resposta is not None:
                        print('OPÇÃO INVÁLIDA!!!')
                if resposta == 'S':
                    stts2[0] = 15
                    stts1[0] = 13
                    esquiva = 3
                    esquivaChefe = 4
                    rodada = 1
                else:
                    print('VOCÊ PERDEU!!!')
                    exit()

        iniciativa1 = stts1[4] + random.randint(1, 20)
        iniciativa2 = stts2[4] + random.randint(1, 20)

        if iniciativa2 > iniciativa1:
            print('''▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
O {} teve a iniciativa.
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀           
'''.format(nomeChefe))
            print('O {} vai atacar.'.format(nomeChefe))
            acao2 = 0
            while acao2 != '1' and acao2 != '2' and acao2 != '3' and acao2 is not None:
                acao2 = acaoRevidar()
                if acao2 != '1' and acao2 != '2' and acao2 != '3' and acao2 is not None:
                    print('OPÇÃO INVÁLIDA!!!')

            if acao2 == '1':
                iniciativa1 = random.randrange(20) + stts1[1]
                iniciativa2 = random.randrange(20) + stts2[1]
                print('Vocês se atacaram:')
                if iniciativa1 > iniciativa2:
                    print('E os dois conseguiram acertar os ataques.')
                    stts1[0] = stts1[0] - stts2[1]
                    stts2[0] = stts2[0] - (stts1[1] - 1)
                else:
                    print('Mas só o {} conseguiu acertar o ataque.'.format(nomeChefe))
                    stts1[0] = stts1[0] - stts2[1]

            elif acao2 == '2':# Se ação for 2 - Defender
                print('{} defendeu o ataque.'.format(nomePlayer))
                if stts2[1] > stts1[2]:# Se ATK do inimigo maior que DEF do player acontece ->
                    stts1[0] = stts1[0] - (stts2[1] - stts1[2])# -> HP do player recebe ele mesmo menos a subtração entre ATK do inimigo e sua DEF
            elif acao2 == '3':# Se ação for 3 - Esquivar
                if esquiva > 0:
                    print('{} conseguiu esquivar.'.format(nomePlayer))
                    iniciativa2 = random.randrange(20)
                    iniciativa1 = random.randrange(20)
                    if iniciativa2 > iniciativa1:
                        print('{} se machucou ao tentar te acertar.'.format(nomeChefe))
                        stts2[0] = stts2[0] - random.randrange(3)
                    else:
                        print('{} mal consegue ver o movimento de {}.'.format(nomeChefe, nomePlayer))
                    esquiva -= 1
                else:
                    print('{} NÃO PODE MAIS ESQUIVAR!!!'.format(nomePlayer.upper()))
                    print('{} acertou seu ataque'.format(nomeChefe))
                    stts1[0] = stts1[0] - (stts2[1] + 1)
        else:
            print('''▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Você teve a iniciativa.
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
            acao = 0
            while acao != '1' and acao != '2' and acao is not None:
                acao = acaoPrimaria()
                if acao != '1' and acao != '2' and acao is not None:
                    print('OPÇÃO INVÁLIDA!!!')

            if acao == '1':
                print('Você atacou o {}'.format(nomeChefe))
                acaoChefe = random.randint(1, 3)

                if acaoChefe == 1:
                    iniciativa1 = random.randint(1, 20) + stts1[1]
                    iniciativa2 = random.randint(1, 20) + stts2[1]
                    print('{} tentou revidar:'.format(nomeChefe))
                    if iniciativa1 < iniciativa2:
                        print('E os dois conseguiram acertar os ataques.')
                        stts1[0] = stts1[0] - (stts2[1] - 1)
                        stts2[0] = stts2[0] - stts1[1]
                    else:
                        print('Mas só você conseguiu acertar o ataque.')
                        stts2[0] = stts2[0] - stts1[1]
                elif acaoChefe == 2:# Se ação for 2 - Defender
                    print('{} defendeu o ataque.'.format(nomeChefe))
                    if stts1[1] > stts2[2]:# Se ATK do inimigo maior que DEF do player acontece ->
                        stts2[0] = stts2[0] - (stts1[1] - stts2[2])# -> HP do player recebe ele mesmo menos a subtração entre ATK do inimigo e sua DEF

                elif acaoChefe == 3:# Se ação for 3 - Esquivar
                    if esquivaChefe > 0:
                        print('{} conseguiu esquivar.'.format(nomeChefe))
                        iniciativa2 = random.randrange(20)
                        iniciativa1 = random.randrange(20)
                        if iniciativa2 > iniciativa1:
                            print('{} se machucou ao tentar acertar o {}.'.format(nomePlayer, nomeChefe))
                            stts1[0] = stts1[0] - random.randint(1, 2)
                        else:
                            print('{} mal consegue ver os movimentos do {}.'.format(nomePlayer, nomeChefe))
                        esquivaChefe -= 1
                    else:
                        print('{} NÃO PODE MAIS ESQUIVAR!!!'.format(nomeChefe.upper()))
                        print('{} acerta seu ataque!'.format(nomePlayer))
                        stts2[0] = stts2[0] - (stts1[1] + 1)
            else:
                print('{} observa o {} e percebe suas habilidades:'.format(nomePlayer, nomeChefe))
                print('''▀▀▀▀▀▀▀
HP: {}
ATK: {}
DEF: {}
MAGI: {}
▀▀▀▀▀▀▀
'''.format(stts2[0], stts2[1], stts2[2], stts2[3]))
        mostrarHP(stts1, stts2)
        rodada = rodada + 1
def mostraHistoria():
    text='''
Andragonia RPG - Game
=====================
Andragonia, esse era o nome de um reino que fora
esquecido pelos Deuses e Titãs e conquistado por humanos.
Nesse mundo, o rei recebeu o maior presente desejado por um pai,
receber em suas mãos seu filho.
Porém esse não recebeu apenas um filho, mas dois,
que receberam os nomes de Galand de Grance e Leo de Grance,
respectivamente o mais velho e o mais novo.
Cresceram como duas crianças saudáveis.
Correndo, brincando e lutando.
Desde muito jovens foram instruídos que seriam rivais
e que ganharia aquele mais forte e corajoso.
O tempo passou e todos do reino notavam o glamour e
honra que Galand ganhava e cada vez que derrubava Leo,
ele tornava-se mais e mais forte.
Mais orgulhoso. 
Mais destemido. 
Mais próximo de ser o possível rei de Andragonia como seu pai desejava. 
Porém, Leo não queria ser jogado para debaixo do tapete,
e sempre voltava para uma revanche com o irmão mesmo com mais de 500 derrotas ou além dos números... 
O previsto aconteceu e o irmão mais velho, Galand recebeu a coroa que tanto almejava, e fora coroado o novo rei.
Entretanto, Leo não aceitava que esse título fosse de seu irmão, pois queria aquilo mais que qualquer um.
Revoltado, abandona a cidade em busca de poder para conseguir vencer o seu irmão e retomar o lugar que deveria lhe pertencer.

===================================================================================

Jovem Leo prepara uma mochila de suprimentos e abandona o reino,
sem falar para ninguém seus objetivos.
Segue para o norte em busca de tal poder. 
Nas montanhas que sempre via de sua janela,
encontra um monge meditando com um capacete azulado em sua cabeça, chamado Lung Kao,
que escuta sua história e lhe diz que sabe como conseguir tamanho poder.

Leo vê que aquela é sua oportunidade, e a agarra com força. 
A partir de então passa a treinar todos os dias durante muito tempo com o Lung,
até superar o seu mestre que já não tem mais nada a lhe ensinar, e por fim diz:
 - Meu jovem Leo, você já me ultrapassou faz tempos. É hora de provar a si mesmo que pode conseguir o que deseja, receba isso. 
Ele estende o capacete azulado com marcas douradas em direção ao jovem.
 - Pegue-o e supere a mim e a si mesmo.
Leo recebe o capacete e logo o põe em sua cabeça,
e escuta as últimas palavras de seu mestre que está indo embora seguir um novo caminho montanha abaixo.
 - Existem três criaturas, uma ao noroeste, outra ao norte e por fim uma ao nordeste. 
 - Vença-as e assim está pronto para qualquer desafio. 
'''
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
def play(cont_boss, escolha, choice):
    bla = '''Você corre para onde? '''
    atk_fug = ''' 
--------------------
 [ 1 ] - Batalhar
 [ 2 ] - Fugir
--------------------'''
    inicial_lugar = '''
-----------------------------------
  Você está na Montanha Solitária
-----------------------------------
[ 1 ] - Caminho dos Corvos - [ ↖ ]
[ 2 ] - Árvore Quebrada - [ ↑ ]
[ 3 ] - Caminho das Runas - [ ↗ ]
-----------------------------------'''
    ciclope_lugar = '''
------------------------------
  Você está em Gigante Bones
------------------------------
Em sua frente encontra-se
um terrível Ciclope
------------------------------
'''
    ciclope_lugar_final = '''-------------------------------
[ 1 ] - Estrada do Javali Morto - [ → ]
[ 2 ] - Caminho dos Corvos - [ ↘ ]
-------------------------------'''
    lobisomem_lugar = '''
-----------------------------
  Você está em Blood Spikes
-----------------------------
Em sua frente encontra-se
um Lobisomem Atroz
-------------------------'''
    lobisomem_lugar_final = '''-------------------------------
[ 1 ] - Estrada do Javali Morto - [ ← ]
[ 2 ] - Cinzas - [ → ]
[ 3 ] - Árvore Quebrada - [ ↓ ]
-------------------------------'''
    elemental_lugar = '''
-------------------------
  Você está em LavaLake
-------------------------
Em sua frente encontra-se 
o Sr.Elemental Derretido
-------------------------'''
    elemental_lugar_final = '''-------------------------------
[ 1 ] - Cinzas - [ ← ]
[ 2 ] - Caminho das Runas - [ ↙ ]
-------------------------------'''
    pacifista_run = '''
Leo retornava a Montanha Solitária, lar de seu mestre Lung Kao. Sentindo-se de mãos vazias,
o corpo frustado, e o capacete em mãos. Descobrindo que aquele não era o destino que desejava
treinar tanto, para superar seu irmão a troco da vida daquelas criaturas? As coisas não podiam
ser desse jeito, algo dentro de si não permitia tal coisa. Virando seu olhar chateado e confuso 
para encarar o seu mestre em sua frente, Leo diz:

 -Mestre, peço-lhe perdão. Não sou digno de tais atrocidades, não consegui encarar aquelas 
criaturas nos olhos e tentar, tomar-lhes a vida que possuíam. Eles não merecem esse destino
apenas para que eu me torne forte. Eu..... não.... sou digno de ser um rei.

O mestre, ao contrário do que esperava, sorriu orgulhoso:

 -Não, pequeno Leo. Eu o treinei, não para derrotar a todos que encontrasse, tinha até lhe concedido
mais poder com o uso desse capacete. Mas visto que você superou o sentimento que o corrompia por 
dentro, você me orgulha e deve ter orgulho de si mesmo. Sua arma está além de da força, do poder ou 
da glória, está dentro de você. Agora vá e retome o que é seu por direito, o trono de Andragonia, pois
você, Leo de Grace, está preparado.

Ao final da última palavra, Kao. Transforma-se em uma pássaro brilhante e desaparece nas nuvens brancas.'''
    pacifista_run_final = '''
Com o ar renovado dentro de si, e partindo em rumo a Estrada Real. Podia ver os portões de sua terra, aguardando sua entrada. 
Porém lá, podia ver uma forma não muito estranha, era ele Galand de Grace, seu irmão e seu rival.
Que o esperava sozinho e paciente. Apenas falou quando Leo chegou perto.

 -Leo, Leo. Por onde esteve, estávamos todos preocupados com você. Por onde andava? Vamos para casa.

Algo tomou conta de Leo nesse momento, e ele rebateu dizendo:

 -Irmão, sei que você já me derrotou muitas vezes, mas estou aqui para provar que te venço, e que 
me tornei mais forte que ti.

 -Ora, ora.... - disse Galand surpreso - E acha que consegue tal proeza? Vem e me prova isso.

Leo foi para cima de Galand e num embate frenético ambos notaram que estavam tendo 
uma luta muito equilibrada e árdua a ambos. Leo conhecia cada movimento do irmão, mas 
a força dele ainda era um pouco superior a sua, o que comprometeria o decorrer do duelo.
Por fim, Galand consegue derrubar seu irmão que estava quase esgotado naquela situação.
E apontado para ele Galand disse:

 -Pela útima vez eu ganh....

Antes de completar sua última palavra. Criaturas pularam a sua frente e começaram a confrontá-lo
não conseguia enfrentá-las e nem saber de onde elas vinham, apenas sabia que ali ele perdeu. Ao 
cair no chão e erguer o olhar para frente, viu Leo andando em meio a elas, como se as 
conhecesse, e apontando a arma para o irmão disse:

 -Dessa vez, a vitória é minha.'''

    #Cont_Ciclope, Cont_Lobisomem, Cont_Elemental
    cont_lugar_passagem_ciclope = cont_lugar_passagem_lob = cont_lugar_passagem_ele = 0
    contador = 0

    #mostraHistoria()

    if menu == 1:
        print(inicial_lugar)
        while escolha != '1' and escolha != '2' and escolha != '3' and escolha is not None:
            escolha = str(escolhaFunction())
            if escolha != '1' and escolha != '2' and escolha != '3' and escolha is not None:
                print('OPÇÃO INVÁLIDA!!!')


    escolha = int(escolha)
    escolha_4 = int
    while True:

        if escolha_4 == 4:
            escolha = 4
        if escolha == 0:
            if cont_boss == [1, 1, 1] :
                print('''
--------------------------------
  Você está Montanha Solitária
--------------------------------
[ 1 ] - Caminho dos Corvos - [ ↖ ]
[ 2 ] - Árvore Quebrada - [ ↑ ]
[ 3 ] - Caminho das Runas - [ ↗ ]
[ 4 ] - Estrada Real - [ ↓ ]
--------------------------------''')

                escolha = int(input('>>> '))

            if cont_boss == [2, 2, 2]:

                print('''
--------------------------------
  Você está Montanha Solitária
--------------------------------
[ 1 ] - Caminho dos Corvos - [ ↖ ]
[ 2 ] - Árvore Quebrada - [ ↑ ]
[ 3 ] - Caminho das Runas - [ ↗ ]
[ 4 ] - Estrada Real - [ ↓ ]
--------------------------------''')

                escolha = int(input('>>> '))

            elif cont_boss != [1, 1, 1]:

                print('''
--------------------------------
  Você está Montanha Solitária
--------------------------------
[ 1 ] - Caminho dos Corvos - [ ↖ ]
[ 2 ] - Árvore Quebrada - [ ↑ ]
[ 3 ] - Caminho das Runas - [ ↗ ]
--------------------------------''')
                escolha = validador_3(1, 2, 3)

        cont_lugar_passagem_ciclope = cont_boss[0]


        if escolha == 1:
            if cont_lugar_passagem_ciclope == 0 and cont_lugar_passagem[0] == 0:
                print(ciclope_lugar)
                time.sleep(3)
                print('''
           .......
        .-'.'.'.'.'.'.`-.
      .'.'.'.'.'.'.'.'.'.`.
     /.'.'               '.
     |.'    .--...--.     |
     \    `..-.....-..'   /
     |     ..- .-. -..   |
  .-.'    `.   ((@))  .'   '.-.
 ( ^ \      `--.   .-'     / ^ )
  \  /         .   .       \  /
  /          .'     '.  .-    
 ( .\    \ (`-..-')    /._\)
  `-' \   ' .--.          / `-'
      |  / /|| `-..'\   |
      |   |       || |   /-..
  ..-\   `.--.___.'  |
       \       .....     |
        `.  .'      `.  /
          \           .'
       `-.._..-`''')
                time.sleep(1.5)
                print(atk_fug)
                choice = int(input('>>>> '))
                cont_lugar_passagem_ciclope +=1
                cont_lugar_passagem[0] = 1
                salvar(player, cont_boss, escolha, cont_lugar_passagem, choice)



            else:
                print('Agora você encontra apenas rastros de grandes passos, nada além disso.')
                print(ciclope_lugar_final)
                escolha_1 = validador_2(1, 2)
                if escolha_1 == 1:
                    escolha = 2
                elif escolha_1 == 2:
                    escolha = 0
                cont_boss[0] = cont_lugar_passagem_ciclope


            salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)

        if escolha == 2:
            if cont_lugar_passagem_lob == 0 and cont_lugar_passagem[1] == 0:
                print(lobisomem_lugar)
                time.sleep(3)
                print('''
     __
                            .d$$b
                          .' TO$;
                         /  : TP._;
                        / _.;  :Tb|
                       /   /   ;j$j
                   _.-"       d$$$$
                 .' ..       d$$$$;
                /  /P'      d$$$$P. |
               /   "      .d$$$P' |\^"l
             .'           `T$P^"""""  :
         ._.'      _.'                ;
      `-.-".-'-' ._.       _.-"    .-"
    `.-" __  .              .-"
   -(.g$$$$$$$b.              .'
     ""^^T$$$P^)            .(:
       _/  -"  /.'         /:/;
    ._.'-'`-'  ")/         /;/;
 `-.-"..--""   " /         /  ;
.-" ..--""        -'          :
..--""--.-"         (\      .-(
  ..--""              `-\(\/;`
    _.                      :
                            ;`-
                           :''')
                time.sleep(1.5)
                print(atk_fug)
                choice = int(input('>>>> '))
                cont_lugar_passagem_lob += 1
                cont_lugar_passagem[1] = 1
                salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)


            else:
                print('Agora você encontra carne estraçalhada no chão, com marcas de garras profundas.')
                print(lobisomem_lugar_final)
                escolha_2 = validador_3(1, 2, 3)

                if escolha_2 == 1:
                    escolha = 1
                elif escolha_2 == 2:
                    escolha = 3
                elif escolha_2 == 3:
                    escolha = 0

            salvar(player, cont_boss, escolha, cont_lugar_passagem, choice)

        if escolha == 3:
            if cont_lugar_passagem_ele == 0 and cont_lugar_passagem[2] == 0:
                print(elemental_lugar)
                time.sleep(3)
                print('''
          (
            .            )        )
                     (  (|              .
                 )   )\/ ( ( (
         *  (   ((  /     ))\))  (  )    )
       (     \   )\(          |  ))( )  (|
       >)     ))/   |          )/  \((  ) 
       (     (      .        -.     V )/   )(    (
        \   /     .   \            .       \))   ))
          )(      (  | |   )            .    (  /
         )(    ,'))     \ /          \( `.    )
         (\>  ,'/_      ))            _`.  /
        ( \   | /  _   ( \/     _   \ | ( (
         \.)  |/  /   \__      __/   \   \|  ))
        .  \. |>  \      | __ |      /   <|  /
             )/    \__/ :..: \__/     \ <
      )   \ (|_  .      / ;: \          _| )  (
     ((    )\)  --_     --  --      _--    /  ))
      \    (    |  ||               ||  |   (  /
            \.  |  ||_             _||  |  /
              > :  |  V+-I_I_I-+V  |  : (.
             (  \:  T\   _     _   /T  : ./
              \  :    T^T T-+-T T^T    ;<
               \..`_       -+-       _'  )
     )            . `--=..___..=--'. ./         (
    ((     ) (          )             (     ) (   )>
     > \/^/) )) (   ( /(.      ))     ))./())./ (.
    (  ../ ( \))    )   \ (  / \.  ./ ||  .._:|  _. 
    |  \_.  ) |   (/  /: :)) |   \/   |(  <..  )|  ) )
   ))  ./   |  )  ))  _  <  | :(     :))   .//( :  : |
   (: <     ):  --:   ^  \  )(   )\/:   /   // ) :.) :
    \..)   (..  ..  :    :  : .(   \..:..    ./_.  ./''')
                time.sleep(1.5)
                print(atk_fug)
                choice = int(input('>>>> '))
                cont_lugar_passagem_ele += 1
                cont_lugar_passagem[2] = 1
                salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)


            else:
                print('Agora você sente-se extramemente desconfortável num lugar tão quente como esse, sem vida. ')
                print(elemental_lugar_final)
                escolha_3 = validador_2(1, 2)

                if escolha_3 == 1:
                    escolha = 2
                elif escolha_3 == 2:
                    escolha = 0

            salvar(player, cont_boss, escolha, cont_lugar_passagem, choice)

        if choice == 1:

            if escolha == 4:
                print('-' * 70)
                mostra('''
Leo retorna a Montanha Solitárias, depois de ter enfrentado
todas as três criaturas assustadoras.
E lá encontra seu mestre, ao seu aguardo e o tão almejado poder em suas mãos.
Lung fala:
 
 - Vejo que conseguiu meu rapaz, e aqui está o que sempre desejou.
 
Ele estende o elmo para Leo que o recebe em suas mãos sofridas e cortadas, 
mas ansioso por aquele grande momento. 
Ao colocar em sua cabeça, percebe que agora pode, 
enfim, derrotar o seu irmão e recuperar o trono. 
Decide então retornar a Andragonia e enfrentar Galand.''', 0.05)
                print('-' * 70)
                mostra('''
No caminho de volta para o reino de Andragonia, 
Leo avista a diante seu irmão, que o encarava no fundo dos olhos e
sorria maliciosamente. 

- Leo, a quanto tempo, o que houve contigo, pequeno irmão?

Andando friamente para o irmão, Leo rebate:

- Nada, apenas voltei, para provar que te derroto. 
Não por ouro, armas ou exércitos. Apenas a vitória.

- Que seja então.

Ambos assumem postura de combate. 
Galand investe ferozmente em seu irmão como sempre fez, mas este já 
conhecia sua movimentação e rapidamente desviou. 
Um forte soco fora recebido de Galand, que passou alguns segundos 
atordoado, era evidente a evolução do irmão mais novo, que agora não desmontrava medo. 
Antes de ter tempo para 
recuperar-se, Leo avança com tudo, desferindo uma sequência de golpes em sua armadura 
que não é capaz de suportar tamanho dano. 
Agora Galand, sem armadura, sem resistência, percebe que não pode mais derrotar aquele que uma dia
sempre venceu. E usa tudo em um único golpe, saltando em fúria contra a espada de Leo que a empunha com uma 
tremenda força e nem mais esforça-se a segurá-la. 
Por fim cai no chão de joelhos, completamente derrotado. 

- Como ficou tão poderoso assim? - Pergunta Galand, cuspindo sangue.

- Tomei muitas vidas para tal. E hoje, tomo a sua.

E ele o empunhala, com a espada bebendo os últimos segundos da sua preciosa vida.''', 0.05)
                salvar(player, cont_boss, escolha, cont_lugar_passagem, choice)
                break

            elif escolha == 1:
                if cont_boss[0] == 0:
                    cont_boss[0] = battleMecanism(player, ciclope, 'Ciclope', 'Leo', escolha)
                    player[0] += 2
                    print('Após essa terrível batalha você pode ir para:')
                    print(ciclope_lugar_final)
                    escolha_1 = int(escolhaFunction())
                    if escolha_1 == 1:
                        escolha = 2
                    elif escolha_1 == 2:
                        escolha = 0
                    salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)
                    cont_lugar_passagem_ciclope += 1

            elif escolha == 2:
                if cont_boss[1] == 0:
                    cont_boss[1] = battleMecanism(player, lobisomem, 'Lobisomem', 'Leo', escolha)
                    player[1] += 2
                    print('Após essa terrível batalha você pode ir para:')
                    print(lobisomem_lugar_final)
                    escolha_2 = int(escolhaFunction())
                    if escolha_2 == 1:
                        escolha = 1
                    elif escolha_2 == 2:
                        escolha = 3
                    elif escolha_2 == 3:
                        escolha = 0
                    cont_lugar_passagem_lob += 1
                    salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)

            elif escolha == 3:
                if cont_boss[2] == 0:
                    cont_boss[2] = battleMecanism(player, elemental, 'Elemental', 'Leo', escolha)
                    player[0] += 2
                    player[2] += 2
                    player[3] += 2
                    print('Após essa terrível batalha você pode ir para:')
                    print(elemental_lugar_final)
                    escolha_3 = int(escolhaFunction())
                    if escolha_3 == 1:
                        escolha = 2
                    elif escolha_3 == 2:
                        escolha = 0



                    cont_lugar_passagem_ele += 1
                    salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)


        if choice == 2:
            if escolha == 4:
                print('-' * 70)
                mostra(pacifista_run,0.05)
                print()
                print('-' * 70)
                mostra(pacifista_run_final,0.05)
                print()

                break


            if escolha == 1:


                print('Você abandona a batalha, deixando a criatura confusa.')
                cont_lugar_passagem_ciclope += 1
                cont_boss[0] = cont_lugar_passagem_ciclope
                cont_mercy[0] = 1
                print(bla)
                print(ciclope_lugar_final)
                escolha_1 = validador_2(1, 2)

                if escolha_1 == 1:
                    escolha = 2
                elif escolha_1 == 2:
                    escolha = 0

                salvar(player, cont_boss, escolha, cont_lugar_passagem, choice)

            elif escolha == 2:
                print('Você abandona a batalha, deixando a criatura confusa.')
                cont_lugar_passagem_lob += 1
                cont_boss[1] = cont_lugar_passagem_lob
                cont_mercy[1] = 1
                print(bla)
                print(lobisomem_lugar_final)
                escolha_2 = validador_3(1, 2, 3)

                if escolha_2 == 1:
                    escolha = 1
                elif escolha_2 == 2:
                    escolha = 3
                elif escolha_2 == 3:
                    escolha = 0

                salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)

            elif escolha == 3:
                print('Você abandona a batalha, deixando a criatura confusa.')
                cont_lugar_passagem_ele += 1
                cont_boss[2] = cont_lugar_passagem_ele
                cont_mercy[2] = 1
                print(bla)
                print(elemental_lugar_final)
                escolha_3 = validador_2(1, 2)

                if escolha_3 == 1:
                    escolha = 2
                elif escolha_3 == 2:
                    escolha = 0

                salvar(player,cont_boss,escolha, cont_lugar_passagem, choice)


    print('FIM')

mostra('ANDRAGONIA RPG', 0.25)
print('''
[ 1 ] - Começar novo jogo
[ 2 ] - Continuar
[ 3 ] - Sair
''')
menu = ''
while menu != '1' and menu != '2' and menu != '3' and menu is not None:
   menu = input()
   if menu != '1' and menu != '2' and menu != '3' and menu is not None:
        print('OPÇÃO INVÁLIDA!!!')

if menu == '1':
    cont_boss = [0, 0, 0]
    escolha = 0
    choice = 0
    play(cont_boss, escolha, choice)

elif menu == '2':
    save = logar()
    player = save[0]
    cont_boss = save[1]
    escolha = save[2]
    cont_lugar_passagem = save[3]
    choice = save[4]
    play(cont_boss, escolha, choice)

elif menu == '3':
    exit()

