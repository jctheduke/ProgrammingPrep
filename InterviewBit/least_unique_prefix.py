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
                pointer.children[index] = [self._get_node(), 1]
            else:
                new_pointer,curr_count = pointer.children[index]
                pointer.children[index] = [new_pointer, curr_count+1]
            pointer,_ = pointer.children[index]
        
        pointer.isEndOfWord = True
    
    def search(self, key):
        pointer = self.root
        for ch in key:
            index = self.__char_to_index(ch)
            if not pointer.children[index]:
                return False
            else:
                pointer,count = pointer.children[index]
        
        if pointer != None and pointer.isEndOfWord == True:
            return 1
        else:
            return 0
    
    def unique_prefix(self, key):
        pointer = self.root
        uni_pref = ""
        for ch in key:
            index = self.__char_to_index(ch)
            pointer, count = pointer.children[index]
            if count == 1:
                return (uni_pref + ch)
            else:
                uni_pref = uni_pref + ch
        return ""

# driver function 
def main(): 
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["cat", "cab", "catip","zebra", "dog", "duck", "dove"] 
    # Trie object 
    t = Trie() 
    # Construct trie 
    for key in keys: 
        t.insert(key) 
    for key in keys:
        print(key,t.unique_prefix(key))
if __name__ == '__main__': 
    main() 