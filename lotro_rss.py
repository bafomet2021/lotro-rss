import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
from datetime import datetime

URL = "https://forums.lotro.com/index.php?forums/service-news.27/"

r = requests.get(URL)

soup = BeautifulSoup(r.text, "html.parser")

fg = FeedGenerator()

fg.title("LOTRO Maintenance & News")
fg.link(
    href="https://forums.lotro.com/",
    rel="alternate"
)

fg.description(
    "Actualités serveurs LOTRO - Maintenance - Patch"
)

for post in soup.select(".structItem-title a")[:10]:

    title = post.text.strip()

    if any(word in title.lower() for word in [
        "maintenance",
        "offline",
        "online",
        "update",
        "hotfix",
        "patch"
    ]):

        fe = fg.add_entry()

        fe.title(title)

        fe.link(
            href="https://forums.lotro.com/" + post.get("href")
        )

        fe.description(
            "Annonce officielle LOTRO"
        )

        fe.pubDate(datetime.now())


fg.rss_file("feed.xml")
