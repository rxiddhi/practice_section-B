# Clone your fork
git clone https://github.com/your-username/repository-name.git
cd repository-name

# Add the original repository as a remote
git remote add upstream https://github.com/original-owner/repository-name.git

# Create a new branch
git checkout -b feature-branch-name

# Make changes, stage, and commit
git add .
git commit -m "Description of changes"

# Push to your fork
git push origin feature-branch-name

# (Later) Sync with the original repository
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
