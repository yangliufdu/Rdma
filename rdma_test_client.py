#!/usr/bin/python3.8
import sys
import time

sys.path.append('..')

from utils.connection import SKT, CM
from utils.param_parser import parser

from pyverbs.addr import AH, AHAttr, GlobalRoute
from pyverbs.cq import CQ
from pyverbs.device import Context
from pyverbs.enums import *
from pyverbs.mr import MR
from pyverbs.pd import PD
from pyverbs.qp import QP, QPCap, QPInitAttr, QPAttr
from pyverbs.wr import SGE, RecvWR, SendWR


RECV_WR = 1
SEND_WR = 2
GRH_LENGTH = 40

# TODO: Error handling

args = parser.parse_args()

server = not bool(args['server_ip'])

conn = CM(args['port'], args['server_ip'])


print('-' * 80)
print(' ' * 25, "Python test for RDMA")

if server:
    print("Running as server...")
else:
    print("Running as client...")

print('-' * 80)




# Handshake to exchange information such as QP Number
str1 = ''
recv1 = conn._display_recv()
if (recv1['str'] == 'start'):
    for i in range (1000):
        str1 += str(i)
    time_start = time.time()   
    for i in range (10000):
        conn.handshake(str = str1)
    if (i % 50 == 0)
        time_end = time.time()
        time_sum = time_end - time_start
        print(time_sum)
        time_start = time.time()


conn.close()

print('-' * 80)
