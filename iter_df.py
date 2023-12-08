#this function iterates over each (n) row/ col  of a df and splits it into n 1D sublists
import numpy as np

def iter_df (df, check_col):
    train_list = []
    if check_col:
        num_columns=df.shape[1]
        for i in range(num_columns):
            a = [df.iloc[:, i]]
            train_list.append(a)
        array_of_arrays = [np.array(sublist) for sublist in train_list]
        arrays_mat = np.array(array_of_arrays)

    else:
        num_rows=df.shape[0]
        for i in range(num_rows):
            a = [df.iloc[i, :]]
            train_list.append(a)
        array_of_arrays = [np.array(sublist) for sublist in train_list]
        arrays_mat = np.array(array_of_arrays)
    return(arrays_mat)