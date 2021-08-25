#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


groups = [
    "병원",
    "입시",
    "학원",
    "분양",
    "에이스뮤직",
    "더바른 건강정보",
    "공인중개사",
    "인천공항",
    "집수리",
    "하수구",
    "변기",
    "줄눈",
    "설비",
    "싱크대",
    "부동산",
    "별상신당",
    "수원점",
    "영통점",
    "동탄점",
    "하자보수",
    "현수막",
    "곰팡이",
    "컨설팅",
    "피부과",
    "한의원",
    "마사지",
    "정신건강의학과",
    "에어컨",
    "보일러",
    "방충망",
    "외형복원",
    "인테리어",
    "물류창고",
    "치과",
    "한우리",
    "필라테스",
    "연구소",
    "전자담배",
    "출장",
    "법원",
    "여성전용",
    "카톡",
    "(주)",
    "난방시스템",
    "블랙박스",
    "타일시공",
]


if __name__ == '__main__':

    cred = credentials.Certificate('AUTH_FIRESTORE.tmp')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    collection = db.collection(u'dongtan_raw')
    items = collection.order_by(u'bloggername').stream()

    category = {}
    for idx, content in enumerate(items):

        item = content.to_dict()

        print(f"[{idx+1:4d}] ", end='')

        for group in groups:
            if( group in item['bloggername']):
                item['bloggername'] = group
                break


        if( item['bloggername'] in category.keys() ):
            category[ item['bloggername'] ] += 1
        else:
            category[ item['bloggername'] ] = 1

        print(f"[{idx+1:4d}] {item['bloggername']:20s} = {category[ item['bloggername'] ]:4d}")

    category = sorted(category.items(), key=(lambda x:x[1]), reverse=True)
    for idx, (bloggername, count) in enumerate(category):
        print(f"[{idx+1:4d}] {bloggername:40s} = {count:4d}")


    exit()
