import math

class PyMongoPaginate():
    
    def __init__(self, query, page, page_size) -> None:
        self.query = query
        self.page = page
        self.page_size = page_size

    def paginate(self) -> dict:
        skips = (self.page_size * (self.page - 1))
        query = self.query.skip(skips).limit(self.page_size)

        countItems = len([x for x in query])
        countDocuments = self.query.collection.count_documents({})
        pageCount = 0
        
        if countItems > 0:
            pageCount = (countDocuments / countItems)
        else:
            pageCount = (countDocuments / self.page_size)

        return {
            "page": self.page,
            "page_count": math.ceil(pageCount),
            "item_count": countItems,
            "items": query
        }