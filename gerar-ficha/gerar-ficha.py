# Entrada de Dados
nome = input('Digite o nome do aluno(a):' )
idade = input('Digite a idade do aluno(a):' )
peso = input('Digite o peso do aluno(a) (Kg):' )
altura = input('Digite a altura do aluno(a) (m):' )

# Calculando o IMC
imc = float(peso) / (float(altura) ** 2)
print(imc)

# Criando o status
status = "dentro do peso"
if imc > 25:
  status = "sobrepeso"

print(status)

# Gerando o PDF
import pdf_reports

dados_aluno = {
    'nome': nome,
    'idade': idade,
    'peso': peso,
    'altura': altura,
    'imc': round(imc,2),
    'status': status
}

template = pdf_reports.pug_to_html('template.pug', dados=dados_aluno)

pdf_reports.write_report(template, 'ficha_aluno.pdf', use_default_styling=False)