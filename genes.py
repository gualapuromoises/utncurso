def descargar(listacc):
    with open(aa, "r") as algo: 
        gen = algo.read()
    
    Entrez.email = "gualapuro.moises@gmail.com" 
    with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id=acc) as handle:
    seq_record = SeqIO.read(handle, "fasta")
print("%s with %i features" % (seq_record.id, len(seq_record.features)))
seq_record.seq
    return(proceso)

def propiedades(proceso):

    n = len(proceso)
    return(n)

def figura(n):
    m = n+2
    return(m)