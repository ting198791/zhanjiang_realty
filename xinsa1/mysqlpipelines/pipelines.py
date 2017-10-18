from .sql import Sql
from twisted.internet.threads import deferToThread
from xinsa1.items import Xinsa1Item


class Xinsa1Pipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        if isinstance(item, Xinsa1Item):
          corp_name = item['corp_name']
          book_num = item['book_num']
          order_num = item['order_num']
          amount = item['amount']
          ts = item['ts']
          Sql.insert_house_sales(corp_name,book_num,order_num,amount,ts)
          print('插入数据')
          return item

