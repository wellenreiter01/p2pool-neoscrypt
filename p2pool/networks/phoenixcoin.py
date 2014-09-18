from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['phoenixcoin']
SHARE_PERIOD = 30  # seconds
CHAIN_LENGTH = 60*60//10  # shares
REAL_CHAIN_LENGTH = 60*60//10  # shares
TARGET_LOOKBEHIND = 200  # shares
SPREAD = 20  # blocks
IDENTIFIER = '50686F656E69784C'.decode('hex')  # PhoenixL
PREFIX = '5058432D4C697665'.decode('hex')  # PXC-Live
P2P_PORT = 10555
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 10554
BOOTSTRAP_ADDRS = 'atlas.phoenixcoin.org menoetius.phoenixcoin.org prometheus.phoenixcoin.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-pxc'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Phoenixcoin to >= 0.6.6.0!' if v < 60600 else None
