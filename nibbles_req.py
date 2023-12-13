# Assumes map filled with 1's
# Create map
n = 10
nsq = n*n
map = ''.join(['1' for i in range(nsq)])

# Print map
for i in range(nsq):
    if i % n == 0 and i != 0:
        print()
    print(map[i], end='')

# Print bits
print()
print("Bits")
print(nsq)

# Print nibbles
print("Nibbles")
print(hex(int(map)))