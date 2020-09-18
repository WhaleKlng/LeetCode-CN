# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成
# 了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 
# 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。 
# 
#  在结果列表中，选择字典序最小的名字作为真实名字。 
# 
#  示例： 
# 
#  输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], sy
# nonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
# 输出：["John(27)","Chris(36)"] 
# 
#  提示： 
# 
#  
#  names.length <= 100000 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 13 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict

class UnionFind(object):
    def __init__(self, names):
        self.parent = {}
        for name in names:
            self.parent[name] = name

    def union(self, a, b):
        if a not in self.parent or b not in self.parent:
            return
        root_a = self.find_root(a)
        root_b = self.find_root(b)
        if root_a < root_b:
            self.parent[root_b] = root_a
        else:
            self.parent[root_a] = root_b

    def find_root(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        freq_map = defaultdict(int)
        for name_freq in names:  # part：“john 15)"
            # print(name_freq)
            # print(name_freq.split('('))
            name, freq_str = (part.strip().strip(')') for part in name_freq.split('('))
            freq_map[name] = int(freq_str)
        # print(freq_map)
        # 初始化并查集
        uf = UnionFind(freq_map.keys())
        # print(freq_map.keys())
        # 并操作
        for pair_str in synonyms:
            a, b = (name.strip().strip(')').strip('(') for name in pair_str.split(','))
            uf.union(a, b)
        # 生成结果
        result = []
        res_map = defaultdict(int)
        for name, freq in freq_map.items():
            res_map[uf.find_root(name)] += freq
        for name, freq in res_map.items():
            result.append('{}({})'.format(name, freq))
        return result
# leetcode submit region end(Prohibit modification and deletion)
