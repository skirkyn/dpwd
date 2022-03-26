import json
import os
import string
import sys
import threading

from flask import Flask, request

pass_length = 10

pass_found = False
lock = threading.Lock()
app = Flask(__name__)


def generate_passwords(num=1000) -> list:
    total_chars = num * pass_length
    # urandom produces hex every ~ 12th char approx, so we want to make sure
    all_the_chars = []
    while len(all_the_chars) < int(total_chars):
        all_the_chars = all_the_chars + [c for c in map(chr, os.urandom(total_chars * 12)) if c in string.hexdigits]

    all_the_chars = all_the_chars[:total_chars + 1]
    return [''.join(all_the_chars[i: i + pass_length]) for i in range(0, total_chars, pass_length)]


@app.route('/found', methods=['POST'])
def found_pass():
    global pass_found
    if pass_found:
        raise ValueError('pass already found')
    if not request.data:
        raise ValueError('data is required')
    lock.acquire()
    decoded = request.data.decode('utf-8')
    print('FOUND!!!!!!!!!! ' + decoded)
    with open('found.txt', 'w') as f:
        f.write(decoded)
        pass_found = True
    lock.release()
    return ''


@app.route('/passwords')
def get_passwords():
    global pass_found
    if pass_found:
        raise ValueError('pass already found')
    args = request.args
    return json.dumps(generate_passwords(int(args.get('num')) if 'num' in args else 16))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
