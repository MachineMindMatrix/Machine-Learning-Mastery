def entry_count(df, col_name, descending=False, visu=True, entries=10, delimiter=','):
    """counts and outputs the most occuring entrys in a dataset. Can also handle multiple entrys divided by symbols like ; or ,"""

    # takes object with several entries, splits them up and generates a flat list
    df['new_col'] = df[col_name].str.split(delimiter)
    entry_list = df['new_col'].explode().tolist()

    if descending:
        desc = True
    else:
        desc = False

    # create a dictionary with every entry listed and count the number of occurrences
    entry_count = {}
    # create an empty dict and iterate over all entries
    for entry in entry_list:
        if entry in entry_count:
            entry_count[entry] += 1
        else:
            entry_count[entry] = 1

    entries_sorted = dict(sorted(entry_count.items(), key=lambda item: item[1], reverse=desc))

    # plot n most/ least occuring entries
    fig, ax = plt.subplots()
    for index, (key, value) in enumerate(entries_sorted.items()):
        if index < entries:
            entry = [key]
            counts = investors_sorted[key]

            ax.bar(entry, counts)
            ax.set_ylabel('number of entries')
            plt.xticks(rotation=80)
            plt.style.use('dark_background')
            if descending:
                ax.set_title('Most occuring Entries')
            else:
                ax.set_title('Least occuring Entries')
        else:
            break
    plt.show()