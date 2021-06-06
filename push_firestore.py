#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json

if __name__ == '__main__':

    with open("output.tmp") as f:
        items = json.load(f)


    cred = credentials.Certificate('AUTH_FIRESTORE.tmp')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    collection = db.collection(u'dongtan_raw')


    insert_count = 0
    items_count = len(items)
    for idx, item in enumerate(items):

        doc = item['link'].split("=")[-1]

        check = collection.where(u'link', u'==', item['link']).get()
        if( len(check) > 0 and check[0].id == doc ):
            print(f"{idx+1}/{items_count} pass")
            continue

        item['result'] = "NA"

        collection.document(doc).set(item)
        print(f"{idx+1}/{items_count} insert")
        insert_count += 1


    print(f"New insert items : {insert_count}")
    exit()
