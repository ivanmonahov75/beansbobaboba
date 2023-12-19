# task 1

for i in ['ecoli.fasa', 'graci2.fasta', 'pneumohern.fasta']:
    print(i)
    with open('ecoli.fasta') as seq:
        data = seq.read().split('>')
        data.pop(0)
        codons = []
        for i in data:
            codons.append(''.join(i.split('\n')[1:])[0:3])
        codons_s = sorted(list(set(codons)))
        codons_s.remove('')
        for i in codons_s:
            print(f'\t{i}\t{codons.count(i)}')
