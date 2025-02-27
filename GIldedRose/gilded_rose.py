# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
      for item in self.items:
        self.update_item(item)
    
    def update_item(self, item):
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                item.downgrade_item()
        else:
            if item.quality < 50:
                item.quality += 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11 and item.quality < 50:
                        item.quality += 1
                    if item.sell_in < 6 and item.quality < 50:
                        item.quality += 1

        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

        if item.sell_in < 0:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0 and item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality -= 1
            else:
                item.quality = 0 if item.name == "Backstage passes to a TAFKAL80ETC concert" else min(50, item.quality + 1)

    def downgrade_item(self, item):
       item.quality -= 1

    


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
