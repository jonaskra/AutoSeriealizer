import bs4 as bs
import urllib.request


def get_soup(pageUrl):
    sauce = urllib.request.urlopen(pageUrl).read()
    soup = bs.BeautifulSoup(sauce, features='html.parser')

    return [soup]


def get_elements(elements, html_element):
    output = []
    for element in elements:
        output.extend(element.find_all(html_element))

    return output


def get_elements_by_text(elements, string):
    output = []
    for element in elements:
        if string in element.text:
            output.append(element)

    return output


def get_pdf(dict):
    links = get_elements(get_soup(dict['url']), 'a')

    serie_links = get_elements_by_text(links, dict['link_text_pattern'])

    pdf_url = serie_links[-1]['href']

    url_with_slash = dict['url']

    if url_with_slash[-1] != '/':
        url_with_slash += '/'

    if 'ethz.ch' not in pdf_url:
        if pdf_url[0] == '.':
            pdf_url = pdf_url[1:]

        if pdf_url[0] == '/':
            pdf_url = pdf_url[1:]

        pdf_url = url_with_slash + pdf_url

    urllib.request.urlretrieve(pdf_url, dict['file_path'] + serie_links[-1].text + '.pdf')
