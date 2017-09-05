import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'E4EFDBFD'.decode('hex')
P2P_PORT = 17298
ADDRESS_VERSION = 66
RPC_PORT = 17299
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
  'trezarcoin_address' in (yield bitcoind.rpc_help()) and
  not (yield bitcoind.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 100*100000000 >> (height + 1)//1600000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 90
SYMBOL = 'TZC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Trezarrcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Trezarcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.trezarcoin'), 'trezarcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
