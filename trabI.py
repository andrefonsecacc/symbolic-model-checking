class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.item = None
		#self.pai=pai
		self.esq=None # False
		self.dir=None # True
		self.label = None

	def inorder(self):
                self.inordertab2(0)
        def inordertab2(self,tab):
                if self is not None:
                        if self.esq is not None:
                        	self.esq.inordertab2(tab+3)
                        print(" "*tab+str(self.item)+"#"+str(self.label))
                        if self.dir is not None:
                        	self.dir.inordertab2(tab+3)

List_label = [(0,0),(1,1),(0,1),(1,0)] # pares de labels
#tabela_res = [1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0] # resultado da tabela de verdade
tabela_res = [0,1,0,1,0,0,0,0]
#var = ['x1','y1','x2','y2'] # ordem da arvore
var = ['z','x','y']
arv=Tree()
arv_reduce = Tree()
j=0


def fill_tree(arv,i):
	if(i<len(var)):
		arv.esq = Tree()
		arv.dir = Tree()
		
		arv.esq.item = var[i]
		arv.dir.item = var[i]

		fill_tree(arv.esq,i+1)
		fill_tree(arv.dir,i+1)
	else:
		global j
		arv.esq=Tree()
		arv.esq.item = str(tabela_res[j])
		arv.esq.label = tabela_res[j] #atribuir label ao ultimo nivel
		arv.dir = Tree()
		arv.dir.item = str(tabela_res[j+1])
		arv.dir.label = tabela_res[j+1] #atribuir label ao ultimo nivel
		j=j+2
		return

def labelling(arv):
	if arv.label is None:
		if arv.esq.label is None:
			labelling(arv.esq)
		if arv.dir.label is None:
			labelling(arv.dir)
		if arv.esq.label == arv.dir.label:
			arv.label = arv.esq.label
		else:
			par = (arv.esq.label,arv.dir.label)
			#if filter(par,List_label) == true
			#print(List_label.index(par))
			#print(List_label.count(par))
			if List_label.count(par)==1:
				arv.label=List_label.index(par)
			else:
				List_label.append(par)
				arv.label=List_label.index(par)
	
def fill_tree_reduce(tree,r_tree):
	global List_label
	if(tree.esq == None and tree.dir == None):
		return
	elif(tree.esq.label==tree.dir.label):
		if (List_label[int(tree.esq.label)][0]!=List_label[int(tree.esq.label)][1]):
			r_tree.item = tree.item
			r_tree.esq= Tree()
			r_tree.dir = Tree()
			r_tree.esq.item=List_label[int(tree.esq.label)][0]
			r_tree.dir.item=List_label[int(tree.esq.label)][1]
		else:
			r_tree.item = List_label[int(tree.esq.label)][0]
		return
	else:
		r_tree.item=tree.item
		r_tree.esq=Tree()
		r_tree.dir=Tree()
		r_tree.esq.item=tree.esq.item
		r_tree.dir.item=tree.dir.item
		fill_tree_reduce(tree.esq,r_tree.esq)
		fill_tree_reduce(tree.dir,r_tree.dir)


arv.item= var[0]
fill_tree(arv,1)
#arv.inorder()
labelling(arv)
arv.inorder()
print("------------------------")
fill_tree_reduce(arv,arv_reduce)
arv_reduce.inorder()
#arv_reduce.item=arv.item;
#print(arv_reduce.item)