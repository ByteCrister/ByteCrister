import feedparser

RSS_URL = "https://rsshub.app/linkedin/posts/1177422605"

feed = feedparser.parse(RSS_URL)

posts = []
for entry in feed.entries[:5]:  # Get latest 5 posts
    title = entry.title.replace("\n", " ").strip()
    posts.append(f"- [{title}]({entry.link})")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!-- LINKEDIN:START -->"
end = "<!-- LINKEDIN:END -->"

new_content = start + "\n" + "\n".join(posts) + "\n" + end

if start in readme and end in readme:
    updated = readme.split(start)[0] + new_content + readme.split(end)[1]
else:
    updated = readme + "\n## 🔗 Latest LinkedIn Posts\n" + new_content

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated)
