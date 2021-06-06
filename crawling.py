#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import os


class Naver:

    AUTH_CLIENTID = "AUTH_CLIENTID"
    AUTH_CLIENTSECRET = "AUTH_CLIENTSECRET"
    display = 100
    sort = "date"

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


    def searchBlog(self, keyword, MaxPage):

        page = 0
        results = []
        while True:
            if( page >= MaxPage ):
                break

            start = 1 + (self.display * page)
            url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&display={self.display}&start={start}&sort={self.sort}"
            #print(f"{url}")

            contents = requests.get(url, headers=self.headers)

            contents = json.loads(contents.text)

            contents_count = len(contents['items'])
            if( contents_count > 0 ):
                results.extend(contents['items'])

            if( contents_count < self.display ):
                break

            page += 1

        return results



if __name__ == '__main__':

    naver = Naver()

    contents = naver.searchBlog("동탄", 2)
    print(json.dumps(contents, indent=2, ensure_ascii=False))
