from django.contrib import admin
from .models import Cliente, Aluno, Turma, Financeiro
# Register your models here.

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpfCnpj','mobilePhone','descricao_alunos')
    search_fields = ('name','cpfCnpj')
    #list_filter = ('status_disponibilidade')
    #list_editable = ('status_disponibilidade',)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_aluno', 'serie','turma','financeiro')
    search_fields = ('nome_aluno',)
    list_filter = ('serie','turma',)
    list_editable = ('turma',)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome_turma', 'horario_inicial','horario_final')
    search_fields = ('nome_turma',)
    # list_filter = ('serie','turma')
    list_editable = ('horario_inicial','horario_final')


@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'preco_mensalidade','preco_matricula','vencimento','matricula', 'feveveiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', )
    search_fields = ('cliente',)
    # list_filter = ('serie','turma')
    list_editable = ('matricula', 'feveveiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro', )