def ler_arquivo_txt(nome_arquivo):
  arquivo = open(nome_arquivo)
  texto = arquivo.read()
  arquivo.close()
  return texto

def tratar_texto(texto_antigo):
  texto_novo = texto_antigo
  retirar = ["\n", ","," – ", " - ",".","!","?","...",":"]
  for caracter in retirar:
    texto_novo = texto_novo.replace(caracter, " ")
  return texto_novo.lower()

def contar_palavras(palavras):
  contagem = {}
  for palavra in palavras.split():
    #if palavra in ['a','e','o','de']:
    #  continue
    if len(palavra) < 3:
      continue
    try:
      contagem[palavra] += 1
    except:
      contagem[palavra] = 1
  return contagem

def gravar_arquivo_txt(contagem_palavras):
  arquivo = open('resultado_contagem.txt', 'w')
  for chave, valor in contagem_palavras.items():
    arquivo.writelines(f'A palavra {chave} aparece {valor} vez(es) no texto.\n')
  arquivo.close()
  print('Arquivo gerado com sucesso!')

def word_counter(nome_arquivo):
  texto = ler_arquivo_txt(nome_arquivo)
  texto_tratado = tratar_texto(texto)
  contagem = contar_palavras(texto_tratado)
  gravar_arquivo_txt(contagem)
  

word_counter('elefante.txt')