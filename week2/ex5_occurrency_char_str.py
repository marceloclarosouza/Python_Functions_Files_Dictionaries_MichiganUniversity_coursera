#Print the counts of each characters

txt = "Textos, fotos, artes e vídeos da Folha estão protegidos pela legislação brasileira sobre direito autoral. Não reproduza o conteúdo do jornal em qualquer meio de comunicação, eletrônico ou impresso, sem autorização da Folhapress (pesquisa@folhapress.com.br). As regras têm como objetivo proteger o investimento que a Folha faz na qualidade de seu jornalismo. Se precisa copiar trecho de texto da Folha para uso privado, por favor logue-se como assinante ou cadastrado."
char_counts = {}#creating empty dictionary

for char in txt:
    if char not in char_counts:
        char_counts[char] = 0#strsting the count for a new char
    
    char_counts[char] += 1#accumulate to a previous identified char
    
for char in char_counts.keys():#print the keys of the dictionary
    print(char + " " + str(char_counts[char]))