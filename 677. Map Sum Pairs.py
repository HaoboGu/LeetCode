class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inner_dict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.inner_dict[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        s = 0
        for key in self.inner_dict:
            if key.startswith(prefix):
                s += self.inner_dict[key]
        return s


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)