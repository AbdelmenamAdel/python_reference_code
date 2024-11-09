import requests
url="https://www.googleapis.com/books/v1/volumes?Filtering=free-ebooks&q=subject:Programming&Sorting=newest"
res=requests.get(url)
if res.status_code==200:
    data=res.json()
    books=data["items"]
    for book in books:
        title=book["volumeInfo"]["title"]
        authors=book["volumeInfo"]["authors"]
        print(f"Title: {title}")
        print(f"Authors: {', '.join(authors)}")
        print("--------------------")