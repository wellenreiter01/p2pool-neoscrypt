import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'FBC0B6DB'.decode('hex')
P2P_PORT = 9336
ADDRESS_VERSION = 14
RPC_PORT = 9337

RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 200*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 60
SYMBOL = 'FTC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Feathercoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Feathercoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.feathercoin'), 'feathercoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.feathercoin.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//10000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
