class Usuario:
	def _init_(self):
		self.nome = ''
		self.email = ''
		self.avaliacao = ''
		self.estrelas = 0

def exibirMenu():
	print('\n ==== == MENU == ====')
	print('0 - SAIR')
	print('1 - CADASTRAR')
	print('2 - LISTAR AVALIAÇÕES')
	print('3 - CLASSIFICAR AVALIAÇÕES')
	print('4 - ATUALIZAR AVALIAÇÕES')
	print('5 - NOTA MÉDIA DO RESTAURANTE')
	print('==== == ==== == ====')

def cadastrarUsuario(lista):
	novoUsuario = Usuario()
	emailUsuario = input('Digite seu email: ')
	emailValido = validarEmail(listaUsuarios, emailUsuario)
	if emailValido == True:
		novoUsuario.email = emailUsuario
		novoUsuario.nome = input('Digite seu nome: ')
		novoUsuario.avaliacao = input('Digite sua avaliação: ')
		novoUsuario.estrelas = int(input('Digite o número de estrelas (1 a 5): '))
		lista.append(novoUsuario)
	else:
		print('Email incorreto ou já existente!')

def validarEmail(lista, email):
	emailValido = False
	for i in email:
		if i == '@':
			emailValido = True
			for j in lista:
				if j.email == email:
					emailValido = False
	return emailValido

def listarAvaliacao(lista):
	contador = 5
	for i in range(5):
		for j in lista:
			if j.estrelas == contador:
				print('\nUsuário: {}'.format(j.email))
				print('Avaliação {} estrelas: {}'.format(contador, j.avaliacao))
		contador -= 1

def classificarAvalicao(lista, listaElogios, listaCriticas):	
	for i in lista:
		contadorElogios = 0
		contadorCriticas = 0
		avaliacaoMinuscula = i.avaliacao.lower()
		avaliacao = avaliacaoMinuscula.split()
		for j in avaliacao:
			for z in listaElogios:
				if j == z:
					contadorElogios+=1
			for z in listaCriticas:
				if j == z:
					contadorCriticas +=1
		if contadorElogios > contadorCriticas:
			print('A avaliação do usuário {}, {} estrelas, foi ótima!'.format(i.email, i.estrelas))
		elif contadorElogios < contadorCriticas:
			print('A avaliação do usuário {}, {} estrelas, foi ruim!'.format(i.email, i.estrelas))
		elif contadorElogios == contadorCriticas:
			print('A avaliação do usuário {}, {} estrelas, foi indeterminada!'.format(i.email, i.estrelas))

def atualizarAvalicao(lista):
	emailUsuario = input('Digite o email cadastrado: ')
	for i in lista:
		if i.email == emailUsuario:
			i.avaliacao = input('Digite a nova avaliação: ')
		else:
			print('Email não encotrado! Cadastre-se: ')
			cadastrarUsuario(listaUsuarios)

def informarMedia(lista):
	qtddTotal = len(lista)
	qtddEstrelas = 0
	for i in lista:
		qtddEstrelas += i.estrelas
	media = round((qtddEstrelas/qtddTotal),0)
	print('A nota média do restaurante é de: {} estrelas'.format(media))

listaUsuarios = []
listaElogios = ['bom', 'excelente', 'ótimo']
listaCriticas = ['ruim', 'péssimo', 'horrível']

opc = -1
while opc != 0:
	exibirMenu()
	opc = int(input('Digite sua opção: '))
	if opc == 1:
		cadastrarUsuario(listaUsuarios)
	elif opc == 2:
		listarAvaliacao(listaUsuarios)
	elif opc == 3:
		classificarAvalicao(listaUsuarios, listaElogios, listaCriticas)
	elif opc == 4:
		atualizarAvalicao(listaUsuarios)
	elif opc == 5:
		informarMedia(listaUsuarios)