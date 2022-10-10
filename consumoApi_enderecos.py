import requests

def main():
    print("-"*30)
    print("---- Consulta cep ----")
    print("-"*30)
    print()

    cep_input = int(input("Digite seu cep para consulta: "))

    if len(cep_input) != 8:
        print("quantidade de digitos invalida!")
        exit()

    request = requests.get(f"https://viacep.com.br/ws/{cep_input}/json")   

    address_data = request.json()

    if 'erro' not in address_data:
        print('==== CEP ENCONTRADO! ====')
        print('CEP: {}'.format(address_data['cep']) )
        print('Logradouro:{}'.format(address_data['logradouro']))
        print('Complemento:{}'.format(address_data['complemento']))
        print('Bairro:{}'.format(address_data['bairro']))
        print('Cidade:{}'.format(address_data['localidade']))
        print('Estado:{}'.format(address_data['uf']))

    else:
        print("CEP invalido")
    
    options= int(input('Deseja realizar uma nova consulta? \n 1.Sim\n 2.Sair\n'))
    if options == 1:
        main()
    else:
        print("saindo...")

if __name__ == "__main__":
    main()
