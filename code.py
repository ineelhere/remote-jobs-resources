import csv

# Define the header and footer text
header = '''# 🗺️ Remote Jobs Resources 👍

🌐 This GitHub repository contains a list of companies and their career sites that offer remote job opportunities. Contributions and validations are welcome from anyone interested in remote work, including additional companies that offer remote jobs and information about their hiring process.

🚀 The goal is to create a valuable resource for job seekers in the current world, where they can find a remote job opportunity that matches their skills and interests 💼. Let's work together to build the ultimate remote jobs list! 🙌

## List of Remote Companies

| # | Company | Career Site |
| - | ------- | ----------- |
'''

footer = '''---

👋 Want to contribute to this list? Please fork this repository and submit a pull request with any additional companies that offer remote jobs or information about their hiring process. Together, we can help more people find their dream remote job! 🙌
'''

# Open the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Convert the CSV data to markdown
markdown = ''
for i, row in enumerate(data):
    if i == 0:
        continue
    markdown += f'| {i} | ' + ' | '.join(row) + ' |\n'

# Write the markdown to a file
with open('README.md', 'w') as file:
    file.write(header + markdown + footer)
