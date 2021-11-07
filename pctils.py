import open_file as customfile

def getFile():
    return customfile.gui_fname().decode("utf-8")

def showColumnDistribution(df, column):
    column_values = df[column]
    print('Number of entries: ', len(column_values))

    print('\nDistribution of the column:')
    display(column_values.value_counts())

    print('\nNan Values: ', column_values.isna().sum())