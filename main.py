import sqlite3

conexao = sqlite3.connect("financeiro.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS transacoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    tipo TEXT NOT NULL,
    categoria TEXT NOT NULL
    ) 
""")
 
conexao.commit()

class Transacao:
    def __init__(self, descricao, valor, tipo, categoria):
        self.descricao = descricao
        self.valor = valor
        self.tipo = tipo
        self.categoria = categoria

    def cadastrar_transacao(self):
        cursor.execute("""
        INSERT INTO transacoes(descricao, valor, tipo, categoria)
        VALUES (?, ?, ?, ?)
        """, (self.descricao, self.valor, self.tipo, self.categoria))

        conexao.commit()

    def listar_transacao(self):
        cursor.execute("SELECT * FROM transacoes")
        transacoes = cursor.fetchall()

        if not transacoes:
            print('Nenhuma transação foi encontrada!')
            return
        
        for transacao in transacoes:

            id_transacao, descricao, valor, tipo, categoria = transacao

            print('-' * 30)
            print(f"""ID: {id_transacao}
Descrição: {descricao}
Valor: R${valor:.2f}
Tipo: {tipo}
Categoria: {categoria}
""")

    def buscar_transacao_id(self, id__transacao):
        cursor.execute("""SELECT * FROM transacoes 
                       WHERE id = ?""", 
                       (id__transacao, ))
        return cursor.fetchone()

    def atualizar_transacao(self, id_transacao):
        cursor.execute("""UPDATE transacoes
                        SET descricao = ?,
                            valor = ?,
                            tipo = ?,
                            categoria = ?
                        WHERE id = ?
""", (self.descricao, self.valor, self.tipo, self.categoria, id_transacao))

        conexao.commit()

    def excluir_transacao_id(self, id_transacao):
        cursor.execute("""
        DELETE FROM transacoes
        WHERE id = ?
""", (id_transacao,))

        conexao.commit()

    def calcular_saldo(self):
        cursor.execute("""
            SELECT SUM(valor)
            FROM transacoes
            WHERE tipo = 'Entrada'
""")

        total_entrada = cursor.fetchone()[0] or 0

        cursor.execute("""
            SELECT SUM(valor)
            FROM transacoes
            WHERE tipo = 'Saída'
""")

        total_saida = cursor.fetchone()[0] or 0

        saldo = total_entrada - total_saida

        print(f"\nTotal de entradas: R$ {total_entrada:.2f}")
        print(f"Total de saídas: R$ {total_saida:.2f}")
        print('-' * 30)

        if saldo >= 0:
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print(f'Saldo negativo: R${saldo:.2f}')
    def gastos_por_categoria(self):
        cursor.execute("""
            SELECT categoria, SUM(valor)
            FROM transacoes
            WHERE tipo = 'Saída'
            GROUP BY categoria
            ORDER BY SUM(valor) DESC     
""")

        resultados = cursor.fetchall()

        if not resultados:
            print('Nenhuma sáida cadastrada!')
            return

        print('\n===== GASTOS POR CATEGORIA =====')

        for categoria, total in resultados:
            print(f'{categoria}: R${total:.2f}')

while True:
    print('\n===== CADASTRO DE TRANSAÇÃO =====')
    print("""
[ 1 ] - Cadastrar transação
[ 2 ] - Listar transações
[ 3 ] - Buscar transação por iD
[ 4 ] - Atualizar transação
[ 5 ] - Excluir transação por ID
[ 6 ] - Calcular saldo
[ 7 ] - Gastos por categoria
[ 0 ] - Sair
""") 
    
    try:
        opcao = int(input('Escolha: '))
    except ValueError:
        print('Opção inválida! Digite um número inteiro.')
        continue

    if opcao == 1:
        descricao = input('Digite qual descrição da transação: ').strip().title()

        try:
            valor = float(input('Valor da transação: R$'))
        except ValueError:
            print('Error. Digite um valor válido.')
            continue

        tipo = input('Tipo da transação: ').strip().title()
        categoria = input('Categoria da transação: ').strip().title()

        transacao = Transacao(descricao, valor, tipo, categoria)
        transacao.cadastrar_transacao()

        print('Transação cadastrada com sucesso!')

    elif opcao == 2:
        transacao = Transacao("", 0, "", "")
        transacao.listar_transacao()

    elif opcao == 3:
        try:
            id_transacao = int(input('Digite o ID para a busca: '))
        except ValueError:
            print('ID inválido! Digite um ID válido.')
            continue

        transacao = Transacao("", 0, "", "")
        resultado = transacao.buscar_transacao_id(id_transacao)

        if resultado is None:
            print('Transação não foi encontrada!')

        else:
            id_transacao, descricao, valor, tipo, categoria = resultado
        
            print('-' * 30)
            print(f"""ID: {id_transacao}
Descrição: {descricao}
Valor: R${valor:.2f}
Tipo: {tipo}
Categoria : {categoria}
""")
            print('-' * 30)

    elif opcao == 4:
        try:
            id_transacao = int(input('Digite o ID para atualizar transação: '))
        except ValueError:
            print('ID inválido, por favor, digite um ID válido.')
            continue

        transacao = Transacao("", 0, "", "")
        resultado = transacao.buscar_transacao_id(id_transacao)
        
        if not resultado:
            print('Nenhuma transação encontrada!')
            continue

        descricao = input('Nova descrição: ').strip().title()

        try:
            valor = float(input('Novo valor: R$'))
        except ValueError:
            print('Valor inválido. Digite um valor válido.')
            continue

        tipo = input('Novo tipo: ').strip().title()
        categoria = input('Nova categoria: ').strip().title()

        transacao = Transacao(descricao, valor, tipo, categoria)

        transacao.atualizar_transacao(id_transacao)

        print('Transação encontrada!')

    elif opcao == 5:
        try:
            id_transacao = int(
            input('Digite um ID para excluir: '))
        except ValueError:
            print('ID inválido! Digite um ID válido.')
            continue

        transacao = Transacao("", 0, "", "")

        resultado = transacao.buscar_transacao_id(id_transacao)

        if not resultado:
            print('Transação não encontrada!')
            continue

        id_transacao, descricao, valor, tipo, categoria = resultado

        print('-' * 30)
        print(f"""ID: {id_transacao}
Descrição: {descricao}
Valor: R$ {valor:.2f}
Tipo: {tipo}
Categoria: {categoria}
""")
        print('-' * 30)

        escolha = input('Deseja continuar [S/N]? ').strip().lower()

        if not escolha:
            print('Opção inválida!')
            continue

        if escolha[0] == 'n':
            print('Ação cancelada!')
            continue

        transacao.excluir_transacao_id(id_transacao)

        print('Transação excluída com sucesso!')


    elif opcao == 6:

        transacao = Transacao("", 0, "", "")
        transacao.calcular_saldo()

    elif opcao == 7:

        transacao = Transacao("", 0, "", "")
        transacao.gastos_por_categoria()

    elif opcao == 0:
        print('Sistema encerrado..')
        break

    else:
        print('Opção inválida!')
        
conexao.close()