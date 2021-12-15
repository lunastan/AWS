import json
import requests
from bs4 import BeautifulSoup as bs

def lambda_handler(event, context):
    # TODO implement
    res = requests.get('https://beomi.github.io')
    soup = bs(res.text, 'html.parser')
    blog_title = soup.select_one('h1').text
    return {
        'statusCode': 200,
        'body': json.dumps(blog_title)
    }
