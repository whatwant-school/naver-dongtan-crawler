#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os


class Naver:

    AUTH_CLIENTID = "AUTH_CLIENTID"
    AUTH_CLIENTSECRET = "AUTH_CLIENTSECRET"


    def __init__(self):
        try:
            self.clientId = self.getAuth(self.AUTH_CLIENTID)
            self.clientSecret = self.getAuth(self.AUTH_CLIENTSECRET)

            if( not self.clientId or not self.clientSecret ):
                raise Exception("There are not clientId/clientSecret")

            self.headers = {
                'X-Naver-Client-Id' : self.clientId,
                'X-Naver-Client-Secret' : self.clientSecret
            }

        except Exception as e:
            print("Authentication Error")
            raise


    def getAuth(self, kind):
        item = os.getenv(kind, "")

        if( item == "" ):
            filepath = f"{kind}.tmp"
            if( os.path.isfile(filepath) ):
                with open(filepath, 'r') as f:
                    item = f.read().strip()

        return item


    def searchBlog(self, keyword):
        url = f"https://openapi.naver.com/v1/search/blog?query={keyword}"

        contents = requests.get(url, headers=self.headers)

        return json.loads(contents.text)



if __name__ == '__main__':

    naver = Naver()

    contents = naver.searchBlog("동탄")
    print(json.dumps(contents, indent=2, ensure_ascii=False))
