
from github import Github
import pygit2
import dotenv
import os

dotenv.load_dotenv()

# Setuping variables
TOKEN = input("Write token: ")
if TOKEN == "":
	TOKEN = os.getenv("GITHUB_TOKEN")
ORG = input("Write org: ")
PATH_TO_SAFE = input("Write path to save: ")

# Git connection
g = Github(TOKEN)
org = g.get_organization(ORG)
callbacks = pygit2.RemoteCallbacks(pygit2.UserPass(TOKEN, 'x-oauth-basic'))

# Clone repo
for repo in org.get_repos():
    pygit2.clone_repository(
        url=repo.clone_url,
        path=f'{PATH_TO_SAFE}/{repo.name}',
        callbacks=callbacks)
