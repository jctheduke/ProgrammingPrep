class TrieNode(object):

    def __init__(self):
        self.children = [None]* 26
        self.isEndOfWord = False

class Trie(object):

    def __init__(self):
        self.root = self._get_node()
    
    def _get_node(self):
        return TrieNode()
    
    def __char_to_index(self,ch):
        return ord(ch)-ord('a')
    
    def insert(self, key):
        pointer = self.root

        for ch in key:
            index = self.__char_to_index(ch)
            if not pointer.children[index]:
                pointer.children[index] = self._get_node()
            pointer = pointer.children[index]
        
        pointer.isEndOfWord = True
    
    def search(self, key):
        pointer = self.root
        for ch in key:
            index = self.__char_to_index(ch)
            if not pointer.children[index]:
                return False
            else:
                pointer = pointer.children[index]
        
        if pointer != None and pointer.isEndOfWord == True:
            return True
        else:
            return False

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        good_words = A.split('_')
        t = Trie() 
        # Construct trie 
        for key in good_words: 
            t.insert(key)
        
        good_score = {}
        for i,x in enumerate(B):
            for word in x.split('_'):
                good_score[i] = good_score.get(i,0) + (1 if t.search(word) else 0)
        return [x[0] for x in sorted(good_score.items(), key=lambda x: -x[1])]
A = "play_boy"
B = [ "smart_guy", "girl_and_boy_play", "play_ground" ]
s = Solution()
print(s.solve(A, B))