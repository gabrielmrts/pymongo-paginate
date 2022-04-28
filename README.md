# Pymongo Paginate

> Paginate pymongo queries can be simple

![GitHub repo size](https://img.shields.io/github/repo-size/gabrielmrts/pymongo-paginate?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/gabrielmrts/pymongo-paginate?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/gabrielmrts/pymongo-paginate?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/gabrielmrts/pymongo-paginate?style=for-the-badge)

## Example

```

from pymongo_paginate import PyMongoPaginate

collection = db['your_pymongo_collection']
query = collection.find()

page = 1 ## Current page
pageSize = 10 ## Items per page

pagination = PyMongoPaginate(query, page, pageSize)
paginate = pagination.paginate()

---------------------------------------------------
Output -> dict {
            "page": 1,
            "page_count": 1,
            "item_count": 10,
            "items": []
        }
        

```

