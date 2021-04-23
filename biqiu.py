class ReDict(dict):
    def __init__(self):
        super(ReDict, self).__init__()

    def __getattribute__(self, item):
        str_ = str(item)
        try:
            return self[str_]
        except:
            return 'no such name'

    def __setattr__(self, key, value):
        str1 = str(key)
        self[str1] = value


person_data = ReDict()
person_data.name = '老王'
person_data.age = 27
person_data.dream = 'a great law man'
print(person_data)
print(person_data.hight)
