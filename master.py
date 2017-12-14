from socket import *
import requests
from collections import deque
import shutil
from flask import Flask
from flask_restful import Resource, Api, request
import sys

blobs_list = deque()
new_cc = 0
cc_total = 0
blobs_length = 0
cc_count = 0
total_workers = sys.argv[1]

app = Flask(__name__)
api = Api(app)

class Master(Resource):

    def get(self):
        global blob_urls

        if blob_urls:
            return blob_urls.popleft()
        else:
            return "done"

    def put(self):

        global cc_total
        global cc_count

        new_cc = float(request.form['cc']
        cc_count += 1
        cc_total += new_cc
    
        if cc_count == int(total_workers):
                       cc_average = cc_total/blobs_length
                       shutdown_master()
        return '', 204

    def get_tree_urls(git_url):

                tree_urls = []

                with open('github-token.txt', 'r') as tf:
                       token = tf.read()

                payload = {'access_token': token}
                header_s ={'Accept': 'application/vnd.github.v3.raw'}

                resp = requests.get(blob, params = payload, headers = header_s)

                for item in resp.json():
                       tree_urls.append(item['commit']['tree']['url'])
                       

    def shutdown_master():
                func = request.environ.get('werkzeug.server.shutdown')
                if func is None:
                    raise RuntimeError('Not running with the Werkzeug Server')
                func()

    def get_blobs_list(git_url, tree_urls):
                 
                global blobs_list
                global blobs_length

                with open('github-token.txt', 'r') as tf:
                       token = tf.read()

                payload = {'access_token': token}
                header_s ={'Accept': 'application/vnd.github.v3.raw'}

                for blob in tree_urls:
                       resp = requests.get(blob, params = payload, headers = header_s)

                       trees = resp.json()['tree']
                       for item in tree:
                           f_url = item['url']
                           file_name = item['path']

                           url_file_name = f_url + '|' + file_name

                blobs_length = len(blobs_list)
                
                       
        
def main():
    
    git_url = 'https://api.github.com/repos/macgabht/Cyclomatic-Complexity/commits'
    tree_urls = get_tree_urls(github_url)      # get the list of tree URL's from the project's commits
    get_blob_url_list(git_url, tree_urls)    # get blob URLs of each tree's 
    app.run(host='localhost', port=5000, debug=False)


api.add_resource(Master, '/')


if __name__ == "__main__":
    main()
