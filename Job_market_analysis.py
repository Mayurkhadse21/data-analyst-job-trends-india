# Step 1: Load the dataset

import pandas as pd

df = pd.read_csv("job_postings_india_50.csv")
df.head()

# Step 2: Clean the data
# Drop duplicates if any
df.drop_duplicates(inplace=True)

# Standardize capitalization
df["Job Title"] = df["Job Title"].str.title()
df["Company"] = df["Company"].str.title()
df["Location"] = df["Location"].str.title()

# Step 3: Analyse top job titles
top_roles = df["Job Title"].value_counts().head(10)
print("Top 10 Job Titles:\n", top_roles)

# Step 4: Analyse top hiring cities
top_cities = df["Location"].value_counts().head(10)
print("Top 10 Cities Hiring:\n", top_cities)

# Step 5: Skill frequency in summaries
skills = ["excel", "sql", "python", "power bi", "tableau", "communication", "statistics"]
text = " ".join(df["Summary"].dropna()).lower()
skill_counts = {skill: text.count(skill) for skill in skills}
skill_df = pd.DataFrame(skill_counts.items(), columns=["Skill", "Frequency"])
print(skill_df)

skill_df.to_csv("skills_summary.csv", index=False)













