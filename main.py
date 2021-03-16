import re
import sys
import argparse
from requests import get
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Please enter the link")
parser.add_argument('link', metavar='L', type=str, nargs='+',
                    help='the link to crawl')
# parser.add_argument('--print', dest='print', action=print())

# args = parser.parse_args()
# print(args.)
def get_emails(link = 'https://generator.email/'):
    r = get(link).content

    soup = BeautifulSoup(r, 'html.parser')

    emails = re.findall(r'[\w\.-]+@[\w\.-]+', soup.text)

    # print (soup.text)

    return emails

    # for line in soup:
    #     print(line)
    # return soup


if __name__ == '__main__':

    emails = get_emails()
    print(*emails, sep='\n')
