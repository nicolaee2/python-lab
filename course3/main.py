x = set() # empty set
x = {1, 2, 3}
print(x)
x = {1, 2, 2, 3, 1, 1} # {} initialization
print(x)
x = {1, 2, "AB", "ab"}
print(x)
x = set([1, 2, 3, 4]) # from list
print(x)
x = set((1, 2, 3, 4)) # from tuple
print(x)
x = set("Hello") # from string
print(x)
x = {1, 2, 3, 'A', 'C'}
# x[1] can t access
y = {1, 2, 3}
# x + y can t sum two sets
# use add
# remove throws error, discard not, clear makes the set empty
x = {1, 2, 3}
x |= {4, 5, 6}
print(x)
x.update({5, 6})
print(x)
x.update({5}, {6}, {7})
print(x)
x = {1, 2, 3}
y = {4, 5, 6}
t = {7, 8, 9}
z = x | y | t
print(z)
w = x.union(y) # can be called with multiple sets
print(w)

# use & or .intersection(set1, set2, ...) for intersection
# use - or .difference(set1, set2, ...) for difference
# use ^ or .symmetric_difference(set) for symmetric difference

# intersection_update, difference_update, symmetric_difference_update
# there is no union_update
# |=, &=, -=, ^=

# use in and not in to check existence in set
# use len to find length of set
# use isdisjoint, issubset or <=
# use issuperset or >=
# also > and < can be used.

# use pop to remove and get one element from the set. Different from remove or discard, pop returns that
# element and the popped element is from the arbitrary order of the elements in the set

# use copy for shallow copy
x = {i for i in range(0, 9)}
print(x)
# can also use map, filter, min, max, sum, anu, all, sorted, reversed
# frozenset, can t update the set

x = dict()
x = {}
x = {"A": 1, "B": 2}
print(x)
x = dict(abc=1, aaa=2)
print(x)
x = dict({"abc": 1, "aaa": 2})
print(x)
x = dict([("aaa", 1), ("abc", 2)])
print(x)
x = dict((("aaa", 1), ("abc", 2)))
print(x)
x = dict(zip(["abc", "aaa"], [1, 2]))
print(x)
# if a key doesn't exist, we can't write dict[key]
# can use in to check key existence
# can use len to count number of keys
x = {"A": 1, "B": 2}
y = x.setdefault("C", 3)
print(y)
print(x)
x.update({"A": 10})
print(x)
x.update(D=123, E=43)
print(x)

# can use del, or .clear method
# can use .copy for a shallow copy
# use static method dict.fromkeys(["A", "B"], 2)

# elements from dictionary can be accessed using get.
# get returns None, when the key isn't found
# get and pop get as second parameter the default, if doesn't exist
# pop returns error if not found and if not default

# use .keys() to get array of keys
# use .values() to get list of values
# use .items() to get an iterable

# to iterate a dictionary ascending of their values
# use sorted(x.items(), key = lambda x: x[1]):

# use ** in a function to say that that parameter is a dict
def get_smt(**dic):
    return dic.get("Hey")
print(get_smt(a=123, Hey=4))