import zoo
import zoo as menagerie
from zoo import hours
from zoo import hours as info
from collections import OrderedDict
from collections import defaultdict

# 11.1
zoo.hours()


# 11.2
menagerie.hours()


# 11.3
hours()


# 11.4
info()


# 11.5
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)


# 11.6
fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)


# 11.7
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])
