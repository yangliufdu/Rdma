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

if args['qp_type'] == IBV_QPT_UD and args['operation_type'] != IBV_WR_SEND:
    print("UD QPs don't support RDMA operations.")
    conn.close()


ctx = Context(name=args['ib_dev'])
pd = PD(ctx)
cq = CQ(ctx, 100)

cap = QPCap(max_send_wr=args['tx_depth'], max_recv_wr=args['rx_depth'], max_send_sge=args['sg_depth'],
            max_recv_sge=args['sg_depth'], max_inline_data=args['inline_size'])
qp_init_attr = QPInitAttr(qp_type=args['qp_type'], scq=cq, rcq=cq, cap=cap, sq_sig_all=True)
qp = QP(pd, qp_init_attr)

gid = ctx.query_gid(port_num=1, index=args['gid_index'])

# Handshake to exchange information such as QP Number
str1 = ''
recv1 = conn._display_recv()
if (recv1['str'] == 'start'):
    for i in range (10000):
        str1 += str(i)
    time_start = time.time()   
    for i in range (10):
        conn.handshake(str = str1)
    time_end = time.time()
    time_sum = time_end - time_start
    print(time_sum)


conn.close()

print('-' * 80)
