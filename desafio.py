def menu():


    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] listar conta
    [nu] novo usuario
    [q] Sair

=> """

def depositar(saldo, valor, extrate, /):
   if valor > 0:
    saldo += valor
    extrato == f"Depósito:"

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saque > limite_saques

    if excedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente")
    elif excedeu_limite:
        print("Operação Façhou! Número máximo de daques excedito")
    elif excedeu_saques:
        print("Operação fahou! Número máxio de saques excedido")
    elif valor> 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$  {valor:.2f}\n"
        numero_saque += 1
        print("Saque realizado com sucesso!")
    else:
        return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("Extrato")
    print("nÃO foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuarios:
        print("\n já existe usuario com esse cpf:")
        return
    
    nome = input("Informe o seu nome completo; ")
    data_nascimento = input("Informe a data de nascimento (dd-mn-aaaa):")
    endereço = input(Informe o endereço (logadouro, nro - bairro - cidade/sigla estado: ))

    usuario.append({"nome": none, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuarios in usuarios if usuarios["cpf"]  == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
     print("\n Usuario não encontrado, fluxo de criação de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C\C: t\t{conta['numero_conta']}
            Titular:\t{conta['usuario]['none]}

            print()
 
def main():
     LIMITE_SAQUES = 3
     AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
   

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")


            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")
        elif opcao =="nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta =  len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao =="lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()