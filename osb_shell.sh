#!/bin/sh
# ref: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
#
# Usage example: /bin/sh ./git_push.sh wing328 swagger-petstore-perl "minor update"

git_user_id=$1
git_repo_id=$2
release_note=$3

if [ "$git_user_id" = "" ]; then
    git_user_id="GIT_USER_ID"
    echo "[INFO] No command line input provided. Set \$git_user_id to $git_user_id"
fi

if [ "$git_repo_id" = "" ]; then
    git_repo_id="GIT_REPO_ID"
    echo "[INFO] No command line input provided. Set \$git_repo_id to $git_repo_id"
fi

if [ "$release_note" = "" ]; then
    release_note="Minor update"
    echo "[INFO] No command line input provided. Set \$release_note to $release_note"
fi
echo "started"
# Initialize the local directory as a Git repository
git init
echo "stae"
# Adds the files in the local repository and stages them for commit.
git add .
#git config --global user.email "sn.ankitha0003@gmail.com"
#git config --global user.name "ankithasn"
# Commits the tracked changes and prepares them to be pushed to a remote repository.
git commit -m "$release_note"
echo "ste"



GIT_TOKEN="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"
# Sets the new remote
git_remote=`git remote`
echo $git_remote
echo "strat"
echo "git remote add origin https://github.com/${git_user_id}/${git_repo_id}.git"
git remote add origin https://${git_user_id}:${GIT_TOKEN}@github.com/${git_user_id}/${git_repo_id}.git
#if [ "$git_remote" = "" ]; then # git remote not defined
#    echo $GIT_TOKEN . "git token"
#    if [ "$GIT_TOKEN" = "" ]; then
#        echo "[INFO] \$GIT_TOKEN (environment variable) is not set. Using the git crediential in your environment."
#        git remote add origin https://github.com/${git_user_id}/${git_repo_id}.git
#    else
#        echo "hew"
#        echo "git remote add origin https://${git_user_id}:${GIT_TOKEN}@github.com/${git_user_id}/${git_repo_id}.git"
#        git remote add origin https://${git_user_id}:${GIT_TOKEN}@github.com/${git_user_id}/${git_repo_id}.git
#    fi
#    #git branch -M master
#fi

git pull origin main

# Pushes (Forces) the changes in the local repository up to the remote repository
echo "Git pushing to https://github.com/${git_user_id}/${git_repo_id}.git"
git push origin main 2>&1 | grep -v 'To https'