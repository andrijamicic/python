#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests

wp_login = 'https://websiteurl/wp-login.php'
wp_admin = 'https://websiteurl/wp-admin/'
username = 'user'
password = 'pass'

with requests.Session() as s:
    headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
    datas={
        'log':username, 'pwd':password, 'wp-submit':'Log In',
        'redirect_to':wp_admin, 'testcookie':'1'
        }
    s.post(wp_login, headers=headers1, data=datas)
    resp = s.get(wp_admin)
    print(resp.text)
