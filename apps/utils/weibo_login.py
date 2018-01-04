# _*_ coding: utf-8 _*_
"""
__author__ = 'lawtech'
__date__ = '2018/1/3 下午3:02'
"""
import requests


def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_uri = "http://47.100.40.228:8000/complete/weibo/"
    auth_url = weibo_auth_url + "?client_id={client_id}&redirect_uri={re_url}".format(client_id=1709286761,
                                                                                      re_url=redirect_uri)

    print(auth_url)


def get_access_token(code="92702b66bb786267d6525307eeb95553"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    re_dict = requests.post(access_token_url, data={
        "client_id": 1709286761,
        "client_secret": "08ea25734324070b42ebc01c25c42ea7",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://47.100.40.228:8000/complete/weibo/"
    })
    pass


# '{"access_token":"2.001MzLID_ZzfrBc3f232edf7XZiSBD","remind_in":"157679998","expires_in":157679998,"uid":"2869466040","isRealName":"true"}'


def get_user_info(access_token="2.001MzLID_ZzfrBc3f232edf7XZiSBD", uid=2869466040):
    user_show_url = "https://api.weibo.com/2/users/show.json?access_token={access_token}&uid={uid}".format(
        access_token=access_token, uid=uid)
    print(user_show_url)


if __name__ == '__main__':
    # get_auth_url()
    # get_access_token(code="92702b66bb786267d6525307eeb95553")
    get_user_info(access_token="2.001MzLID_ZzfrBc3f232edf7XZiSBD")
