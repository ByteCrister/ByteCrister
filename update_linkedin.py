# update_linkedin.py
from linkedin_api import Linkedin
import os

# Environment secrets for GitHub Actions
LINKEDIN_EMAIL = os.environ.get("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

if not LINKEDIN_EMAIL or not LINKEDIN_PASSWORD:
    raise ValueError("LinkedIn credentials not set in environment variables")

# Login to LinkedIn
api = Linkedin(LINKEDIN_EMAIL, LINKEDIN_PASSWORD)

# Fetch latest 5 posts from the user
username = "sadiqul-islam-shakib"
posts = api.get_user_posts(username)
latest_posts = posts[:5]  # take 5 latest

# Prepare table rows
rows = []
for post in latest_posts:
    text = post.get("text", "").replace("\n", " ").strip()
    post_url = f"https://www.linkedin.com/feed/update/{post.get('id')}"
    rows.append(f"<tr><td>{text}</td><td><a href=\"{post_url}\" target=\"_blank\">View Post</a></td></tr>")

# Read existing README
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start_marker = "<!-- LINKEDIN:START -->"
end_marker = "<!-- LINKEDIN:END -->"
new_content = start_marker + "\n" + "\n".join(rows) + "\n" + end_marker

# Replace old content
if start_marker in readme and end_marker in readme:
    updated = readme.split(start_marker)[0] + new_content + readme.split(end_marker)[1]
else:
    updated = readme + "\n" + new_content

# Write updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)