

#### Sets ####

""" Set is a collection of items.
    A a collection of unordered and un-indexed distinct elements. 
"""
# syntax
st = set()

""" Examples with sets """

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

""" We use len() method to find the length of a set """

len(it_companies)
# To see the length
# length = len(it_companies)
# print(length)
""" Adding items to a set """
it_companies.add("Twiter") # One item
it_companies.update(["Nvidia", "Meta", "Samsumg"]) # Multiple items

""" We can remove an item from a set using remove() and discard() method """
it_companies.remove("Meta")
it_companies.discard("Twiter") # If the item is not found remove() method will raise errors. However, discard() method doesn't raise any errors.

""" We can join two sets using the union() or update() method."""
#a_and_b = A.union(B) # Union This method returns a new set
#A.update(B) # A new set is not created, B contents are added to A

""" Finding Intersection Items """
A.intersection(B) # returns a set of items which are in both the sets

""" A set can be a subset or super set of other sets """
A.issubset(B) # return True or False
A.issuperset(B) # return True or False

""" If two sets do not have a common item or items we call them disjoint sets."""
B.isdisjoint(A) # False becase there are common items

""" Symmetric Difference Between Two Sets """
A.symmetric_difference(B) #returns a set that contains all items from both sets, except items that are present in both sets

""" Deleting a Set """
del A, B

""" Converting List to Set """
list_age = list(age)

""" Difference Between Two Sets"""
len_age = len(age)
len_list_age = len(list_age)

print(len_age)
print(len_list_age)