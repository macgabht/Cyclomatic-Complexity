import socket
import os, sys
import requests
from radon.complexity import SCORE
from radon.cli.harvest import CCHarvester
from radon.cli import Config

RECV_BUFFER = 1024

    
cc_config = Config(
    exclude='',
    ignore='venv',
    order=SCORE,
    no_assert=True,
    how_closures=False,
    min='A',
    max='F',

                 )

    def work():

        ''''''''''''''''''''''''''
        'set up connection socket'

        host = 'localhost'
        port = 5000
        cc_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cc_s.bind((host, port))
        cc_s.listen(1)

        ''''''''''''''''''''''''''''''
        'receive url from the master'

        while 1:
            conn, addr = cc_s.accept()
            response = conn.recv(1024)
            url = response.decode()
            print ('URL:' + url)
            cc = cc_func(url, cc_config)
            cc = str(cc)

            conn.send(cc.encode())
        conn.close()
        
    def cc_func(url, cc_config):
        blob = url.split('|')[0]
        file_name = url.split('|')[1]
        toke = get_token()
        p_h = params(toke)

        py = if_python(file_name)
        if py == True:
            
            path = file_name

            response = requests.get(blob, params = p_h[0], headers = p_h[1])

            with open(path, 'w') as tf:
                tf.write(response.text)

            tf.close()

            file_grab = open(path, 'r')
            data = CCHarvester(path, cc_config).gobble(file_grab)
            file_grab.close()
            os.remove(path)
            file_complexity = 0

            for x in data:
                print (x.complexity)
                file_complexity += int(x.complexity)

            print ("Complexity found: " + str(file_complexity)

            return file_complexity
            
        

        
    def if_python(self, file_name):
         return True if match('.*\.py', filename) is not None else False


    def get_token():
        with open('github-token.txt', r) as fn:
            token = fn.read()
            return token

    def params(token):
        payl = {'access_token': token}
        headers = {'Accept': 'application/vnd.github.v3.raw'}

        return(payl, headers)
        
            

    def main():
        worker = Worker()
        print ('Worker ready to do work')
        worker.work()
        print('Worker finished')

if __name__ == "__main__":
    main()
