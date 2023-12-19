# task 1
print('Task 1:')
for i in ['ecoli.fasa', 'graci2.fasta', 'pneumohern.fasta']:
    print(i, ':', sep='')
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


# task 2
print('Task 2:')
with open('ecoli.fasta') as seq:
    data = seq.read().split('>')
    data.pop(0)

for seq in data:
    temp = ''.join(seq.split('\n')[1:])[0:-3]

    for i in range(int(len(temp)/3)):
        if temp[i*3:i*3 + 3] == 'TGA' or temp[i*3:i*3 + 3] == 'TAG' or temp[i*3:i*3 + 3] == 'TAA':
            print('\t', seq.split('\n')[0])
