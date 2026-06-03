from django.shortcuts import render

def inicio(request):
    # Dados gerais da série
    context = {
        'titulo': 'Breaking Bad - O Legado',
        'sinopse': 'Um professor de química do ensino médio descobre que tem câncer terminal e decide secretamente produzir metanfetamina para garantir o futuro financeiro de sua família.',
        'ano_lancamento': 2008,
        'criador': 'Vince Gilligan'
    }
    return render(request, 'inicio.html', context)

def elenco(request):
    # Dicionário com 11 integrantes do elenco
    context = {
        'integrantes': [
            {'nome': 'Bryan Cranston', 'personagem': 'Walter White', 'idade': 70, 'posicao': 'Protagonista / Produtor', 'local_nascimento': 'Hollywood, Califórnia', 'foto': 'fotos/walter.png'},
            {'nome': 'Aaron Paul', 'personagem': 'Jesse Pinkman', 'idade': 46, 'posicao': 'Co-protagonista', 'local_nascimento': 'Emmett, Idaho', 'foto': 'fotos/jesse.webp'},
            {'nome': 'Anna Gunn', 'personagem': 'Skyler White', 'idade': 57, 'posicao': 'Elenco Principal', 'local_nascimento': 'Santa Fe, Novo México', 'foto': 'fotos/Skyler White.webp'},
            {'nome': 'Dean Norris', 'personagem': 'Hank Schrader', 'idade': 63, 'posicao': 'Elenco Principal', 'local_nascimento': 'South Bend, Indiana', 'foto': 'fotos/Hank Schrader.webp'},
            {'nome': 'Betsy Brandt', 'personagem': 'Marie Schrader', 'idade': 53, 'posicao': 'Elenco Principal', 'local_nascimento': 'Bay City, Michigan', 'foto': 'fotos/Marie Schrader.webp'},
            {'nome': 'RJ Mitte', 'personagem': 'Walter White Jr.', 'idade': 33, 'posicao': 'Elenco Principal', 'local_nascimento': 'Lafayette, Louisiana', 'foto': 'fotos/Walter White Jr..webp'},
            {'nome': 'Bob Odenkirk', 'personagem': 'Saul Goodman', 'idade': 63, 'posicao': 'Elenco Principal', 'local_nascimento': 'Berwyn, Illinois', 'foto': 'fotos/Saul Goodman.jpg'},
            {'nome': 'Jonathan Banks', 'personagem': 'Mike Ehrmantraut', 'idade': 79, 'posicao': 'Elenco Principal', 'local_nascimento': 'Washington, D.C.', 'foto': 'fotos/Mike Ehrmantraut.webp'},
            {'nome': 'Giancarlo Esposito', 'personagem': 'Gus Fring', 'idade': 68, 'posicao': 'Antagonista Principal', 'local_nascimento': 'Copenhague, Dinamarca', 'foto': 'fotos/Gus Fring.webp'},
            {'nome': 'Jesse Plemons', 'personagem': 'Todd Alquist', 'idade': 38, 'poshesion': 'Elenco Recorrente', 'local_nascimento': 'Dallas, Texas', 'foto': 'fotos/Todd Alquist.webp'},
            {'nome': 'Laura Fraser', 'personagem': 'Lydia Rodarte-Quayle', 'idade': 50, 'posicao': 'Elenco Recorrente', 'local_nascimento': 'Glasgow, Escócia', 'foto': 'fotos/Lydia Rodarte-Quayle.webp'},
        ]
    }
    return render(request, 'elenco.html', context)

def sobre(request):
    # Dados sobre os autores e o site
    context = {
        'info_site': {
            'projeto': 'Trabalho Acadêmico de Webdesign',
            'tecnologias': 'Django, HTML e CSS',
            'descricao': 'site para conclusão do trabalho dado por diego cirilo.'
        },
        'autores': [
            {'nome': 'joão Emanuel de Souza Gomes'}
        ]
    }
    return render(request, 'sobre.html', context)

# Create your views here.
