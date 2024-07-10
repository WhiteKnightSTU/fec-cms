import re

from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


bucket_url = 'https://cg-26646295-a781-431c-ab40-895616b7ea28.s3.amazonaws.com'


def new_press_link(link):
    if len(re.findall(r'\d+', link)) > 0:
        new_url = bucket_url + '/fecgov-assets/news_releases/{0}/'.format(re.findall(r'\d+', link)[0])
        return (new_url)
    else:
        return (link)


# using this one on staging for now
def make_absolute_links(orig_href, body):
    soup = bs(body, "html5lib")
    links = soup.find_all('a')
    for link in links:
        # looking for all realitive links
        if 'href' in link.attrs and str(link['href'])[:7] != 'http://':
            if str(link['href'])[:1] == '/':
                link['href'] = '/' + link['href']
            # re-save links as absolute links
            link['href'] = urljoin(orig_href, link['href'])
    return str(soup)


# this can be the function the remake all the links
def remake_links(body):
    # find relative links
    soup = bs(body, "html5lib")
    links = soup.find_all('a', href=True)
    for link in links:
        # we can add more links to check here
        path_replacements = [
            # Press path replacements
            ('http://fec.gov/press/press[0-9]+/news_releases/', new_press_link(link['href'])),
            ('http://fec.gov/press/press[0-9]+/', new_press_link(link['href'])),
            ('http://fec.gov/press/archive/[0-9]+/archive/[0-9]+/', new_press_link(link['href'])),
            ('http://fec.gov/press/archive/[0-9]+/', new_press_link(link['href'])),
            ('http://www.fec.gov/press/press[0-9]+/news_releases/', new_press_link(link['href'])),
            ('http://www.fec.gov/press/press[0-9]+/', new_press_link(link['href'])),
            ('http://www.fec.gov/press/archive/[0-9]+/archive/[0-9]+/', new_press_link(link['href'])),
            ('http://www.fec.gov/press/archive/[0-9]+/', new_press_link(link['href'])),
        ]

        for old, new in path_replacements:
            re_string = '^' + old + '*'
            if re.match(re_string, link['href']):
                link['href'] = re.sub(old, new, link['href'])

    return str(soup)


def fix_pdf_imports_old(body):
    # find relative links
    soup = bs(body, "html5lib")
    links = soup.find_all('a', href=True)
    for link in links:
        # we can add more links to check here
        path_replacements = [
            # Press path replacements
            'http://fec.gov/press/archive/[0-9]+/archive/[0-9]+/',
            'http://www.fec.gov/press/archive/[0-9]+/archive/[0-9]+/',
        ]

        for old in path_replacements:
            re_string = '^' + old + '*'
            if re.match(re_string, link['href']):
                link['href'] = re.sub(r'\/archive\/[0-9]+', '', link['href'], count=1)

    return str(soup)


# # using this to test
# test = """<html><head></head><body>
#     lsdkjfkj <a href="/test.com">x</a> sijdflkj
#     <a href="http://www.example/test.com">y</a> asd
#     <a href="http://fec.gov/press/archive/1975/archive/1975/archive.pdf">archive releases 1</a>
#     <a href="http://fec.gov/press/archive/1975/archive.pdf">archive releases 2</a>
#     <a href="http://fec.gov/press/press2016/news_releases/current.pdf">current releases</a>
#     <a href="http://fec.gov/press/press2010/2010_18M-Candidate_Files/1cansum201018.pdf">current releases type 2</a>'
#     <a href="http://www.fec.gov/press/archive/1977/archive/1977/19770210_MatchingFunds.pdf">test</a>
#     </body>
# """
# print(fix_pdf_imports_old(test))
