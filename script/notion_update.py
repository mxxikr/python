from datetime import datetime
from notion.client import NotionClient
from notion.block import CollectionViewBlock
from notion.block import PageBlock, TextBlock, TodoBlock
from pendulum import date
import gitblog_crawler
from notion_database.database import Database
import os

# 크롤링할 페이지 주소
mxxikr_source = "https://mxxikr.github.io/"

# f12 -> 애플리케이션 -> token_v2
token = os.environ.get('NOTION_TOKEN')

# 노션 페이지 주소
url = "https://www.notion.so/mxxikr/MinJieun-Study-81066d9ba23d4631802283ae3668b408"

# 노션 데이터 베이스 주소
database_id = 'https://www.notion.so/mxxikr/fbc597fa579844bc85a3e7c7bce1a61e?v=48dfff5133eb4188b5fca09d372706c3'

collection_id = '7a9a17cd-3f9b-4cec-8f1e-bddac510a2a6'

client = NotionClient(token_v2=token)
page = client.get_block(url)

contents_collection = client.get_collection(collection_id)
properties = contents_collection.get_schema_properties()

for property in properties:
    print(property)

def get_schema_todo():
    # 테이블 스키마 생성
        return {
            # title 필수
            "title": {"name": "Git Blog Posting Check ✔️", "type": "title"},
            "url": {"name": "Posting URL", "type": "url"},
            "post": {"name": "Post", "type":"text"},
            "day": {"name": "Date", "type": "date"},
            "check": {"name": "Checking", "type": "select",
                "options": [
                    {
                        "color": "red",
                        "id": "502c7016-ac57-413a-90a6-64afadfb0c44",
                        "value": "포스팅 미완료",
                    },
                    {
                        "color": "blue",
                        "id": "57f431ab-aeb2-48c2-9e40-3a630fb86a5b",
                        "value": "포스팅 완료",
                    }
                ]
            }
        }

def new_page(page):
    # 새로운 페이지 생성
    new_page = page.children.add_new(PageBlock)
    today = datetime.now().strftime('%Y-%m-%d')
    new_page.title = '{}에 생성된 페이지'.format(today)

    print("페이지명:", page.title)

def new_text(page):
    # 텍스트 생성
    text = page.children.add_new(TextBlock)
    text.title = "text 생성"

def new_check(page):
    # 체크박스 생성
    todo1 = page.children.add_new(TodoBlock)
    todo1.title = "체크박스 생성"
    todo1.checked = True

def new_table(page):
    child = page.children.add_new(CollectionViewBlock)
    child.collection = client.get_collection(
        client.create_record(
            "collection", parent=child, schema=get_schema_todo())
        )
    child.title = 'GIT BLOG POSTING'
    child.views.add_new(view_type="table")

    row = child.collection.add_row()

    row.set_property('title', '@mxxikr')
    row.set_property('url', mxxikr_source)
    row.set_property('post', gitblog_crawler.diff_list(mxxikr_source))
    row.set_property('day', datetime.strptime("2022-10-21",'%Y-%m-%d'))
    row.set_property('check', '포스팅 완료')

#  row 업데이트 구현 필요
def new_row(page):
    return

def notion_check_mxxikr(mxxikr_source):    
    
    print("업로드 체크 완료")
