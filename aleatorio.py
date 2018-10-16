#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

print("Digite a sequencia de acesso de blocos, sendo que QUALQUER letra determina o fim da sequencia:");
fila = [];
while (1==1):	
	entrada = raw_input();
	if (entrada.isdigit() == False):
		break;
	fila.append(entrada);
print("Digite a quantidade de linhas da memoria:");
tamanho_total = int(raw_input());
linhas = tamanho_total;
memoria = [];
while (linhas>0):
	memoria.append("T");
	linhas=linhas-1;
j = 0;
substituicao = 0;
hit = 0;
miss_compulsorio = 0;
miss_capacidade = 0;
while(len(fila)>j):		
	posicao = randint(0,tamanho_total-1);
	troca = False;		
	if (memoria[posicao] == fila[j]):
		hit+=1;
	else:
		if (memoria[posicao] == "T"):
			miss_compulsorio +=1;				
			memoria.insert(posicao, fila[j]);
			memoria.pop(posicao+1);
		else:
			miss_capacidade +=1;				
			memoria.insert(posicao, fila[j]);
			memoria.pop(posicao+1);		
		substituicao+=1;
	j+=1;
print("\nForam realizadas "+str(substituicao)+" substituicoes na memoria cache");
print("\n"+str(hit)+" Hits\n"+str(miss_compulsorio)+" Miss compulsorio\n"+str(miss_capacidade)+" Miss capacidade\n"+str(miss_compulsorio+miss_capacidade)+" Misses no total");


