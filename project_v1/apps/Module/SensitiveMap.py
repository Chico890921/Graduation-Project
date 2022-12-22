class Node:
    def __init__(self, value="\0", childtree=None):
        self.value = value
        self.childtree = childtree #point

class tree:
    
    def __init__(self):
        self.nodelist = [] #list
        
    def isempty(self):
        if (len(self.nodelist) == 0):
            return True
        return False
        
    def insertword(self, wordlist):
        
        prenode, curnode = Node(), Node()

        for word in wordlist:
            newtree, first = False, True
            curtree = self

            for value in word:
                
                curnode = Node()

                #數字特殊處理(每個詞彙的分數)
                if "1" <= value and value <="3":
                    newtree = True

                #更新level
                if first == False:
                    if newtree == True:
                        curtree = tree()
                    else:
                        if (prenode.childtree == None):
                            prenode.childtree = tree()
                        curtree = prenode.childtree
                
                #數字特殊處理(每個詞彙的分數)
                if "1" <= value and value <="3":
                    curnode.value = value
                    curtree.nodelist.append(curnode)
                    prenode.childtree = curtree
                    continue

                #判斷存不存在
                for node in curtree.nodelist:
                    if node.value == value:
                        curnode = node
                        break

                #不存在，存進去
                if curnode.value != value:
                    
                    curnode.value = value
                    curtree.nodelist.append(curnode)

                    #連接上一層
                    #第一次迴圈是沒有上一層的
                    #first == False表示prenode已經指向上一層
                    if first == False:
                        prenode.childtree = curtree
                    newtree = True
                else: #存在，不需再存
                    newtree = False

                prenode = curnode
                first = False

    #cnt 縮排
    def printtree(self, cnt):
        
        for node in self.nodelist:
            #縮排
            for i in range(cnt):
                print(end=".")
            print(node.value)
            
            if node.childtree != None:
                newlevel = tree()
                newlevel = node.childtree
                newlevel.printtree(cnt+1)
