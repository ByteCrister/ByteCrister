import feedparser

RSS_URL = "https://rsshub.app/linkedin/posts/1177422605"
feed = feedparser.parse(RSS_URL)

rows = []
for entry in feed.entries[:5]:  # latest 5 posts
    title = entry.title.replace("\n", " ").strip()
    link = entry.link
    rows.append(f"<tr><td>{title}</td><td><a href='{link}' target='_blank'>View Post</a></td></tr>")

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