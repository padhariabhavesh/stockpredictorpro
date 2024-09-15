from googlesearch import search

def google_search(query, num_results=10):
    # Perform the search and get the URLs
    urls = search(query, num_results=num_results)
    
    # Print out the results
    for url in urls:
        print(url)

if __name__ == "__main__":
    query = input("Enter your search query: ")
    num_results = int(input("Enter the number of results to return: "))
    google_search(query, num_results)
