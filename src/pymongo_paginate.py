import math

class PyMongoPaginate():
    
    def __init__(self, query, page, page_size) -> None:
        self.query = query
        self.page = page
        self.page_size = page_size

    def paginate(self) -> dict:
        skips = (self.page_size * (self.page - 1))
        query = self.query.skip(skips).limit(self.page_size)

        if self.page == 0:
            self.page = 1 

        clonedCursor = self.query.clone()
        countItems = len([x for x in clonedCursor])
        countDocuments = clonedCursor.collection.count_documents({})
        pageCount = 0
        
        if self.page_size > 0:
            if countItems == 0:
                pageCount = 0
            else:
                pageCount = (countDocuments / countItems)
        else:
            pageCount = (countDocuments / self.page_size)

        return {
            "page": self.page,
            "page_count": math.ceil(pageCount),
            "item_count": countItems,
            "items": [element for element in query]
        }