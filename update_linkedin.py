import feedparser

RSS_URL = "https://rsshub.fans/linkedin/posts/1177422605"
feed = feedparser.parse(RSS_URL)

print("Number of posts:", len(feed.entries))
for entry in feed.entries:
    print(entry.title, entry.link)
