# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("C:\\Users\\Matthew.Hiebing\\Documents\\0_BitbucketRepos\\data-gateway")
# Your mock repo
mock_repo = git.Repo("C:\\Users\\Matthew.Hiebing\\Documents\\1_GitHubRepos\\BitbucketCommits")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['Matthew.Hiebing@email.com', 'Matthew.Hiebing@schools.utah.gov'])
importer.import_repository()
