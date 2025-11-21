import sys
#print(sys.executable)
import os
#print("Current working directory:", os.getcwd())
#project_root = os.path.dirname(os.path.abspath(__file__))  # script's folder
#sys.path.append(project_root)
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from os.path import expanduser
from data.pathways.gmt_pathway import get_KEGG_map

input_genes = ['AR', 'AKT', 'EGFR']
filename = expanduser('~/OneDrive/Documents/679/CS679_Project/data/pathways/MsigDB/c2.cp.kegg.v6.1.symbols.gmt')
mapp, genes, pathways = get_KEGG_map(input_genes, filename)
print('genes', genes)
print('pathways', pathways)
print('mapp', mapp)
