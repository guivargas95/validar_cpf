
val = []
val2 = []
cpf = []

num = str(input('Informe seu cpf (Apenas números): '))
while len(num) != 11:
    num = str(input('CPF Inválido. Informe seu cpf (Apenas números): '))
for c in num:
    cpf.append(int(c))
for c in range(10,1,-1):
    val.append(c)
res1 = (val[0]*cpf[0])+(val[1]*cpf[1])+(val[2]*cpf[2])+(val[3]*cpf[3])+(val[4]*cpf[4])+(val[5]*cpf[5])+(val[6]*cpf[6])+(val[7]*cpf[7])+(val[8]*cpf[8])
res1 = (res1*10)%11
if res1 == 10:
    res1 = 0
val.clear()
for c in range(11,1,-1):
    val.append(c)
res2 = (val[0]*cpf[0])+(val[1]*cpf[1])+(val[2]*cpf[2])+(val[3]*cpf[3])+(val[4]*cpf[4])+(val[5]*cpf[5])+(val[6]*cpf[6])+(val[7]*cpf[7])+(val[8]*cpf[8])+(val[9]*cpf[9])
res2 = (res2*10)%11
if res2 == 10:
    res2 = 0
print(f'Primeiro código de verificação: \033[1;34m{res1}\033[m\nSegundo código de verificação: \033[1;34m{res2}\033[m\n')
if res1 == cpf[9] and res2 == cpf[10]:
    print(f'\033[1;32mCPF VÁLIDO\033[m')
else:
    print(f'\033[1;31mCPF INVÁLIDO\033[m')



