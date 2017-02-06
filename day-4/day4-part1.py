#!/usr/bin/env python

from hashlib import md5


class AdventMiner():

    def __init__(self, secret):
        self.secret = secret

    def get_coin(self, n):
        coin_hash = self.get_hash(n)

        if coin_hash[:5] == "0" * 5:
            return coin_hash
        else:
            return False

    def get_hash(self, n):
        m = md5()
        m.update(self.secret + n)
        return m.hexdigest()

miner = AdventMiner(b"ckczppom")
index = 0
coin = False

while not coin:
    index += 1
    coin = miner.get_coin(str(index).encode())

print(index)
