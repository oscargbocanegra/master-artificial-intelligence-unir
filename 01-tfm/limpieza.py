# Clean and transform the data from the classified elements to ensure compatibility with NLP models

# Function to clean and transform URI data
def clean_transform_uri(uri_df):
    uri_df_cleaned = uri_df.copy()
    # Normalize URI strings
    uri_df_cleaned['uri'] = uri_df_cleaned['uri'].str.strip().str.lower()
    # Normalize name strings
    uri_df_cleaned['name'] = uri_df_cleaned['name'].str.strip().str.lower()
    # Extract useful keywords from URIs or names for NLP (e.g., split paths, isolate last part)
    uri_df_cleaned['extracted_keywords'] = uri_df_cleaned['uri'].apply(lambda x: x.split('/')[-1].replace('.rdf', ''))
    return uri_df_cleaned

# Apply cleaning and transformation to the identified URI data
concepts_cleaned = clean_transform_uri(concepts_classified)
relationships_cleaned = clean_transform_uri(relationships_classified)
attributes_cleaned = clean_transform_uri(attributes_classified)

# Combine all cleaned and transformed data for further analysis or model preparation
combined_cleaned = pd.concat([concepts_cleaned, relationships_cleaned, attributes_cleaned], keys=['Concepts', 'Relationships', 'Attributes'])

# Display the cleaned and transformed dataset
tools.display_dataframe_to_user(name="Cleaned and Transformed Data for NLP", dataframe=combined_cleaned)
