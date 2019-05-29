from __future__ import print_function
import sys
import traceback
from hashlib import sha1
from bencode import bencode, bdecode

def get_torrent_hash(path):
    content = open(path, 'rb').read()
    metainfo = bdecode(content)
    info = metainfo[b'info']
    digest = sha1(bencode(info)).hexdigest().upper()
    return digest

if __name__ == '__main__':
    digest = get_torrent_hash(sys.argv[1])
    print(digest)
