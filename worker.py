from re import match
from socket import *

from radon.complexity import SCORE
from radon.cli.harvest import CCHarvester
from radon.cli import Config
from time import gmtime, strftime
import requests
import os

import os.path
import sys
import shutil



class Worker():

    master_url = 'http://localhost:22222/'
    cc_total = 0

     cc_config = Config(
            exclude='',
            ignore='venv',
            order=SCORE,
            no_assert=True,
            show_closures=False,
            min='A',
            max='F',
    )

    def __init__(self):
        self.blob_url = requests.get(self.master_url).json()
        self.Done = False
        self.token = self.get_token


    def CC_Calc(self, url):
        blob_url = raw_url.split('|')[0]
        file_name = raw_url.split('|')[1]

        payload = {'access_token': self.token}
        header_s = {'Accept': 'application/vnd.github.v3.raw'}
        
        x = self.is_py(file_name)
        if x == True:

            resp = requests.get(blob_url, params = headers[0], headers=header_s)
            path = file_name

            with open(path, 'wb') as tf:
                tf.write(resp.text)
            tf.close()

            CC_file = open(path, 'r')
            results = CCHarvester(path, self.cc_config).gobble(CC_file_get)
            CC_file.close()
            os.remove(path)

            cc_file = 0

            for y in results:
                cc_file += int(y.complexity)

            return cc_file
            else:
                return 0

    def do_work(self):
        self.blob_url = requests.get(self.master_url).json()
        while self.blob_url != "done":
            file_cc = self.CC_calc(self.blob_url)
            self.total_cc += file_cc
            self.blob_url = requests.get(self.master_url).json
            #----------need to tidy this loop----#

        requests.put(self.manager_url, data={'cc': self.total_cc})

        
            

    def get_token(self):
        with open('git-token.txt', 'r') as tf:
            return token = tf.read()
        
    def is_py(self, file_name):
        return True if match('.*\.py', file_name) is not None else False
    
def main():
    work = Worker()
    work.do_work()



if __name__ == "__main__"
    main()

    

    
