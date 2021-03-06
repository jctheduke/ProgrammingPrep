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

# driver function 
def main(): 
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["cat", "cab", "catip"] 
    output = ["Not present in trie", "Present in trie cat catip"] 
    # Trie object 
    t = Trie() 
    # Construct trie 
    for key in keys: 
        t.insert(key) 
    # Search for different keys 
    print("{} ---- {}".format("cat",output[t.search("the")])) 
    print("{} ---- {}".format("cab",output[t.search("these")])) 
    print("{} ---- {}".format("catnip",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")])) 

if __name__ == '__main__': 
    main() 