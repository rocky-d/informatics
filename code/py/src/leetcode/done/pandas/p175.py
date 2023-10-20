from rockyutil.leetcode import *


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    return person.merge(address, on = 'personId', how = 'left').loc[:, ['firstName', 'lastName', 'city', 'state']]


person_df = pd.DataFrame({
    'personId': [1, 2, 3],
    'lastName': ['Wang', 'Alice', 'Du'],
    'firstName': ['Allen', 'Bob', 'Rocky']
})
address_df = pd.DataFrame({
    'addressId': [1, 2, 3],
    'personId': [2, 1, 5],
    'city': ['New York City', 'Leetcode', 'Sydney'],
    'state': ['New York', 'California', 'Australia']
})

print(combine_two_tables(person_df, address_df))
