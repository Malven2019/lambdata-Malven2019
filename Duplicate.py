import numpy as np
import pandas as pd


def getDuplicateColumns(X):
    '''
    Get a list of duplicate columns.
    It will iterate over all the columns in dataframe and find the columns whose contents are duplicate.
    :param df: Dataframe object
    :return: List of columns whose contents are duplicates.
    '''
    duplicateColumnNames = set()
    # Iterate over all the columns in dataframe
    for x in range(X.shape[1]):
        # Select column at xth index.
        col = X.iloc[:, x]
        # Iterate over all the columns in DataFrame from (x+1)th index till end
        for y in range(x + 1, X.shape[1]):
            # Select column at yth index.
            otherCol = X.iloc[:, y]
            # Check if two columns at x and y index are equal
            if col.equals(otherCol):
                duplicateColumnNames.add(X.columns.values[y])
    return list(duplicateColumnNames)


    # Get list of duplicate columns
duplicateColumnNames = getDuplicateColumns(X)
print('Duplicate Columns in X are as follows')
for col in duplicateColumnNames:
    print('Column name : ', col)
