from matplotlib import pyplot as plt

# task 1
print('Task 1:')
for i in ['ecoli.fasta', 'graci2.fasta', 'pneumohern.fasta']:
    print(i, ':', sep='')
    with open(i) as seq:
        data = seq.read().split('>')
        data.pop(0)
        codons = []
        for i in data:
            codons.append(''.join(i.split('\n')[1:])[0:3])
        codons_s = sorted(list(set(codons)))
        try:
            codons_s.remove('')
        except:
            pass
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

print('Task 3:')
for i in ['ecoli.fasta', 'graci2.fasta', 'pneumohern.fasta']:
    print(i, ':', sep='')
    with open(i) as seq:
        data = seq.read().split('>')
        data.pop(0)
        codons = []
        # temp = ''.join(data[1].split('\n')[1:])
        # print(''.join((temp[-3], temp[-2], temp[-1])))
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

print('Task 4:')
for i in ['ecoli.fasta', 'graci2.fasta', 'pneumohern.fasta']:
    print(i, ':', sep='')
    with (open(i) as seq):
        data = seq.read().split('>')
        data.pop(0)
        cod = dict.fromkeys(['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG' ], 0)
        with open('out.txt', 'w') as ans:
            prot = []
            for i in data:
                prot.append(''.join(i.split('\n')[1:]))


            for i in range(len(prot)):
                prot[i] = ''.join(list(prot[i])[:-3])
            prot = ''.join(prot)
            for i in range(int(len(prot)/3)):
                try:
                    cod[prot[i*3:i*3 + 3]] += 1
                except:
                    pass



            for i in cod.keys():
                print(f'\t{i}\t{cod[i]}')

print('Task 5:', sep='')
with open('ecoli_full.fasta') as seq:
    data = seq.read().split('>')
    data.pop(0)
    data = ''.join(data[0].split('\n'))
    with open('out.txt', 'w') as ans:
        prot = []
        for i in data:
            prot.append(''.join(i.split('\n')[1:]))

        window, step = 100000, 1000
        gc_sum = 0
        # data = ''.join(prot)
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
            ans.write(f'{i * step}\t{gc:.3f}\t{gc_sum:.3f}\n')
            loc.append(gc)
            glob.append(gc_sum)
        print('\t', gc_sum)
plt.figure(figsize=(30, 10))
# plt.plot(loc, label='Current')
# plt.legend()
# plt.show()
plt.plot(glob, label='Global')
plt.legend()
plt.show()
