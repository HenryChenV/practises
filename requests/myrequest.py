#!/usr/bin/env python
#-*-encoding=utf=8-*-


import requests
import json


def raw_requests():
    '''
    没有在各个请求间保持session，需要手动传sessionid
    '''

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'

    login_url = 'http://127.0.0.1:8000/login'
    password = raw_input('password: ')
    login_data = {"username": "henry", "password": password, "versions": "1.1.0"}

    get_task_list_url = 'http://127.0.0.1:8000/task_list'
    get_task_list_data = {"quick_time": "1", "optional_time": "3"}

    res = requests.post(login_url, data={'pop_data': json.dumps(login_data)}, headers=headers)
    print res.text, '\n\n'

    sessionid = res.cookies.get('sessionid')
    cookies={'sessionid': sessionid}
    res = requests.post(get_task_list_url, data={'pop_data': json.dumps(get_task_list_data)}, headers=headers, cookies=cookies)
    print res.text, '\n\n'


def requests_with_session():
    '''
    在各个请求间保持session，会更具sessionid自动设置cookies
    '''

    login_url = 'http://127.0.0.1:8000/login'
    password = raw_input('password')
    login_data = {"username": "henry", "password": password, "versions": "1.1.0"}

    get_task_list_url = 'http://127.0.0.1:8000/task_list'
    get_task_list_data = {"quick_time": "1", "optional_time": "3"}

    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'

    res = s.post(login_url, data={'pop_data': json.dumps(login_data)})
    print res.text, '\n\n'

    res = s.post(get_task_list_url, data={'pop_data': json.dumps(get_task_list_data)})
    print res.text, '\n\n'


def download():
    tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
    r = requests.get(tarball_url)
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    with open('xxx.tar.gz', 'wb') as fp:
        for chunk in r.iter_content(chunk_size=100):
            fp.write(chunk)


def requests_with_hooks():
    '''
    TypeError: "print_url() got an unexpected keyword argument 'verify'"
    '''
    def print_url(r):
        print r.url
    hooks = dict(response=print_url)
    import ipdb; ipdb.set_trace() ### XXX BREAKPOINT
    resp = requests.get('http://httpbin.org', hooks=hooks)
    print resp.text


def stream_requests():
    r = requests.get('http://httpbin.org/stream/20', stream=True)
    for line in r.iter_lines():
        if line:
            print (json.loads(line))

if __name__ == '__main__':
#    raw_requests()
#    requests_with_session()
#    download()
#    requests_with_hooks()
    stream_requests()
