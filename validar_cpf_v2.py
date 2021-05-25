res1 = res2 = 0
cpf = []
num = str(input('Informe seu cpf (Apenas números): '))
while len(num) != 11 or num in '11111111111' or num in '22222222222' or num in '33333333333' or num in '44444444444' or num in '55555555555' or num in '66666666666' or num in '77777777777' or num in '88888888888' or num in '99999999999':
    num = str(input('CPF Inválido. Informe seu cpf (Apenas números): '))
for c in num:
    cpf.append(int(c))
#Executa a verificação dos dígitos de segurança.
for c,v in enumerate(range(10,1,-1)):
    res1 += v * cpf[c]
res1 = (res1 * 10) % 11
if res1 == 10:
    res1 = 0
for c,v in enumerate(range(11,1,-1)):
    res2 += v * cpf[c]
res2 = (res2 * 10) % 11
if res2 == 10:
    res2 = 0
print(f'Primeiro código de verificação: \033[1;34m{res1}\033[m\nSegundo código de verificação: \033[1;34m{res2}\033[m\n')
if res1 == cpf[9] and res2 == cpf[10]:
    print(f'\033[1;32mCPF VÁLIDO\033[m')
else:
    print(f'\033[1;31mCPF INVÁLIDO\033[m')
