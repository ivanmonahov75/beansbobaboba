from matplotlib import pyplot as plt

# task 1
print('Task 1:')
for bac in ['ecoli.fasta', 'graci2.fasta', 'pneumohern.fasta']:
    print(bac, ':', sep='')
    with open(bac) as file:
        data = file.read().split('>')[1:]

        codons = []
        for seq in data:
            codons.append(''.join(seq.split('\n')[1:])[0:3])

        codons_sorted = sorted(list(set(codons)))
        try:
            codons_sorted.remove('')
        except:
            pass

        for codon in codons_sorted:
            print(f'\t{codon}\t{codons.count(codon)}')


# task 2
print('Task 2:')
with open('ecoli.fasta') as file:
    data = file.read().split('>')[1:]

    for seq in data:
        temp = ''.join(seq.split('\n')[1:])[0:-3]

        for i in range(int(len(temp)/3)):
            if temp[i*3:i*3 + 3] == 'TGA' or temp[i*3:i*3 + 3] == 'TAG' or temp[i*3:i*3 + 3] == 'TAA':
                print('\t', seq.split('\n')[0])
                break

# task 3
print('Task 3:')
for bac in ['ecoli.fasta', 'graci2.fasta', 'pneumohern.fasta']:
    print(bac, ':', sep='')
    with open(bac) as seq:
        data = seq.read().split('>')
        data.pop(0)
        codons = []
        for i in data:
            temp = ''.join(i.split('\n')[1:])
            try:
                codons.append(''.join((temp[-3], temp[-2], temp[-1])))
            except:
                pass
        codons_s = sorted(list(set(codons)))
        try:
            codons_s.remove('')
        except:
            pass
        for i in codons_s:
            print(f'\t{i}\t{codons.count(i)}')


# task 4
print('Task 4:')
for bac in ['ecoli.fasta', 'graci2.fasta', 'pneumohern.fasta']:
    print(bac, ':', sep='')

    with open(bac) as seq:
        data = seq.read().split('>')[1:]

        cod = dict.fromkeys(['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'], 0)
        with open('out.txt', 'w') as ans:
            prot = []
            for i in data:
                prot.append(''.join(i.split('\n')[1:]))

            prot = ''.join(prot)
            for i in range(int(len(prot)/3)):
                try:
                    cod[prot[i*3:i*3 + 3]] += 1
                except:
                    pass

            for i in cod.keys():
                print(f'\t{i}\t{cod[i]}')

# task 5
print('Task 5:', sep='')
with open('ecoli_full.fasta') as seq:
    data = seq.read().split('>')
    data.pop(0)
    data = ''.join(data[0].split('\n'))
    prot = []
    for i in data:
        prot.append(''.join(i.split('\n')[1:]))

    window, step = 100000, 1000
    gc_sum = 0
    loc = []
    glob = []
    for i in range(int(len(data) / step)):
        temp = data[i * step:i * step + window]
        if len(temp) < window:
            break
        try:
            gc = (temp.count('G') - temp.count('C')) / (temp.count('G') + temp.count('C'))
        except ZeroDivisionError:
            gc = 0
        gc_sum += gc
        loc.append(gc)
        glob.append(gc_sum)
    print('\t', gc_sum)

plt.figure(figsize=(30, 10))
# un comment for second graph
# plt.plot(loc, label='Current')
# plt.legend()
# plt.show()
plt.plot(glob, label='Global')
plt.legend()
plt.show()
