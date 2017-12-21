from socket import *
import requests
from collections import deque
import shutil
from flask import Flask
from flask_restful import Resource, Api, request
import sys

cc_total = 0
blobs_list = deque()
new_cc = 0
total_workers = 8
blobs_length = 0
cc_count = 0


app = Flask(__name__)
api = Api(app)

class Master(Resource):

    def get(self):
        global time0
        global blob_urls
        
        if blob_urls:
            if blobs_length-1 == len(blobs_list):
                time0 = time.clock()
            return blob_urls.popleft()
        else:
            return "done"

    def put(self):
        global time0
        global time1
        global CC_average
        global cc_total
        global cc_count

        new_cc = float(request.form['cc']
        cc_count += 1
        cc_total += new_cc
    
        if cc_count == int(total_workers):
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

    def get_blobs_list(tree_urls):
                 
                global blobs_list
                global blobs_length

                with open('github-token.txt', 'r') as tf:
                       token = tf.read()

                payload = {'access_token': token}
                header_s ={'Accept': 'application/vnd.github.v3.raw'}

                for blob in tree_urls:
                       resp = requests.get(blob, params = payload, headers = header_s)

                       tree = resp.json()['tree']
                       for item in tree:
                           f_url = item['url']
                           file_name = item['path']

                           url_file_name = f_url + '|' + file_name
                           blobs_list.append(url_file_name) 
                blobs_length = len(blobs_list)
                
                       
        
def main():
    
    git_url = 'https://api.github.com/repos/macgabht/Distributed-File-System/commits'
    tree_urls = get_tree_urls(github_url)      # tree URL's from the project's commits
    get_blob_list(git_url, tree_urls)    # get blob URLs of each trees
    
    app.run(host='localhost', port=22222, debug=False)
    time1 = time.clock()
    CC_average = cc_total/blobs_length
    alpha = time1 - time0
    print('Time taken: {0:0.2f}s'.format(alpha))
    time_data = ("Total_workers=" + str(total_workers) + ", time =" + str(delta) + 'secs\n')
    with open ("WorkerData.txt", 'a+') as f:
                f.write(time_data)
                    
api.add_resource(Master, '/')


if __name__ == "__main__":
    main()
