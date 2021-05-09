# samochody = ['syrena', 'polonez', 'ferrari', 'dacia']
#
# print(samochody[0])
# print(samochody[1])
# for s in samochody:
#  print(s)
# for idx in range( len(samochody) ) :
#     print("idx: " + str(idx) + " : " + samochody[idx])



kolory = ['white', 'black', 'green', 'pink', 'blue']

print(kolory)
print(kolory[0])
print(kolory[1])
print(kolory[4])

print("--- po for ---")
for kolor in kolory:
    print("===")
    print(kolor)

print("--- po idx w petli ------------")

for idx in range(len(kolory)):
    print(idx,kolory[idx])
