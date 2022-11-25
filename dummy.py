import os
from git import Repo


git_user_id = "ankithasn"
git_repo_id = "test_push"
COMMIT_MESSAGE = "initial code"
Github_token = "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"

PATH_OF_GIT_REPO = os.getcwd()
# PATH_OF_GIT_REPO = r'/Users/ankitha/Documents/Baffle/repos/hackathon/javascript-client-generated/'


def gitPushToRepo(git_user_id, git_repo_id, COMMIT_MESSAGE, Github_token):
    # TODO encrypt github token

    try:
        repo = Repo.init(PATH_OF_GIT_REPO)
        # repo.git.checkout("main")
        repo.git.add(".")
        print("added files")
        # TODO undo git changes if error
        repo.index.commit(COMMIT_MESSAGE)
        print(git_user_id + ":" + Github_token + "@github.com/" + git_user_id + "/" + git_repo_id + ".git")
        if "origin" not in repo.remotes:
            # origin = repo.create_remote('origin', repo.remotes.origin.url)
            o = repo.create_remote(name='origin', url=git_user_id + ":" + Github_token + "@github.com/" + git_user_id + "/" + git_repo_id + ".git")
        else:
            o = repo.remotes.origin
        o.pull("main")
        o.push()
        # repo.git.push()
    except Exception as e:
        print('Some error occurred while pushing the code', e)


if __name__ == "__main__":
    # git_user_id = input("Enter user id: ")
    # git_repo_id = input("Enter repo name: ")
    # COMMIT_MESSAGE = input("Enter commit message: ")
    # Github_token = input("Enter github token: ")
    gitPushToRepo(git_user_id, git_repo_id, COMMIT_MESSAGE, Github_token)
