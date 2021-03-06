from math import sqrt

def carregaMovieLens(path='C:/Users/weber/Python-AlgRec/base'):
    filmes ={}
    for linha in open(path + '/u.item'):
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    base ={}
    for linha in open(path + '/u.data'):
        (usuario, idfilme, nota, tempo) = linha.split('\t')
        base.setdefault(usuario,{})
        base[usuario][filmes[idfilme]] = float(nota)
    return base


def euclidiana(usuario1, usuario2):
    si={}
    for item in base[usuario1]:
        if item in base[usuario2]: si[item]=1
    if len(si) == 0 :return 0
    soma = sum([pow(base[usuario1][item] - base[usuario2][item],2)
        for item in base[usuario1] if item in base[usuario2]])
    return 1/(1+sqrt(soma))

def getSimilaridade(usuario):
    similaridade = [(euclidiana(usuario, outro), outro)
        for outro in base if outro != usuario]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]

def getRecomendacoes(usuario):
	totais ={}
	somaSimilaridade={}
	
	for outro in base:
		if outro == usuario:continue
		similaridade = euclidiana(usuario, outro)
		
		if similaridade <= 0: continue

		for item in base[outro]:
			if item not in base[usuario]:
				totais.setdefault(item, 0)
				totais[item] += base[outro][item] * similaridade
				somaSimilaridade.setdefault(item,0)
				somaSimilaridade[item] += similaridade
	ranking = [(total /somaSimilaridade[item], item) for item, total in totais.items()]
	ranking.sort()
	ranking.reverse()
	return ranking[0:30]


base = carregaMovieLens()
#print(getSimilaridade('123'))
#Recomendações de filmes
print(getRecomendacoes('2'))