from Bio import Phylo
from Bio import SeqIO
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Entrez
from Bio import SeqIO
from Bio import GenBank 
import csv 
import re 
import matplotlib
import matplotlib.pyplot as plt
from Bio.Align.Applications import ClustalwCommandline
import os

def fasta_downloader():
    """" 
    La funcion fasta_downloader permite:
        1. Convertir un .txt con ids de datos de genbank en lista
        2. Para despues obtener la secuencia de cada id en formato genbank
        3. Guardar los datos obtenidos en un documento .gb del tipo genbank
    """
with open("gen1.txt", 'r+') as list:
            id_coati = list.readlines()
            Entrez.email = "gualapuro.moises@gmail.com"
            coati = []
            for ids in id_coati:
                 handle = Entrez.efetch(db="nucleotide", id=ids, rettype="gb", retmode="text")
                 secuencias = SeqIO.read(handle, "genbank")
                 coati.append(secuencias)
                 SeqIO.write(coati, "coati.gb", "genbank")
                 
                
def alignment():
    """" 
    La funcion alignment permite:
        1. Transformar el archivo tipo genbank en formato FASTA
        2. Realizar un alineamiento de secuencias usando ClustalW
    """     
    sec = SeqIO.parse('data\coati.gb', 'genbank')
    SeqIO.write(sec, "data\coati.fasta", "fasta")
      
    clustalw_exe = r"C:\Program Files (x86)\ClustalW2\ClustalW2\clustalw2.exe"
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile = "data\coati.fasta")
    assert os.path.isfile(clustalw_exe), "Clustal_W executable is missing or not found"
    stdout, stderr = clustalw_cline()
    print(clustalw_cline)

def tree():
      """
      La funcion tree:
        1. Permite realizar un calculo de distancias para formar un arbol filogenetico en formato .pdf
      """
      with open("data\coati.aln", "r") as f:
            alignment = AlignIO.read(f, "clustal")
            calculator = DistanceCalculator("identity")
            distance_matriz = calculator.get_distance(alignment)
            constructor = DistanceTreeConstructor(calculator)
            tree = constructor.build_tree(alignment)
            tree.rooted = True
            fig = plt.figure(figsize=(80, 70), dpi=200) # create figure & set the size 
            matplotlib.rc('font', size=12)              # fontsize of the leaf and node labels 
            matplotlib.rc('xtick', labelsize=20)       # fontsize of the tick labels
            matplotlib.rc('ytick', labelsize=20)       # fontsize of the tick labels
            axes = fig.add_subplot(1, 1, 1)
            Phylo.draw(tree, axes=axes)
            fig.savefig("data\coati_phylotree.pdf")
             



