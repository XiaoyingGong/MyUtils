# author: 龚潇颖 Gong, Xiaoying
# IDE: PyCharm
# Time：2022/7/14 9:32
# Email: gongxiaoying5991@163.com
# des:交并集工具，用于合并区域，我使用的场景在于合并同一个活动区（150角秒范围内）的增亮区域
# 主要包含两个类：1、处理交并集的‘UnionFind’ 2、处理输入数据结构的‘SampleTree’
# 通过输入的树的根来判断。
# 1、判断根在不在已有的根列表里，如果在则并入，如果不在执行2
# 2、如果不在已有的根列表中，则在每个根的叶子节点查询，是否在其中，如果在，则其并入该叶子节点的根当中，否则执行3
# 3、在1和2都不符合的情况下，直接根据输入的根节点在并查集中新建一个根节点

class UnionFind:
    def __init__(self):
        self.union_find_set = {}

    # father == None证明没找到
    def find(self, input_root):
        roots = list(self.union_find_set.keys())
        father = None
        if father in roots:
            father = input_root
        # 已经有了
        else:
            for root in roots:
                if input_root in self.union_find_set[root]:
                    father = root
        return father

    def merge(self, input_root, input_leafs):
        father = self.find(input_root)
        # 如果father == None, 就自己成为father
        if father == None:
            self.union_find_set[input_root] = input_leafs
        else:# 找到了father
            self.union_find_set[father] = self.union_find_set[father] | input_leafs
        return True

    # 从定义的SampleTree组成的list来构建并查集
    def init_union_find_by_SampleTree_list(self, sample_tree_list):
        for cur_sample_tree in sample_tree_list:
            cur_root, cur_son_set = cur_sample_tree.get_data()
            self.merge(cur_root, cur_son_set)
        return self.union_find_set


# 数据结构用来放未进入并查集前的数据
class SampleTree:
    def __init__(self, root, son_set):
        self.root = root
        self.son_set = son_set

    def get_data(self):
        return self.root, self.son_set

if __name__ == '__main__':
    # --------------------- 构建实验数据 ---------------------
    # 如果要保证leaf的值的唯一性，输入一定要为set（集合）
    t1 = SampleTree(1, {1, 2, 3, 7})
    t2 = SampleTree(3, {3, 4, 5})
    t3 = SampleTree(2, {2, 3, 7})
    t4 = SampleTree(3, {3, 11, 12})
    t5 = SampleTree(1, {1, 2, 3, 111, 222})
    t6 = SampleTree(10, {10})
    t_list = [t1, t2, t3, t4, t5, t6]

    # ------------------ 构建并查集 ------------------
    union_find = UnionFind()
    result = union_find.init_union_find_by_SampleTree_list(t_list)

    print(result)
