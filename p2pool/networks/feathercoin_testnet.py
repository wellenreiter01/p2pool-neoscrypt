from p2pool.bitcoin import networks

PARENT = networks.nets['feathercoin_testnet']
SHARE_PERIOD = 30  # seconds
CHAIN_LENGTH = 60*60//10  # shares
REAL_CHAIN_LENGTH = 60*60//10  # shares
TARGET_LOOKBEHIND = 200  # shares
SPREAD = 20  # blocks
IDENTIFIER = '4665617468657222'.decode('hex')
PREFIX = 'B131010BA6D4729B'.decode('hex')
P2P_PORT = 19340
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 19328
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-ftct'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Feathercoin to >= 0.8.7.0!' if v < 80700 else None
