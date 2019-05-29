# python-bencode
bencode for Python2 and Python3

Source code adopted from https://pypi.org/project/bencode/ and https://pypi.org/project/BitTorrent-bencode/.

For Python3, argument for `bdecode()` has changed to bytes, `bencode()` has changed to return bytes.
String is decoded as raw bytes (no further decoding to string with UTF-8 or other encoding) and encoded as bytes with UTF-8.

# Usage
```python
from __future__ import print_function
import sys
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
```

# License
```python
# The contents of this file are subject to the BitTorrent Open Source License
# Version 1.1 (the License).  You may not copy or use this file, in either
# source code or executable form, except in compliance with the License.  You
# may obtain a copy of the License at http://www.bittorrent.com/license/.
#
# Software distributed under the License is distributed on an AS IS basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.  See the License
# for the specific language governing rights and limitations under the
# License.

# Written by Petru Paler
```
