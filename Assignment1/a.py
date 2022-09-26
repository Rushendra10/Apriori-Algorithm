import sys
from itertools import combinations

n = len(sys.argv)

if (n==4):
    DBFILE = sys.argv[1]
    MINSUP = float(sys.argv[2])
    MINCONF = float(sys.argv[3])

else:
    print("Improper command line arguments")


file = open(DBFILE, 'r')
lines = file.readlines()

# print(len(lines))

transactions = []

NUM_TRANS = len(transactions)

for line in lines:

    t = line.strip().split(", ")
    transactions.append(t)

# print(transactions)
NUM_TRANS = len(transactions)

##########################################################################################

unique_items = set()

for t in transactions:

    for i in range(len(t)):

        unique_items.add(t[i])

unique_items = list(unique_items)
unique_items.sort()
# print(unique_items)

maxtran = max(transactions, key=lambda t: len(t))

L1 = []
support = {}

for i in range(0, len(unique_items)):

    cnt=0

    for j in range(0, len(transactions)):

        if (unique_items[i] in transactions[j]):
            cnt+=1

    if (cnt>MINSUP*NUM_TRANS):

        L1.append(set([unique_items[i]]))
        support[frozenset([unique_items[i]])] = cnt

# print(len(L1))

# print(L1)
# print(list(L1[0]))

def find_LK(LK_1, k):
    
    candidates = []

    for i in range(0, len(LK_1)):

        for j in range(i+1, len(LK_1)):

            l1 = sorted(list(LK_1[i]))[:k-2]
            l2 = sorted(list(LK_1[j]))[:k-2]


            

            if (l1==l2):

                l1 = set(LK_1[i])
                l2 = set(LK_1[j])

                # print(l1)
                # print(l2)
                # print("-"*30)

                l1 = frozenset(l1.union(l2))

                candidates.append(l1)

    sup_cnt = {}

    for c in candidates:

        for t in transactions:

            # print(list(c))
            # print(t)
            

            if (c.issubset(t)):

                # print("true")

                if (c not in sup_cnt):
                    sup_cnt[c] = 1

                else:
                    sup_cnt[c]+=1
            
            # print("-------")

    # print(sup_cnt)

    LK = []
    supportk = {}

    for c, cnt in sup_cnt.items():
        
        # print(c, cnt)
        sup = int(cnt)/NUM_TRANS

        if (sup>MINSUP):
            LK.append(c)
            supportk[c] = cnt

    return LK, supportk 

# LK, sup = find_LK(L1, 2)


# print(LK)


def apriori():

    L = L1
    k=1

    tables = []
    sups = []

    tables.append(L1)
    sups.append(support)

    while(True):

        # print("in loop")

        k+=1

        LK, sup = find_LK(L, k)

        L = LK

        if (len(LK)==0):
            break

        else:
            tables.append(LK)
            sups.append(sup)

    return tables, sups


table, sups = apriori()

# sups[1][]

# print(table)
# print(sups)

# print(sups.index(frozenset({'I3', 'I4'})))
# print(type(sups[1]))

# print(type(table[0]))


class Rule:

    def __init__(self, left, right, table, sups):
        self.left = left
        self.right = right
        self.table = table
        self.sups = sups

    def __str__(self):
        
        # return ("{" + str(self.left) + "}" + "->" + "{" + str(self.right) + "}")
        return (str(self.left) + str(self.right) + "[" + str(self.support()) + " " + str(round(self.confidence(), 4)) + "]")

    def __eq__(self, other):

        return (self.left==other.left and self.right==other.right)

    def support(self):
        
        n1 = len(self.left)
        n2 = len(self.right)

        ind = n1+n2-1

        union = self.left.union(self.right)

        if (len(union)!=n1+n2):
            return -1

        # print(type(union))

        sup_cnt = sups[ind][frozenset(union)]

        # print(sup_cnt)

        support = sup_cnt/NUM_TRANS

        return support

    def confidence(self):

        n1 = len(self.left)
        n2 = len(self.right)

        union = self.left.union(self.right)

        if (len(union)!=n1+n2):
            return -1

        sup_union = sups[n1+n2-1][frozenset(self.left.union(self.right))]

        sup_left = sups[n1-1][frozenset(self.left)]

        conf = sup_union/sup_left

        return conf

#######################################################################

rules = []

for i in table:

    if (table.index(i)!=0):

        for j in i:

            # print(list(j))

            comb = []

            for k in range(len(j)+1):

                comb += [list(x) for x in combinations(j, k)]
            
            # print(comb)

            reqd_subsets = filter(lambda item: len(item) > 0 and len(item)<len(j), comb)

            reqd_subsets = list(reqd_subsets)

            for x in range(0, len(reqd_subsets)):
                for y in range(0, len(reqd_subsets)):

                    if (x!=y):
                        rule = Rule(set(reqd_subsets[x]), set(reqd_subsets[y]), table, sups)
                    
                        # print(rule)

                        if (rule.support()!=-1):
                            rules.append(rule)
                        

strong_rules = []

for rule in rules:
    if (rule.confidence()>MINCONF):
        print(rule)
        strong_rules.append(rule)


# print(table)
