import requests, json

def retrieve_Db(ID, headers):
    db_retrieveUrl = "https://api.notion.com/v1/databases/{}".format(ID)
    response= requests.request("GET", db_retrieveUrl, headers=headers)
    data = response.json()

    return

def query_Db(ID, headers):
    db_retrieveUrl = "https://api.notion.com/v1/databases/{}/query".format(ID)
    response = requests.request("POST", db_retrieveUrl, headers=headers)
    data = response.json()

    return data



def createPage(ID, headers, title_, url_, publish_, authors_, abstract_, tags_):
    page_createUrl = "https://api.notion.com/v1/pages"
    pageData = {
            "parent": {"database_id": ID},
            "properties": {
                "Title": {
                    "title": [
                        {
                        "text": {
                                "content": title_
                            }
                        }
                    ]
                },
                "URL":{
                    "url": url_
                },
                "PublishDate":{
                    "date":{
                        "start": publish_
                    }
                },
                "Authors": {
                    "rich_text": [
                        {
                            "text": {
                                "content": authors_
                            }
                        }
                    ]
                },
                "Abstract": {
                    "rich_text": [
                        {
                            "text": {
                                "content": abstract_
                            }
                        }
                    ]
                },
                "Tags": {
                    "multi_select": tags_
                
            }
        }
    }
    newPage = json.dumps(pageData)
    response = requests.request("POST", page_createUrl, headers=headers, data=newPage)
    
    return