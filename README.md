# Arxiv to Notion

Prepare your configuration.json file as below:
```json
{
    "notion": {
        "token": "",
        "databaseID": ""
    }
}
```
**You can also store the keys into repo secrets to apply it to GitHub actions.** 

- arXiv
> 1. There are some variables you can modify in arxiv part. For example, the search strategy default is ["cs.AI", "cs.CV", "cs.LG", "cs.CL", "cs.NE", "stat.ML"], sorted by submitted date and so on.  
> 2. Visit arXiv API webpage for details: https://arxiv.org/help/api/user-manual

- Notion
> 1. Go to https://www.notion.so/my-integrations and get your Internal Integration Token
> 2. Click the share button on database, then invite the integration you just created
> 3. Copy Notion database link to browser and get the ID, e.g. https://www.notion.so/workspace/[DATABASEID]?v=12345678 , the database ID is 32 characters (With team plan, there would be no workspace section)

* Notion table columns (notion data type):  
  "Title" (title)  
  "URL" (url)  
  "PublishDate" (ISO8601 time format)  
  "Authors" (rich_text)  
  "Abstract" (rich_text)  
  "Tags" (multi-select)
**Feel free to modify as your table design :)**

Command:
```python
python main.py [--num 100]
```
Change the integer to decide how many papers you want to retrieve.