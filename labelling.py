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
    items = list(collection.where(u'result', u'==', u'NA').order_by(u'bloggername').get())

    items_count = len(items)
    print(f"Total : {items_count}")
    grouping = ""
    for idx, content in enumerate(items):

        item = content.to_dict()

        print(f"[{idx+1}/{items_count}] ", end='')

        if( grouping != "" ):
            if( item['bloggername'] == grouping ):
                item['result'] = False
                doc = item['link'].split("=")[-1]
                collection.document(doc).update({u'result': item['result']})
                print("pass")
                print("")
                continue
            else:
                grouping = ""


        print(f"bloggername: {item['bloggername']}")
        print(f"title: {item['title']}")
        print(f"postdate: {item['postdate']}")
        print(f"description: {item['description']}")
        print("")
        print("1.Private, 2.Commercial, 3.Commercial(bloggername)")

        label = input()

        if( label == "1" ):
            item['result'] = True

        elif( label == "2" ):
            item['result'] = False

        elif( label == "3" ):
            item['result'] = False
            grouping = item['bloggername']

        else:
            continue

        doc = item['link'].split("=")[-1]
        collection.document(doc).update({u'result': item['result']})

        print("")
        print("")

    exit()
