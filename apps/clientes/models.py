from django.db import models

# Create your models here.
class Cliente(models.Model):
    name = models.CharField(max_length=70)
    cpfCnpj = models.CharField(max_length=17)
    email = models.EmailField(max_length=254) 
    mobilePhone = models.IntegerField()
    postalCode = models.IntegerField()
    addressNumber = models.IntegerField()
    descricao_alunos = models.TextField()
    
    def __str__(self):
        return self.name


class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=70)
    serie = models.CharField(max_length=50,choices=(("1º Ano - Fundamental I", ("1º Ano - Fundamental I")),
                                             ("2º Ano - Fundamental I", ("2º Ano - Fundamental I")),
                                             ("3º Ano - Fundamental I", ("3º Ano - Fundamental I")),
                                             ("4º Ano - Fundamental I", ("4º Ano - Fundamental I")),
                                             ("5º Ano - Fundamental I", ("5º Ano - Fundamental I")),
                                             ("6º Ano - Fundamental II", ("6º Ano - Fundamental II")),
                                             ("7º Ano - Fundamental II", ("7º Ano - Fundamental II")),
                                             ("8º Ano - Fundamental II", ("8º Ano - Fundamental II")),
                                             ("9º Ano - Fundamental II", ("9º Ano - Fundamental II")),
                                             ("1º Ano - Médio", ("1º Ano - Médio")),
                                             ("2º Ano - Médio", ("1º Ano - Médio")),
                                             ),default="")
    escola = models.CharField(max_length=50)
    idade = models.IntegerField()
    necessidade_especial = models.BooleanField(default=False)
    preco = models.IntegerField()
    desconto = models.IntegerField(default=0)
    observacoes = models.TextField(blank=True,null=True)
    status =  models.CharField(max_length=50,choices=(("Ativo", ("Ativo")),
                                             ("Atrasado", ("Atrasado")),
                                             ("Pendente", ("Pendente")),
                                             ),default="")
    responsavel = models.ForeignKey("Cliente", on_delete=models.DO_NOTHING)
    turma = models.ForeignKey("Turma",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome_aluno    


class Turma(models.Model):
    nome_turma = models.CharField(max_length=50)
    horario_inicial = models.TimeField(auto_now=False, auto_now_add=False)
    horario_final = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome_turma
