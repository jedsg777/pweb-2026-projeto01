from django.shortcuts import render, redirect
from .forms import PersonagemForm
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import PersonagemForm

def inicio(request):
    context = {
        'titulo': 'Breaking Bad - O Legado',
        'sinopse': 'Um professor de química do ensino médio descobre que tem câncer terminal e decide secretamente produzir metanfetamina para garantir o futuro financeiro de sua família.',
        'ano_lancamento': 2008,
        'criador': 'Vince Gilligan'
    }
    return render(request, 'inicio.html', context)



ELENCO_PADRAO = [
    {'nome': 'Bryan Cranston', 'personagem': 'Walter White', 'idade': 70, 'posicao': 'Protagonista / Produtor', 'local_nascimento': 'Hollywood, Califórnia', 'foto': 'fotos/walter.png'},
    {'nome': 'Aaron Paul', 'personagem': 'Jesse Pinkman', 'idade': 46, 'posicao': 'Co-protagonista', 'local_nascimento': 'Emmett, Idaho', 'foto': 'fotos/jesse.webp'},
    {'nome': 'Anna Gunn', 'personagem': 'Skyler White', 'idade': 57, 'posicao': 'Elenco Principal', 'local_nascimento': 'Santa Fe, Novo México', 'foto': 'fotos/Skyler White.webp'},
    {'nome': 'Dean Norris', 'personagem': 'Hank Schrader', 'idade': 63, 'posicao': 'Elenco Principal', 'local_nascimento': 'South Bend, Indiana', 'foto': 'fotos/Hank Schrader.webp'},
    {'nome': 'Betsy Brandt', 'personagem': 'Marie Schrader', 'idade': 53, 'posicao': 'Elenco Principal', 'local_nascimento': 'Bay City, Michigan', 'foto': 'fotos/Marie Schrader.webp'},
    {'nome': 'RJ Mitte', 'personagem': 'Walter White Jr.', 'idade': 33, 'posicao': 'Elenco Principal', 'local_nascimento': 'Lafayette, Louisiana', 'foto': 'fotos/Walter White Jr..webp'},
    {'nome': 'Bob Odenkirk', 'personagem': 'Saul Goodman', 'idade': 63, 'posicao': 'Elenco Principal', 'local_nascimento': 'Berwyn, Illinois', 'foto': 'fotos/Saul Goodman.jpg'},
    {'nome': 'Jonathan Banks', 'personagem': 'Mike Ehrmantraut', 'idade': 79, 'posicao': 'Elenco Principal', 'local_nascimento': 'Washington, D.C.', 'foto': 'fotos/Mike Ehrmantraut.webp'},
    {'nome': 'Giancarlo Esposito', 'personagem': 'Gus Fring', 'idade': 68, 'posicao': 'Antagonista Principal', 'local_nascimento': 'Copenhague, Dinamarca', 'foto': 'fotos/Gus Fring.webp'},
    {'nome': 'Jesse Plemons', 'personagem': 'Todd Alquist', 'idade': 38, 'posicao': 'Elenco Recorrente', 'local_nascimento': 'Dallas, Texas', 'foto': 'fotos/Todd Alquist.webp'},
    {'nome': 'Laura Fraser', 'personagem': 'Lydia Rodarte-Quayle', 'idade': 50, 'posicao': 'Elenco Recorrente', 'local_nascimento': 'Glasgow, Escócia', 'foto': 'fotos/Lydia Rodarte-Quayle.webp'},
]

def elenco(request):

    if 'elenco_lista' not in request.session:
        request.session['elenco_lista'] = list(ELENCO_PADRAO)

    if request.method == 'POST':
        form = PersonagemForm(request.POST, request.FILES)
        
        if form.is_valid():
            foto_arquivo = request.FILES['foto']
            
            
            caminho_salvamento = os.path.join(settings.BASE_DIR, 'app', 'static', 'fotos')
            os.makedirs(caminho_salvamento, exist_ok=True)
            
            
            fs = FileSystemStorage(location=caminho_salvamento)
            nome_arquivo_salvo = fs.save(foto_arquivo.name, foto_arquivo)
            
            
            caminho_static_foto = f'fotos/{nome_arquivo_salvo}'

            novo_personagem = {
                'nome': form.cleaned_data['nome'],
                'personagem': form.cleaned_data['personagem'],
                'idade': int(form.cleaned_data['idade']),
                'posicao': form.cleaned_data['posicao'],
                'local_nascimento': form.cleaned_data['local_nascimento'],
                'foto': caminho_static_foto 
            }
            
           
            lista_atual = list(request.session['elenco_lista'])
            lista_atual.append(novo_personagem)
            
            request.session['elenco_lista'] = lista_atual
            request.session.modified = True
            
            return redirect('elenco')
    else:
        form = PersonagemForm()

    context = {
        'integrantes': request.session.get('elenco_lista', ELENCO_PADRAO),
        'form': form
    }
    return render(request, 'elenco.html', context)

def sobre(request):
    context = {
        'info_site': {
            'projeto': 'Trabalho Acadêmico de Webdesign',
            'tecnologias': 'Django, HTML e CSS',
            'descricao': 'site para conclusão do trabalho dado por diego cirilo.'
        },
        'autores': [
            {'nome': 'joão Emanuel de Souza Gomes', 'rm': '12345', 'funcao': 'Desenvolvedor'}
        ]
    }
    return render(request, 'sobre.html', context)