import requests
import xml.etree.ElementTree as ET

# URL of news RSS feed
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def loadRSS():
    '''
    Utility function to load RSS feed
    '''
    try:
        # Create HTTP request response object
        resp = requests.get(RSS_FEED_URL)
        resp.raise_for_status()  # Raise an error for bad HTTP status codes
        # Return response content
        return resp.content
    except requests.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return None

def parseXML(rss):
    '''
    Utility function to parse XML format RSS feed
    '''
    if rss is None:
        return []

    try:
        # Create element tree root object
        root = ET.fromstring(rss)

        # Create empty list for news items
        newsitems = []

        # Namespace dictionary
        namespaces = {'media': 'http://search.yahoo.com/mrss/'}

        # Iterate news items
        for item in root.findall('./channel/item'):
            news = {}

            # Iterate child elements of item
            for child in item:
                tag = child.tag.split('}')[-1]  # Remove namespace part if any

                # Special handling for media content
                if tag == 'content':
                    news['media'] = child.attrib.get('url', None)
                else:
                    news[tag] = child.text.strip() if child.text else None

            newsitems.append(news)

        # Return news items list
        return newsitems
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []

def topStories():
    '''
    Main function to generate and return news items
    '''
    # Load RSS feed
    rss = loadRSS()

    # Parse XML
    newsitems = parseXML(rss)
    return newsitems
