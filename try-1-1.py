import yaml
from datetime import datetime, date

def date_constructor(loader, node):
    value = loader.construct_scalar(node)
    
    # Adjust the format string based on your date format
    if isinstance(value, int):
        return date(value, 1, 1)
    elif '-' in value:
        if len(value) == 7:
            return datetime.strptime(value + '-01', '%Y-%m-%d').date()
        elif len(value) == 10:
            return datetime.strptime(value, '%Y-%m-%d').date()
    
    raise ValueError(f"Invalid date format: {value}")

yaml.add_constructor('tag:yaml.org,2002:date', date_constructor, yaml.SafeLoader)

# Example YAML content with various date formats
yaml_content = """
- title: Article 1
  issued: 2022
- title: Article 2
  issued: 2023-05
- title: Article 3
  issued: 2021-11-10
"""

# Load YAML with custom constructor
articles = yaml.load(yaml_content, Loader=yaml.SafeLoader)

# Replace 'issued' values with datetime.date objects
for article in articles:
    if isinstance(article['issued'], int):
        article['issued'] = date(article['issued'], 1, 1)
    if isinstance(article['issued'], str):
        if len(article['issued']) == 7:
            article['issued'] = datetime.strptime(article['issued'] + '-01', '%Y-%m-%d').date()
        elif len(article['issued']) == 10:
            article['issued'] = datetime.strptime(article['issued'], '%Y-%m-%d').date()

# Sorting the articles by date in reverse chronological order
sorted_articles = sorted(articles, key=lambda x: x['issued'], reverse=True)

# Print the sorted articles
for article in sorted_articles:
    print(article)
