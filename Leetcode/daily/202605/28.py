from typing import List
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        self.min_len = float("inf")
        self.idx = float("inf")


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s: str, idx: int):
        node = self.root
        if len(s) < node.min_len:
            node.min_len = len(s)
            node.idx = idx

        for ch in s:
            c = ch
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

            if len(s) < node.min_len:
                node.min_len = len(s)
                node.idx = idx

    def query(self, s: str) -> int:
        node = self.root

        for ch in s:
            if ch in node.children:
                node = node.children[ch]
            else:
                break

        return node.idx


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        trie = Trie()

        for i, word in enumerate(wordsContainer):
            reversed_word = word[::-1]
            trie.insert(reversed_word, i)

        res = []
        for query in wordsQuery:
            reversed_query = query[::-1]
            res.append(trie.query(reversed_query))

        return res
    # TLE
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        ans = []
        for query in wordsQuery:
            n = len(query)
            best_count = -1
            best_len = float('inf')
            best_idx = 0
            for j,word in enumerate(wordsContainer):
                minimum = min(n, len(word))
                i = -1

                count = 0
                while i >= -minimum:
                    if query[i] == word[i]:
                        count += 1
                    else:
                        break
                    i -= 1
                
                if (count > best_count or 
                    (count == best_count and len(word) < best_len) or
                    (count == best_count and len(word) == best_len and j < best_idx)
                ):
                    best_count = count
                    best_len = len(word)
                    best_idx = j
                
            ans.append(best_idx)

        return ans

    # MLE
    def stringIndicesV1(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        filter_res = defaultdict(list)
        for query in wordsQuery:
            for j,word in enumerate(wordsContainer):
                minimum = min(len(query), len(word))
                i = -1

                count = 0
                while i >= -minimum:
                    if query[i] == word[i]:
                        count += 1
                    else:
                        break
                    i -= 1
                
                if count > 0:
                    filter_res[query].append((count, len(word), j))
                else:
                    filter_res[query].append((count, len(word), j))
                    
        # print(filter_res)

        ans = []
        for x in filter_res:
            filter_res[x].sort(key=lambda x: (-x[0], x[1]))
            ans.append(filter_res[x][0][-1])
        
        # print(filter_res)
        return ans
    
sol = Solution()
print(sol.stringIndices(wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]))
print(sol.stringIndices(wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]))