import os
import subprocess

# --- Configuration ---
project_name = "my_project"
repo_path = os.path.join(os.getcwd(), project_name)
github_repo_url = "https://github.com/yourusername/your-repo-name.git"  # Optional

# --- Step 1: Create project folder ---
os.makedirs(repo_path, exist_ok=True)
print(f"Created project folder: {repo_path}")

# --- Step 2: Create a README file ---
readme_path = os.path.join(repo_path, "README.md")
with open(readme_path, "w") as f:
    f.write("# " + project_name)

# --- Step 3: Run Git commands ---
def run_git_command(command, cwd):
    result = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print("Error:", result.stderr.strip())

# Initialize git
run_git_command("git init", repo_path)

# Add files
run_git_command("git add .", repo_path)

# Commit
run_git_command('git commit -m "Initial commit"', repo_path)

# Optional: Connect to GitHub remote (uncomment if needed)
# run_git_command(f"git remote add origin {github_repo_url}", repo_path)
# run_git_command("git branch -M main", repo_path)
# run_git_command("git push -u origin main", repo_path)
