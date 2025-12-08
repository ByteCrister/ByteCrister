import feedparser

RSS_URL = "https://rsshub.app/linkedin/posts/1177422605"

feed = feedparser.parse(RSS_URL)

rows = []
for entry in feed.entries[:5]:  # latest 5 posts
    title = entry.title.replace("\n", " ").strip()
    link = entry.link
    rows.append(f"<tr><td>{title}</td><td><a href=\"{link}\" target=\"_blank\">View Post</a></td></tr>")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!-- LINKEDIN:START -->"
end = "<!-- LINKEDIN:END -->"

new_content = start + "\n" + "\n".join(rows) + "\n" + end

if start in readme and end in readme:
    updated = readme.split(start)[0] + new_content + readme.split(end)[1]
else:
    updated = readme + "\n" + new_content

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)