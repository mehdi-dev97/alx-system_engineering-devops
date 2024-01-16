import requests
def number_of_subscribers(subreddit):
    """  
    Get total number of subscribers on subreddit.
    Args:
        subreddit (str): subreddit name
    Returns:
        integer: Total of subscribers in subreddit
    """
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/med_)"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        data = req.json().get('data')
        return data.get('subscribers')
    else:
        return 0
