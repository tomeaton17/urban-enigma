'''

rh = request handler 
rh accepts two arguments : url, lookup_str = None
gets_requests(url) and asserts status_code
from response looksup lookup_str in json if it doesn't exist it returns the whole
json object (lookup_str will mostlikey default to 'data' key)

'''
import requests, os
from pprint import pprint as pp
def get_request(url, requests=requests):
    '''returns request.get object '''
    result = requests.get(url)
    ## insert an assert check on the status code before return
    return result

def look_up_key(dict_item, key_name):
    ''' if key exists return value otherwise return dict_item '''
    return dict_item.get(key_name, dict_item)


def request_handler(url, lookup_str=None):
    ''' returns returns a json, if lookup_str returns value '''
    request_result = get_request(url).json()
    return look_up_key(request_result, lookup_str)


if __name__ == '__main__':
    pp(get_request('https://api.instagram.com/v1/users/self/?access_token=' + os.environ['API_TOKEN'], requests))
    
