try:
    from googlesearch import search as google_search
except ImportError:
    import os
    os.system('pip install googlesearch-python')

def perform_google_search():
    print('Enter what you want to search')
    query = input('=> ')
    result = int(input('How many results you want?: '))

    # Perform the Google search
    search_results = google_search(query, num_results=result)

    # Print the search results
    for i, result in enumerate(search_results, start=1):
        print(f"{i}. {result}")

perform_google_search()



'''
┌─[cyber-programer@programer]─[~]
└──╼ $python3 google_search.py

Enter what you want to search
=> php?id=5
How many results you want?: 5
1. http://www.juc.edu.bd/page.php?id=5
2. http://esjindex.org/search.php?id=5
3. http://www.bdfoods.com.bd/awards.php?id=5
4. https://www.bjp-bg.com/paper.php?id=5
5. http://millenniumstudio.net/index.php-id=5
6. https://e-sga.org/index.php?id=5

'''

