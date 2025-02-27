# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
      for item in self.items:
        self.update_item(item)
    
    def update_item(self, item):
        is_special_item = item.name == "Aged Brie" and item.name == "Backstage passes to a TAFKAL80ETC concert"
        is_not_sulfura = item.name != "Sulfuras, Hand of Ragnaros"
        self.decrese_sell_in(item)
        if not is_special_item:
            if item.quality > 0 and is_not_sulfura:
                self.downgrade_item(item)
        else:
            if item.quality < 50:
                item.quality += 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11 and item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality += 1

        if item.sell_in < 0:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0 and is_not_sulfura:
                    item.quality -= 1
            else:
                item.quality = 0 if item.name == "Backstage passes to a TAFKAL80ETC concert" else min(50, item.quality + 1)

    def decrese_sell_in(self, item):
        item.sell_in -= 1

    def downgrade_item(self, item):
       item.quality -= 1

    


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
