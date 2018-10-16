#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
fila_memoria = [];
while(len(fila)>j):	
	troca = False;		
	if (troca == False):
		for indice, bloco in enumerate(memoria):			
			if (bloco == "T"):			
				memoria.insert(indice, fila[j]);
				memoria.pop(indice+1);
				fila_memoria.append(fila[j]);
				troca = True;
				miss_compulsorio +=1;
				break;
			if (fila[j]==bloco):
				troca = True;
				hit+=1;
				for i, bloco_fila in enumerate(fila_memoria):
					if (fila[j] == bloco_fila):	
						bloco_aux = bloco_fila;
						fila_memoria.pop(i);
						fila_memoria.append(bloco_aux);
				break;
		if (troca == False):
			miss_capacidade +=1;
			bloco_mais_antigo = fila_memoria[0];	
			fila_memoria.pop(0);
			for indice, bloco in enumerate(memoria):	
				if (bloco == bloco_mais_antigo):
					memoria.insert(indice, fila[j]);
					memoria.pop(indice+1);
					fila_memoria.append(fila[j]);
					break;
			substituicao=substituicao+1;
	j+=1;
print(memoria);
print("\nForam realizadas "+str(substituicao)+" substituicoes na memoria cache");
print("\n"+str(hit)+" Hits\n"+str(miss_compulsorio)+" Miss compulsorio\n"+str(miss_capacidade)+" Miss capacidade\n"+str(miss_compulsorio+miss_capacidade)+" Misses no total");


