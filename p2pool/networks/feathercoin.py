from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['feathercoin']
SHARE_PERIOD = 30  # seconds
CHAIN_LENGTH = 60*60//10  # shares
REAL_CHAIN_LENGTH = 60*60//10  # shares
TARGET_LOOKBEHIND = 200  # shares
SPREAD = 120  # blocks
IDENTIFIER = '4665617468657221'.decode('hex')
PREFIX = 'B131010BA6D4729A'.decode('hex')
P2P_PORT = 19339
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 19327
BOOTSTRAP_ADDRS = 'p2pool.neoscrypt.de pool.maeh.org pool2.maeh.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-ftc'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Feathercoin to >= 0.8.7.1!' if v < 80700 else None
  