# Git Sync Guide: Linking Local Project to Existing GitHub Repo

Follow these steps if you have a local directory with existing files and you want to link it to a new or existing GitHub repository that already contains files/history.

## 1. Initialize and Commit Local Files
Initialize Git in your local folder and commit all current files to ensure they are tracked:
```bash
# Initialize local repo
git init

# Stage and commit all local files
git add .
git commit -m "Initial commit of local files"
```

## 2. Link to Remote Repo
Rename your default branch to `main` and link the remote URL:
```bash
# Ensure branch is named 'main'
git branch -M main

# Add the remote link (replace with your repo URL)
git remote add origin https://github.com/USER/REPO-NAME.git
```

## 3. Sync and Merge Unrelated Histories
If the remote repository already contains files, pulling normally will fail or warn about unrelated histories. Run:
```bash
git pull origin main --allow-unrelated-histories --no-edit
```
*Note: This merges the remote history into your local repository, preserving both sets of files.*

## 4. Push Back to GitHub
Once merged, push your local commits up to GitHub and track the branch:
```bash
git push -u origin main
```
