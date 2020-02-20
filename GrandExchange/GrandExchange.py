import requests
import json
from tabulate import tabulate

class Exchange(object):
    def __init__(self):
        self._exchange_data = json.loads(requests.get("https://rsbuddy.com/exchange/summary.json").content)

    def retrieve(self):
        return self._exchange_data

    def get_item(self, name):
        for x in self._exchange_data:
            if self._exchange_data[x]['name'] == name:
                return Item(self._exchange_data[x])
        raise Exception("No item matching that name was found.")

class Item(object):
    def __init__(self, item):
        self._raw_data = item
        self.id = item['id']
        self.name = item['name']
        self.members = item['members']
        self.sp = item['sp']
        self.buy_average = item['buy_average']
        self.buy_quantity = item['buy_quantity']
        self.sell_average = item['sell_average']
        self.sell_quantity = item['sell_quantity']
        self.overall_average = item['overall_average']
        self.overall_quantity = item['overall_quantity']

    def prettify(self):
        print(tabulate([[self.id, self.name, self.members, self.sp, self.buy_average, self.buy_quantity, self.sell_average, self.sell_quantity, self.overall_average, self.overall_quantity]], headers=["ID", "Name", "Members", "Store Price", "Buy Average", "Buy Quantity", "Sell Average", "Sell Quantity", "Overall Average", "Overall Quantity"], tablefmt="grid"))

    def item_data(self):
        return self._raw_data