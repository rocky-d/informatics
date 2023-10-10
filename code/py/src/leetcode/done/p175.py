from leetcode.util import *


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    person['city'] = [None for _ in range(len(person))]
    person['state'] = [None for _ in range(len(person))]
    for i, person_id in enumerate(person.loc[:, 'personId']):
        for j, p_id in enumerate(address.loc[:, 'personId']):
            if p_id == person_id:
                person.loc[i, 'city'] = address.loc[j, 'city']
                person.loc[i, 'state'] = address.loc[j, 'state']
                break
    return person.drop('personId', axis = 1)


person_df = pd.DataFrame({
    'personId': [1, 2, 3],
    'lastName': ['Wang', 'Alice', 'Du'],
    'firstName': ['Allen', 'Bob', 'Rocky']
})
address_df = pd.DataFrame({
    'addressId': [1, 2, 3],
    'personId': [2, 1, 3],
    'city': ['New York City', 'Leetcode', 'Sydney'],
    'state': ['New York', 'California', 'Australia']
})

print(combine_two_tables(person_df, address_df))
