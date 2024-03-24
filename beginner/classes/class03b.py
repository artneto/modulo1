#retornar a quantidade de palavras
#informar n de ocorrencia de determinada palavra
#permitir substituir algumas palavras

text_inicial = '''no meio do caminho tinha uma pedra
 tinha uma pedra no meio do caminho pedra pedra funcao'''

count_text = len(text_inicial.split())
count_pedra = text_inicial.count("pedra")
rep_palavra = text_inicial.replace("pedra", "funcao")
print(count_text)
print(count_pedra)
print(rep_palavra)