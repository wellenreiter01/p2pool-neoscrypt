from p2pool.bitcoin import networks

PARENT = networks.nets['phoenixcoin_testnet']
SHARE_PERIOD = 30  # seconds
CHAIN_LENGTH = 60*60//10  # shares
REAL_CHAIN_LENGTH = 60*60//10  # shares
TARGET_LOOKBEHIND = 200  # shares
SPREAD = 20  # blocks
IDENTIFIER = '50686F656E697854'.decode('hex')  # PhoenixT
PREFIX = '5058432D54657374'.decode('hex')  # PXC-Test
P2P_PORT = 20555
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 20554
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-pxct'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Phoenixcoin to >= 0.6.6.0!' if v < 60600 else None
