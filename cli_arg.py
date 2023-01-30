import sys
if len(sys.argv) < 5:
    print("To run use : main.py <num-peers> <percent-slow> <percent-lowcpu> <mean-interarrival-time>")
    print("arg count less than 5")
    exit(-1)
n=int(sys.argv[1])
z0=int(sys.argv[2])
z1=int(sys.argv[3])
t_tx=float(sys.argv[4])