from urllib.request import urlopen


def arxiv_query(max_results=100):
    # arxiv api url
    base_url = "http://export.arxiv.org/api/query?"

    # search parametesrs
    search_query = ["cs.AI", "cs.CV", "cs.LG", "cs.CL", "cs.NE", "stat.ML"]
    start_index = 0
    max_results = max_results
    sortBy = "submittedDate"
    sortOrder = "descending"
    # verbose=False

    query = 'search_query=%s&start=%i&max_results=%i&sortBy=%s&sortOrder=%s' % ('+OR+'.join(['cat:%s' % c for c in search_query]), 
                                                                                start_index, 
                                                                                max_results, 
                                                                                sortBy, 
                                                                                sortOrder)

    response = urlopen(base_url+query).read()
    return response