class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        for ch in s:
            if ch in ['(','[','{']:
                st.append(ch)
            else:
                if not st or (ch == ')' and st[-1] != '(') or (ch == ']' and st[-1] != '[') or (ch == '}' and st[-1] != '{'):
                    return False
                st.pop()
        return len(st)==0