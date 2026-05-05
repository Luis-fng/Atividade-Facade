class Conta:
    def __init__(self):
        self.saldo = 1000

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado")
        else:
            print("Saldo insuficiente")

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito realizado")

class Emprestimo:
    def solicitar(self, valor):
        print("Empréstimo aprovado")
        return valor

class Seguranca:
    def autenticar(self, senha):
        return senha == "1234"

class BancoFacade:
    def __init__(self):
        self.conta = Conta()
        self.emprestimo = Emprestimo()
        self.seguranca = Seguranca()

    def realizar_transacao(self, tipo, valor, senha):
        if not self.seguranca.autenticar(senha):
            print("Acesso negado")
            return

        if tipo == "saque":
            if valor > self.conta.saldo:
                valor_emprestimo = self.emprestimo.solicitar(valor)
                self.conta.depositar(valor_emprestimo)
            self.conta.sacar(valor)

        elif tipo == "deposito":
            self.conta.depositar(valor)

        print("Saldo:", self.conta.saldo)

banco = BancoFacade()
banco.realizar_transacao("saque", 1500, "1234")
banco.realizar_transacao("deposito", 300, "1234")
banco.realizar_transacao("saque", 200, "0000")