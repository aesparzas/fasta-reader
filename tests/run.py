from Bio import SeqIO

from fasta_read import FastaReader

fasta_sequences = SeqIO.parse(open('sample.fa'), 'fasta')
result = {}
for seq in fasta_sequences:
    result.update({
        seq.name: str(seq.seq)
    })
fr = FastaReader('sample.fa')
shared_items = {k: fr[k] for k in fr if k in result and fr[k] == result[k]}
assert len(shared_items) == len(fr)
