class ReDict(dict):
    def __init__(self):
        super(ReDict, self).__init__()

    def __getattr__(self, item):
        str1 = str(item)
        try:
            return self[str1]
        except:
            print('NO such name')

    def __getattribute__(self, item):
        str1 = str(item)
        return self[str1]

    def __setattr__(self, key, value):
        str1 = str(key)
        self[str1] = value


re_dict = ReDict()
re_dict.name = '老王'
re_dict.age = 27
re_dict.dream = 'a great law man'
print(re_dict)
