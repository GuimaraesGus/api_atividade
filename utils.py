from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Gustavo', idade=29)
    print(pessoa)
    pessoa.save()

# Consulta dados na tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    # pessoa = Pessoas.query.filter_by(nome='Gustavo').first()
    # print(pessoa, pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = 'João'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='João').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
