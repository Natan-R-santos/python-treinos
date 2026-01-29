usuarios = [
    {"email": "natan@gmail.com", "senha": "1234"},
    {"email": "gabi@gmail.com", "senha": "4321"},
    {"email": "mel@gmail.com", "senha": "9999"}
]
print(usuarios[2].['email'])
print(usuarios[0].['senha'])
print(usuarios)

email = input(('Digite seu email:'))
senha = input(('Digite sua senha:'))
logado = False
tentativa = 3

while tentativa < 3:
    for usuario in usuarios
      if email == usuarios['email'] and senha == usuarios['senha']
        logado = True
        break
if logado:
    print('Usuario logado')
    break
else:
    tentativa +=1
    print('Login negado,tente novamente')

if tentativa < 3:
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
if tentativa == 3 and not logado:
    print('Conta Bloquada')
