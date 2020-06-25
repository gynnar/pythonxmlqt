import xml.etree.ElementTree as ET
import requests


class radioChannel():
    def __init__(self):
        self.name = None
        self.image_url = None
        self.live_url = None
        self.channel_type = None


class channelList():
    def __init__(self):
        self.ch_list = []
        self.ch_data_url = "http://api.sr.se/api/v2/channels/"

    def getChInfoFromXml(self, et):
        for elem in et.iter('channel'):
            rc = radioChannel()
            try:
                rc.name = elem.attrib['name']
                rc.channel_type = elem.find('channeltype').text
                rc.image_url = elem.find('image').text
                rc.live_url = elem.find('liveaudio/url').text

                self.ch_list.append(rc)
            except:
                print("Hoppsan... :P")

    def fetchXmlData(self):
        response = requests.get(self.ch_data_url)
        root = ET.fromstring(response.text)
        print("Number of pages: ", root.find('pagination/totalpages').text)
        no_pages = int(root.find('pagination/totalpages').text)
        print(no_pages)
        for i in range(1, no_pages):
            url = self.ch_data_url + "?page=" + str(i)
            print(url)
            response = requests.get(url)
            root = ET.fromstring(response.text)
            self.getChInfoFromXml(root)


if __name__ == '__main__':

    cl = channelList()

    cl.fetchXmlData()

    for ch in cl.ch_list:
        print(ch.name)
