class validar_cpf:
    def __init__(self, cpf):
        self.__cpf = cpf
        self.validar()

    def numero_valido(self):
        '''Verifica se o valor contém apenas números, 11 dígitos e se os números não são todos iguais'''
        cpf = self.__cpf
        if len(cpf) != 11:
            print('Um CPF deve conter 11 dígitos')
            return False
        try:
            cpf = int(cpf)
        except:
            print('O valor deve conter apenas números')
            return False
        valoresInvalidos = []
        for c in range(1, 10):
            for num in range(1, 12):
                valoresInvalidos.append(f'{c}')
            valoresInvalidos = ''.join(valoresInvalidos)
            if str(cpf) in valoresInvalidos:
                print('CPF inválido')
                return False
            valoresInvalidos = []
        return True

    def verificar_digito_seguranca(self):
        '''Executa a verificação dos dígitos de segurança'''
        resultado1 = resultado2 = 0
        cpf = []
        for c in self.__cpf:
            cpf.append(int(c))
        for c,v in enumerate(range(10,1,-1)):
            resultado1 += v * cpf[c]
        resultado1 = (resultado1 * 10) % 11
        if resultado1 == 10:
            resultado1 = 0
        for c,v in enumerate(range(11,1,-1)):
            resultado2 += v * cpf[c]
        resultado2 = (resultado2 * 10) % 11
        if resultado2 == 10:
            resultado2 = 0
        if resultado1 == cpf[9] and resultado2 == cpf[10]:
            return True
        else:
            return False

    def validar(self):
        '''Conclui a validação e retorna se o CPF é válido ou não'''
        if self.numero_valido() and self.verificar_digito_seguranca():
            print(f'\033[1;32mCPF VÁLIDO\033[m')
            return True
        else:
            print(f'\033[1;31mCPF INVÁLIDO\033[m')
            return False
