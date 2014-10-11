import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'DAAFA5BA'.decode('hex')
P2P_PORT = 19336
ADDRESS_VERSION = 65
RPC_PORT = 19337
RPC_CHECK = defer.inlineCallbacks(lambda daemon: defer.returnValue(
  'feathercoinaddress' in (yield daemon.rpc_help()) and
  (yield daemon.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 60
SYMBOL = 'FTCt'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Feathercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Feathercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.feathercoin'), 'feathercoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com:3080/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com:3080/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com:3080/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
