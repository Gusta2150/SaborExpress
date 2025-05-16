import os

#Essa variavel é uma maneira de criar uma lista no momento mas não armazena para sempre.
restaurantes = [{'Nome': 'Praça', 'Categoria': 'Japonesa', 'Ativo': False},
                {'Nome': 'Pizza Sub', 'Categoria': 'Italiana', 'Ativo': True},
                {'Nome': 'Burgue', 'Categoria': 'Americana', 'Ativo': False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar o estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_sub('Finalizar app')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida! \n')
    voltar_ao_menu()

def exibir_sub(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante'''

    exibir_sub('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'Nome': nome_do_restaurante, 'Categoria': categoria, 'Ativo': False}
    restaurantes.append(dados_restaurante)
    #append > é uma maneira de colocar o dados dentro da variavel fazendo uma lista

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_sub('Listando restaurantes')

    print(f'{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']
        ativo = 'Ativado' if restaurante['Ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
        
    voltar_ao_menu()

def altere_estado():
    exibir_sub('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado...')

    voltar_ao_menu()

def escolher_opcao():
    try:
    #Foi colocado 'int' pois antes ele estava passando como str, assim com 'int' ele tranforma o dado em inteiro
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()
        
        elif opcao_escolhida == 3: 
            altere_estado()       

        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            finalizar_app()
    except ValueError:
        print('Por favor, insira um número válido.')
        voltar_ao_menu()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
