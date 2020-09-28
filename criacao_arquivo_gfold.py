#Codigo para criar o arquivo no formato necessario para fazer a expressão diferencial por gfold (ver Protocolo_Gfold)
#Abrir os arquivos que serão usados e criar o output
mapping = open("mappings.txt")
quant = open("quant_ONF5.sf")
out = open("ONF1.read_count","w")

#Criar referência de leitura de linha por linha do mapping e da quantificação do Salmon
ref_map = mapping.readlines()
ref_quant = quant.readlines()

#Marcador - validar se o transcrito achou uma correspondência no final da busca
marcador = 0

#Primeira referencia - cada linha do mapping (estruturada em "Transcrito/Gene")
for linha_map in ref_map:
    #Separar transcrito do gene
    fragmento = linha_map.split(" ")
    transcrito = fragmento[0].strip()
    gene = fragmento[1].strip()
    #Escrever o transcrito e o gene no output
    out.write(gene)
    out.write("\t")
    out.write(transcrito)
    out.write("\t")
    marcador = 0
    #Correr um laço no aquivo de quantificação para achar a referência do transcrito
    for linha_quant in ref_quant:
        #Separar o arquivo em todos os seus fragmentos (Transcrito/Lenght/predicted Lenght/TPM/Numreads)
        frag_quant = linha_quant.split("\t")
        transcrito_quant = frag_quant[0].strip()
        num_reads = frag_quant[4].strip()
        #identificar correspondencia entre transcrito da vez e o transcrito buscado
        if transcrito == transcrito_quant:
            marcador = 1
            out.write(num_reads)
            out.write("\t")
            out.write("0")
            out.write("\t")
            out.write("0")
            out.write("\n")

        #Verificar, ao final da busca, se houve busca equivalente
        if transcrito_quant == "TCONS_00031912":
            if marcador == 0:
                out.write("Não encontrado")
                out.write("\t")
                out.write("0")
                out.write("\t")
                out.write("0")
                out.write("\n")
