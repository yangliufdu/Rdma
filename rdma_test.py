#!/usr/bin/python3.8
import sys
import time

sys.path.append('..')

from utils.connection import SKT, CM, CommBase
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
print(args['port'])
print(args['server_ip'])
conn = CM(args['port'], args['server_ip'])


print("conn succeed");
time.sleep(2)


print('-' * 80)
print(' ' * 25, "Python test for RDMA")

if server:
    print("Running as server...")
else:
    print("Running as client...")

conn.handshake(str = "start")

# Handshake to exchange information such as QP Number

for i in range(10000):
    str = conn._display_recv()
    print(str['str'])
    print('*' * 80)
    print(i)



conn.close()
print('-' * 80)
