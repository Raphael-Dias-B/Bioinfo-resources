#Codigo para criar o arquivo no formato necessario para fazer a expressão diferencial por gfold (ver Protocolo_Gfold)
mapping = open("mappings.txt")
quant = open("quant_ONF5.sf")
out = open("ONF1.read_count","w")

ref_map = mapping.readlines()
ref_quant = quant.readlines()

for linha_map in ref_map:
    fragmento = linha_map.split(" ")
    transcrito = fragmento[0].strip()
    gene = fragmento[1].strip()
    out.write(gene)
    out.write("\t")
    out.write(transcrito)
    out.write("\t")
    for linha_quant in ref_quant:
        frag_quant = linha_quant.split("\t")
        transcrito_quant = frag_quant[0].strip()
        num_reads = frag_quant[4].strip()

        if transcrito == transcrito_quant:
          out.write(num_reads)
          out.write("\t")
          out.write("0")
          out.write("\t")
          out.write("0")
          out.write("\n")
