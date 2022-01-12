'''
Dictionaries for Data Science
Link for dataset (https://datacatalog.worldbank.org/search/dataset/0037712)
'''


# Pre-defined lists
feature_names = ['CountryName', 'CountryCode',
                 'IndicatorName', 'IndicatorCode', 'Year', 'Value']

row_vals = ['Arab World', 'ARB',
                'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT',
                '1960', '133.56090740552298']

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)
print(zipped_lists)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)

# Print the dictionary
print(rs_dict)
