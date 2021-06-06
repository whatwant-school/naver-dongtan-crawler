#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


if __name__ == '__main__':

    cred = credentials.Certificate('AUTH_FIRESTORE.tmp')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    collection = db.collection(u'dongtan_raw')
    items = collection.where(u'result', u'==', u'NA').stream()


    for idx, content in enumerate(items):

        item = content.to_dict()

        print(f"bloggername: {item['bloggername']}")
        print(f"title: {item['title']}")
        print(f"postdate: {item['postdate']}")
        print(f"description: {item['description']}")
        print("")
        print("1.Private, 2.Commercial")

        label = input()

        if( label == "1" ):
            item['result'] = True

        elif( label == "2" ):
            item['result'] = False

        else:
            continue

        doc = item['link'].split("=")[-1]
        collection.document(doc).update({u'result': item['result']})

        print("")
        print("")

    exit()
