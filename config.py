NUM_TXN=100
n = 10 # n - no of peers
z0=20 # z0 percent are slow 1-z0 are fast
z1=40 # z1 percent are lowcpu and 1-z1 - high cpu
t_tx=2 # t_tx transaction mean inter arrival time (seconds)

# CONSTANTS
LOW,HIGH=0,1
L_CONN,H_CONN=4,8