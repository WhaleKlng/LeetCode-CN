# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。 
# 
#  有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
#  和 "192.168@1.1" 是 无效的 IP 地址。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  输入：s = "1111"
# 输出：["1.1.1.1"]
#  
# 
#  示例 4： 
# 
#  输入：s = "010010"
# 输出：["0.10.0.10","0.100.1.0"]
#  
# 
#  示例 5： 
# 
#  输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3000 
#  s 仅由数字组成 
#  
#  Related Topics 字符串 回溯算法 
#  👍 414 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(track, start, s):
            # 满四段且用光所有字符串
            if len(track) == 4 and start == len(s):
                res.append('.'.join(track))
            # 满四段但没用光所有字符串
            if len(track) == 4 and start < len(s):
                return

            for l in range(1, 4):
                # 字符不存在,超出边界，最后一个字符的索引为s[start + l - 1]
                if start + l - 1 >= len(s):
                    return
                # 若选择长度超过2的字串，则不能是'0'开头
                if l >= 2 and s[start] == "0":
                    return
                tmp = s[start:start + l]
                # 长度为3的字串，取值不能大于225
                if l == 3 and int(tmp) > 255:
                    return
                backtrack(track + [tmp], start + l, s)

        backtrack([], 0, s)
        return res
# leetcode submit region end(Prohibit modification and deletion)
