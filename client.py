import time

import requests
import json

server_host = 'https://localhost:5000'
curr_pass = '6F6DA75EF3'

start = time.time()
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # 'Referer': 'https://localhost/blitz/console/',
    # 'Content-Type':
    #     'application/x-www-form-urlencoded',
    # 'Origin': 'localhost',
    # 'Cookie': 'cstate=ipLvGaWA7IdLdmw4s3QikaiGBrNZfq9qFJvYN0TpC6qtWPPM4HahuGJWYbMs06u4SZEwUkAvTPEagRu9jCV92AoBMuKFiRRLE8Tdj28lBIM|MTY0ODIyOTE3Mw|U0gxQVMxMjhDQkM|98uIGOiXA7fr5mC1bnyCzQ|0IpBYfiOl-DPwigoCEgqOH7MMLQ'
    'Cookie': 'cstate=8rODl0DeseE6b8r1aPdOA8uCu4dGtEtUdTTsxCwApl2dzOpiaDqRauvXJvCUSln3Yvo76fCyqfv_676ZJNOIwx1Ojfpmjr7OD6EHBGuvOjQ|MTY0ODIyODA4Mw|U0gxQVMxMjhDQkM|hIcqPPuN2pZlgp4liMsUdw|rOk-dTNi8BwSrFpkgD0HbxGzRjU'
    # 'Cookie': 'csession=GibkGKD9BDvVySajC5jD-ximO8sFDW3XiosUuxo7yKQgxQTM8SYeTP2BTHYTTwIKYyG94miy57nIdI19gmqlnDCJJbTy-C27ZfPlVg-pPqpoDS56wuNnc6IbByWNR7yvlQb8KQKvOxhms5d1yi2g73jpHC9E6LBMiAmC66OGg32KXJ8gaNZOHc5XpVsUD3blaN5T8VlYHZs2vAJl4z8pVOzc9tg9OQ5SS0QYJJX3Fh-6kOQqVbrbHqSvkK0h_W5C6CBJCX0KI83hyrgZNQuKZA==|MTY0ODIxMzE1Mw==|U0gxQVMxMjhDQkM|kn4KaXEHQvHGOy6k4yRqhQ|iSKBTdCoJnnsRs7VbFupYWOxeBQ='
}

# proxies = {
#               "socks"  : http_proxy,
#
#             }
resp = requests.post('https://localhost/blitz/console/login', data={'username': 'admin', 'password': 'curr_pass'},
                     headers=headers,
                     verify=False, allow_redirects=True)
print(resp.text)

resp = requests.post('https://localhost/blitz/console/login', data={'username': 'admin', 'password': 'blitz-demo'},
                     headers=headers,
                     verify=False, allow_redirects=True)
print(resp.text)
# print(time.time() - start)
# if u'Введен некорректный логин или пароль' in resp.text:
#     print('not found')
# elif not resp.ok:
#     print(resp.text)
# else:
#     print(curr_pass)

# curl -kvL 'https://localhost/blitz/console/login' -X POST -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: https://localhost' -H 'Connection: keep-alive' -H 'Referer: https://localhost/blitz/console/' -H 'Cookie: cstate=5QvwwnQDf-vJqjTNiC_HzE-vTqwcoU74aZHeNLwbB7rzg9VXrLjUqmO-N0tIsgxS7NFemJYMwrdoVyyR8j3u5ExQWQhSUdEs-HDpVXBgrHo|MTY0ODIyNzY2MA|U0gxQVMxMjhDQkM|f7Jbml_TmBvYfIe1l0iiyA|NXkTwlb8L-Zq3LC_yCHZ0uMnqZc; csession=U7GxSNezE6W7WFxkW-_jOVlFso86Wu98t46QzASmdwT2589J2o-S5beAPk1JejdN2-saiYTj969TEphrg-r_tS8fzdQqNliAz__x47q1TTwQbBy1mbisPegqt5Cx0TDIvbI-8oGUbz1Dny56_v4XoFnNCzY5ZbuzJ7z-DBsU86Y-NOezx4S7ppu6HewENh_WFEzPVyCQRn8ZII4zSmxCnF9EzBjn2lcxfzSylCWCbQpIOqkow0jo1mQQjfyV28-FoEU9x1VN9VS94JFxxcwt7g|MTY0ODE2NDIxOA|U0gxQVMxMjhDQkM|J4WCop489iZqwi4q3J4acQ|6ZPo06QObIq3_0xEctN0i-CGpzU' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' --data 'username=admin&password=dsdsc'
