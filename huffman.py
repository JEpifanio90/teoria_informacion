#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Josefoo'
from heapq import heappush, heappop, heapify
from collections import defaultdict


class HuffmanCoding:
    def __init__(self):
        self.compression_ratio = 0

    def encode(self, symb2freq):
        heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
        heapify(heap)
        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] += '0'
            for pair in hi[1:]:
                pair[1] += '1'
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    def encode_default_file(self):
        symb2freq = defaultdict(int)
        with open('pagina.txt') as txtFile:
            for line in txtFile:
                for char in line:
                    symb2freq[char] += 1
            huff = self.encode(symb2freq)
            chain = ""
            output = '\n'
            for p in huff:
                output += str(p[1]) + "\n"
                chain = chain + p[0]
            self.compression_ratio = 1 / float(len(huff))
            return output