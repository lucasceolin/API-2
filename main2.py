import requests

opcao = int(input('Você deseja realizar a busca por: [1] CEP ou [2] Endereço?'))
if opcao == 1:
    cep = input('Digite um CEP: ')
    if len(cep) < 8 or len(cep) > 8:
        print('CEP inválido!')
        exit()
    requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    endereco = requisicao.json()
    if 'erro' not in endereco:
        print('Endereço: {}'.format(endereco['logradouro']) +' - '+ 'Bairro: {}'.format(endereco['bairro']) +', Cidade: {}'.format(endereco['localidade']) +' - UF: {}'.format(endereco['uf'])+', CEP: {}'.format(endereco['cep']))
    else:
       print('CEP inválido!')
elif opcao == 2:
    logradouro = str(input('Digite o logradouro: '))
    uf = str(input('Digite o UF: '))
    cidade = str(input('Digite sua cidade: '))
    if len(logradouro) < 3 or len(cidade) < 3:    
        print('Endereço está inválido!')
        exit()
    requisicao = requests.get('https://viacep.com.br/ws/{}/{}/{}/json/'.format(uf,cidade,logradouro))
    endereco = list(requisicao.json())
    print(endereco)
    for p in endereco:
        print(f"Endereco: "+p['logradouro'],f"- Bairro: "+ p['bairro'],f", Cidade: "+ p['localidade'],f" - UF: "+ p['uf'],f", CEP: "+ p['cep'] )
