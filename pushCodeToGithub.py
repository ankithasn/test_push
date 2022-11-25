import os
from git import Repo

git_user_id = "OSB-code-push"
git_repo_id = "OSB-git"
COMMIT_MESSAGE = "initial code"
Github_token = "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"

# PATH_OF_GIT_REPO = os.getcwd()
PATH_OF_GIT_REPO = r'/Users/ankitha/Documents/Baffle/repos/hackathon/javascript-client-generated/'


def git_push_repo():
    # TODO encrypt github token

    try:
        repo = Repo.init(PATH_OF_GIT_REPO)
        repo.git.add(".")
        # TODO undo git changes if error
        repo.index.commit(COMMIT_MESSAGE)
        if "origin" not in repo.remotes:
            # origin = repo.create_remote('origin', repo.remotes.origin.url)
            o = repo.create_remote(name='origin', url=git_user_id + ":" + Github_token + "@github.com/" + git_user_id + "/" + git_repo_id + ".git")
        else:
            o = repo.remotes.origin
        o.pull()
        o.push()
        # repo.git.push()
    except Exception as e:
        print('Some error occured while pushing the code', e)


git_push_repo()
