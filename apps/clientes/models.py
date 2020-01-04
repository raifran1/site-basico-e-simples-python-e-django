from django.db import models

# Create your models here.
class Cliente(models.Model):
    name = models.CharField(verbose_name=u'Nome Completo',max_length=70)
    cpfCnpj = models.CharField(verbose_name=u'CPF',max_length=17)
    email = models.EmailField(verbose_name=u'Email',max_length=254,help_text='Utilizar um email válido') 
    mobilePhone = models.CharField(verbose_name=u'Telefone',max_length=50,help_text='Utilize um número válido')
    postalCode = models.IntegerField(verbose_name=u'CEP',help_text='Utilize um CEP válido')
    addressNumber = models.IntegerField(verbose_name=u'Número da Casa',)
    descricao_alunos = models.TextField(verbose_name=u'Sobre os Alunos',help_text='Campo para utilizar para Cadastro de Aluno')
    
    class Meta:
        verbose_name = u'Cliente'
        verbose_name_plural = u'Clientes'
        ordering = ['name']

    def __str__(self):
        return self.name


class Aluno(models.Model):
    nome_aluno = models.CharField(verbose_name=u'Nome Completo',max_length=70)
    serie = models.CharField(verbose_name=u'Série',max_length=50,choices=(("1º Ano - Fundamental I", ("1º Ano - Fundamental I")),
                                             ("2º Ano - Fundamental I", ("2º Ano - Fundamental I")),
                                             ("3º Ano - Fundamental I", ("3º Ano - Fundamental I")),
                                             ("4º Ano - Fundamental I", ("4º Ano - Fundamental I")),
                                             ("5º Ano - Fundamental I", ("5º Ano - Fundamental I")),
                                             ("6º Ano - Fundamental II", ("6º Ano - Fundamental II")),
                                             ("7º Ano - Fundamental II", ("7º Ano - Fundamental II")),
                                             ("8º Ano - Fundamental II", ("8º Ano - Fundamental II")),
                                             ("9º Ano - Fundamental II", ("9º Ano - Fundamental II")),
                                             ("1º Ano - Médio", ("1º Ano - Médio")),
                                             ("2º Ano - Médio", ("2º Ano - Médio")),
                                             ),default="")
    escola = models.CharField(verbose_name=u'Escola',max_length=50,blank=True, null=True)
    idade = models.IntegerField(verbose_name=u'Idade',blank=True, null=True)
    necessidade_especial = models.BooleanField(verbose_name=u'Necessidade Especial?',default=False)
    financeiro = models.ForeignKey("Financeiro", verbose_name=u'Cadastro Financeiro', on_delete=models.CASCADE)
    responsavel = models.ForeignKey("Cliente", verbose_name=u'Responsável',on_delete=models.DO_NOTHING)
    turma = models.ForeignKey("Turma",verbose_name=u'Turma',on_delete=models.DO_NOTHING)
    observacoes = models.TextField(verbose_name=u'Observações',blank=True,null=True,help_text='Observações Gerais sobre o Aluno')

    class Meta:
        verbose_name = u'Aluno'
        verbose_name_plural = u'Alunos'
        ordering = ['nome_aluno']


    def __str__(self):
        return self.nome_aluno    


class Turma(models.Model):
    nome_turma = models.CharField(max_length=50)
    horario_inicial = models.TimeField(auto_now=False, auto_now_add=False)
    horario_final = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nome_turma

class Financeiro(models.Model):
    cliente = models.ForeignKey("Cliente", verbose_name=u'Cliente', on_delete=models.CASCADE)
    preco_matricula = models.FloatField(u'Preço da Matrícula',)
    preco_mensalidade = models.FloatField(u'Preço da Mensalidade',)
    vencimento = models.IntegerField(u'Vencimento',)
    matricula = models.BooleanField(u'MATR.',)
    # Jan = models.BooleanField(u'Matr.',)
    feveveiro = models.BooleanField(u'FEV.',)
    marco = models.BooleanField(u'MAR.',)
    abril = models.BooleanField(u'ABR.',)
    maio = models.BooleanField(u'MAI.',)
    junho = models.BooleanField(u'JUN.',)
    julho = models.BooleanField(u'JUL.',)
    agosto = models.BooleanField(u'AGO.',)
    setembro = models.BooleanField(u'SET.',)
    outubro = models.BooleanField(u'OUT.',)
    novembro = models.BooleanField(u'NOV.',)
    dezembro = models.BooleanField(u'DEZ.',)

    class Meta:
        verbose_name = u'Cadastro Financeiro'
        verbose_name_plural = u'Cadastro Financeiro'
        ordering = ['cliente']

    def __str__(self):
        return u'{}'.format(self.cliente) 
    
