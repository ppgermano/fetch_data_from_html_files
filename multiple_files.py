import json
import codecs
from lxml import etree
import os
import time

import pandas as pd

class Data(object):
    def __init__(self, dictionary, page=1):
        for key, value in dictionary.items():
            try:
                setattr(self, key, value[0])
            except:
                setattr(self, key, '')
        if page:
            self.page = page

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

def export_excel(data, file_path):

    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, dict):
        df = pd.DataFrame.from_dict(data)
    elif isinstance(data, pd.DataFrame):
        df = data

    try:
        df.to_excel(file_path)
    except Exception as e:
        print(e)
        return False
    return True

def xpath_reference():
    return {
        'test': '//div[@class="example"]/text()',
        'endpoints': {
            'parent': '',
            'child': {
                'title': '',
                'tables': ''
            }
        }
    }

def _extract_info_search_page_from_html_file(source_code):
    dom = etree.HTML(source_code)
    return [{"information": dom.xpath(xpath_reference()['test'])[0]}]

directory = './html_data'

'''
Usar encoding="Latin-1"
https://qastack.com.br/programming/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character

'''
all_data = []
for filename in os.listdir(directory):
    with codecs.open(os.path.join(directory, filename), 'r', encoding="Latin-1") as file:
        source_code = file.read()
    data = _extract_info_search_page_from_html_file(source_code)
    print(filename)
    all_data.extend(data)

export_excel(all_data, f'./out_data/{time.strftime("%Y%m%d%H%M%S")}.xlsx')
