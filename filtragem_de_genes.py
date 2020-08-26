import re
transcript = open("test.txt")
#transcript = open(str(input("select reference transcript file: ")))
genes = open("reference.txt")
#genes = open(str(input("select gene file: ")))
saida= open("out.txt","w")
#saida = open(str(input("output name: ")),"w")
saida.write("Arquivo de referência: \n")
saida.write(str(transcript))
saida.write("\n")
linhas_genes = genes.readlines()
linhas_transcript = transcript.readlines()

inicio = 0

for g in linhas_genes:
    for t in linhas_transcript:
        frag = t.split("-")
        if g.strip() == frag[0]:
            saida.write(g)
            saida.write("\n")
            for i in linhas_transcript:
                if i == t:
                    inicio = 1
                
                if inicio != 0:
                    if i != t:
                        busca = re.search("[^>]*[R]*[^-| ]",i)
                        
                        if busca.group() == ">":
                            
                            inicio = 0
                            saida.write("\n")
                            
                        else:
                            saida.write(i)
                        
            

