NUM_TXN=100
n = 10 # n - no of peers
z0=20 # z0 percent are slow 1-z0 are fast
z1=40 # z1 percent are lowcpu and 1-z1 - high cpu
t_tx=2000 # t_tx transaction mean inter arrival time (ms)

# CONSTANTS
LOW,HIGH=0,1
L_CONN,H_CONN=4,8

# Randomly chosen constants
import random
pij = random.uniform(10,500)
fast_cij=100000 #kbps
slow_cij=5000 #kbps
dij_numerator = 96 #kbits

# Assumed Constants
NODE_LIMIT=9999 # this can only be in pattern 9,99,999,9999,etc