# 11.1
import zoo
zoo.hours()

# 11.2
import zoo as menagerie
menagerie.hours()

# 11.3
from zoo import hours
hours()

# 11.4
from zoo import hours as info
info()

# 11.5
plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

# 11.6
from collections import OrderedDict
plain = OrderedDict([
    ('a', 1),
    ('b', 2),
    ('c', 3),
])
for (key, value) in plain.items():
    print(f'{key}: {value}')

# 11.7
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])