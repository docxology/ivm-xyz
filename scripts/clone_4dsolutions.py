# Clones all repositories from a specified GitHub user for further analysis.

import os
from github import Github

# Replace with your GitHub access token
ACCESS_TOKEN = "REPLACE_WITH_ACCESS_TOKEN"

# Specify the GitHub username to clone repositories from
USERNAME = "4dsolutions"

# Authenticate with GitHub using the access token
g = Github(ACCESS_TOKEN)

# Retrieve the user object
user = g.get_user(USERNAME)

# Get all repositories of the user
repos = user.get_repos()

# Create a directory to store the cloned repositories
os.makedirs(USERNAME, exist_ok=True)

# Clone each repository
for repo in repos:
    print(f"Cloning {repo.name}...")
    
    # Clone the repository into a subdirectory with the repository name
    os.system(f"git clone {repo.clone_url} {USERNAME}/{repo.name}")

print("Finished cloning all repositories!")