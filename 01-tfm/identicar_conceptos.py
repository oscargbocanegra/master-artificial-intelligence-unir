import xml.etree.ElementTree as ET
import pandas as pd

# Parse the uploaded XML file
file_path = 'D:/datasets/catalog-v001.xml'
tree = ET.parse(file_path)
root = tree.getroot()

# Define namespaces (if necessary)
namespaces = {'': 'http://www.w3.org/2001/XMLSchema'}  # Adjust according to the XML structure

# Extract data from the XML file
concepts = []
relationships = []
attributes = []

for element in root.iter():
    tag = element.tag.split('}')[-1]  # Remove namespace if present
    if tag == 'Concept':
        concepts.append(element.attrib)
    elif tag == 'Relationship':
        relationships.append(element.attrib)
    elif tag == 'Attribute':
        attributes.append(element.attrib)

# Convert to DataFrames for easier visualization
concepts_df = pd.DataFrame(concepts)
relationships_df = pd.DataFrame(relationships)
attributes_df = pd.DataFrame(attributes)

import pandas as pd

# Display DataFrames using pandas built-in functionality
print("Concepts from XML")
print(concepts_df)
print("\nRelationships from XML")
print(relationships_df)
print("\nAttributes from XML")
print(attributes_df)


# Extract <uri> elements from the XML file
uri_elements = []

for element in root.iter():
    tag = element.tag.split('}')[-1]  # Remove namespace if present
    if tag == 'uri':
        uri_elements.append(element.attrib)

# Convert to a DataFrame for analysis
uri_df = pd.DataFrame(uri_elements)

print("URI Elements in XML")
print(uri_df)


# Define classification logic for concepts, relationships, and attributes based on patterns or keywords in the data
def classify_element(row):
    if 'Corporate' in row['name'] or 'CorporateEvents' in row['uri']:
        return 'Concept'
    elif 'Relations' in row['name'] or 'Relations' in row['uri']:
        return 'Relationship'
    elif 'Metadata' in row['name'] or 'Metadata' in row['uri']:
        return 'Attribute'
    else:
        return 'Unclassified'

# Apply classification logic to the DataFrame
uri_df['Category'] = uri_df.apply(classify_element, axis=1)

# Split the data based on classifications
concepts_classified = uri_df[uri_df['Category'] == 'Concept']
relationships_classified = uri_df[uri_df['Category'] == 'Relationship']
attributes_classified = uri_df[uri_df['Category'] == 'Attribute']

# Display the results for each category
print("Classified Concepts")
print(concepts_classified)
print("\nClassified Relationships")
print(relationships_classified)
print("\nClassified Attributes")
print(attributes_classified)



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
print("Cleaned and Transformed Data for NLP")
print(combined_cleaned)

