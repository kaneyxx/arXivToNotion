import re
import feedparser
import time
from notion import query_Db, createPage
from arxiv import arxiv_query
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--num', type=int, default=100, help='how many papers you want to retrieve.')

# load token & database id
with open("./configuration.json", "r") as f:
    data = json.load(f)

# notion
notion_token= data["notion"]["token"]
notion_dbID= data["notion"]["databaseID"]
notion_headers = {
    "Authorization": "Bearer " + notion_token,
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json; charset=UTF-8"
    }

if __name__ == '__main__':
    args = parser.parse_args()

    response = arxiv_query(args.num) #default num of results = 100
    feed = feedparser.parse(response)

    # query current database and create a checklist
    db_check = query_Db(ID=notion_dbID, headers=notion_headers)

    for item in feed.entries:
        item = dict(item)
        title = item["title"].replace("\n", "").replace("  ", " ")
        link = item["link"]
        publish_date = item["published"].split("T")[0]
        summary = item["summary"].replace("\n", "").replace("  ", " ")
        authors = ", ".join(i.name for i in item["authors"])
        tags = [{"name":i.term.replace(",","")} for i in item["tags"]]

        check_link = re.findall(r"abs/(\d*\.\d*)", link)

        if check_link not in db_check:
            createPage(ID=notion_dbID, 
                headers=notion_headers, 
                title_=title, 
                url_=link,
                publish_=publish_date, 
                authors_=authors, 
                abstract_=summary,
                tags_=tags)
            time.sleep(1)
        else:
            pass

