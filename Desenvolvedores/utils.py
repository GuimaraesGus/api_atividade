from models import Programador, Habilidades, ProgramadorHabilidade

# Insere dados na tabela programador
def insere_programador():
    programador = Programador(nome='Gustavo', idade=29, email='gustavollaguimaraes@gmail.com')
    print(programador)
    programador.save()

# Insere dados na tabela habilidades
def insere_habilidade():
    habilidade = Habilidades(nome='Python')
    habilidade.save()
    print(habilidade)
    # habilidade = Habilidades(nome='Java')
    # habilidade.save()
    # habilidade = Habilidades(nome='COBOL')
    # habilidade.save()
    # habilidade = Habilidades(nome='C#')
    # habilidade.save()
    # habilidade = Habilidades(nome='SQL')
    # habilidade.save()
    # habilidade = Habilidades(nome='HTML')
    # habilidade.save()

# Insere dados na tabela programador_habilidade
def insere_programador_habilidade():
    programador_habilidade = ProgramadorHabilidade(programador_id=2, habilidade_id=2)
    programador_habilidade.save()
    programador_habilidade = ProgramadorHabilidade(programador_id=2, habilidade_id=6)
    programador_habilidade.save()
    programador_habilidade = ProgramadorHabilidade(programador_id=3, habilidade_id=2)
    programador_habilidade.save()
    programador_habilidade = ProgramadorHabilidade(programador_id=3, habilidade_id=3)
    programador_habilidade.save()
    programador_habilidade = ProgramadorHabilidade(programador_id=3, habilidade_id=7)
    programador_habilidade.save()
    programador_habilidade = ProgramadorHabilidade(programador_id=3, habilidade_id=5)
    programador_habilidade.save()
    programador_habilidade = ProgramadorHabilidade(programador_id=3, habilidade_id=6)
    programador_habilidade.save()

# Consulta dados na tabela programador
def consulta_programadores():
    programadores = Programador.query.all()
    for programador in programadores:
        print(programador, programador.id)
    # programador = Programador.query.filter_by(nome='Gustavo').first()
    # print(programador, programador.idade)

# Consulta dados na tabela habilidades
def consulta_habilidades():
    habilidades = Habilidades.query.all()
    for habilidade in habilidades:
        print(habilidade, habilidade.id)

# Consulta dados na tabela programador_habilidade
def consulta_programadores_habilidades():
    programadores_habilidades = ProgramadorHabilidade.query.all()
    for programador_habilidade in programadores_habilidades:
        print(programador_habilidade)

# Altera dados na tabela programador
def altera_programador():
    programador = Programador.query.filter_by(nome='Gustavo').first()
    programador.nome = 'Guimarães'
    programador.save()

# Altera dados na tabela habilidades
def altera_habilidade():
    habilidade = Habilidades.query.filter_by(nome='Python').first()
    habilidade.nome = 'Python 2'
    habilidade.save()

# Exclui dados na tabela programador
def exclui_programador():
    programador = Programador.query.filter_by(nome='Guimarães').first()
    programador.delete()

# Exclui dados na tabela habilidades
def exclui_habilidade():
    habilidade = Habilidades.query.filter_by(nome='Python 2').first()
    habilidade.delete()

# Exclui dados na tabela programador_habilidade
def exclui_programador_habilidade():
    programador_habilidade = ProgramadorHabilidade.query.filter_by(programador_id=3, habilidade_id=2).first()
    programador_habilidade.delete()

if __name__ == '__main__':
    # Manipulação de Programador
    # insere_programador()
    consulta_programadores()
    # altera_programador()
    # exclui_programador()

    # Manipulação de Habilidades
    # insere_habilidade()
    consulta_habilidades()
    # altera_habilidadev()
    # exclui_habilidade()

    # Manipulação de Habilidades de Programador
    # insere_programador_habilidade()
    consulta_programadores_habilidades()
    # exclui_programador_habilidade()
    # consulta_programadores_habilidades()