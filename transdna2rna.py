# gathers user input for a DNA seq and converts it to a list
sample = input("Enter a DNA seq: ")
samp_list = list(sample)

# for any DNA seq less than 1 Mbp long, substitutes any T's in the DNA seq list (samp_list) for U's
i = 0
for i in range(1000000):
  try:
    if samp_list[i] == 'T':
      samp_list.remove('T')
      samp_list.insert(i,'U')
      i += 1
  except IndexError:
    pass

# converts the modified list into a string and prints output
rna = ''.join(samp_list)
print(rna)
