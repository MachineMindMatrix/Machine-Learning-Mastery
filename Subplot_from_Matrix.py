def matrix_2_sublist(num_col, mat):

    mat_list = []
    for i in range(num_col):
        a = [mat.iloc[:, i]]
        mat_list.append(a)
    array_of_mat_arrays = [np.array(sublist) for sublist in mat_list]
    arrays_mat = np.array(array_of_mat_arrays)
    return(arrays_mat)