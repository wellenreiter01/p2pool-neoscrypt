import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'FED0D8C3'.decode('hex')
P2P_PORT = 9555
ADDRESS_VERSION = 56
RPC_PORT = 9554
RPC_CHECK = defer.inlineCallbacks(lambda daemon: defer.returnValue(
  'phoenixcoinaddress' in (yield daemon.rpc_help()) and
  not (yield daemon.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//1000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 90
SYMBOL = 'PXC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.getcwd(), 'data') if platform.system() == 'Windows' else os.path.expanduser('~/.phoenixcoin'), 'phoenixcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.phoenixcoin.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.phoenixcoin.org/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.phoenixcoin.org/tx/'
SANE_TARGET_RANGE = (2**256 - 1 >> 30, 2**256 - 1 >> 12)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.1e8
