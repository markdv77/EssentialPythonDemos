import requests
from xml.etree import ElementTree


def main():
    #url = 'https://nicolaiarocci.com/index.xml'
    url = 'http://rss.cnn.com/rss/cnn_topstories.rss'
    r = requests.get(url)
    xml_text = r.text

    #print(xml_text[:500])
    dom = ElementTree.fromstring(xml_text)
    items = dom.findall('channel/item')
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        print('{0} at {1}'.format(title, link))


if __name__ == '__main__':
    main()
