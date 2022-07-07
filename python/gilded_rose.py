from inventory_types.normal import NormalItem   # type: ignore
from inventory_types.brie import Brie   # type: ignore  
from inventory_types.sulfuras import Sulfuras   # type: ignore
from inventory_types.backstage import BackstagePass # type: ignore
from inventory_types.conjured import ConjuredItem   # type: ignore

class GildedRose(object):

    inventory_types = {
        "Aged Brie": Brie,
        "Sulfuras": Sulfuras,
        "Backstage": BackstagePass,
        "Conjured": ConjuredItem
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_type = GildedRose.get_item_type(item)
            item_type.update_quality(item)
            item_type.update_sell_in(item)

    @classmethod
    def get_item_type(cls, item):
        for inv in cls.inventory_types:
            if item.name.casefold().startswith(inv.casefold()):
                return cls.inventory_types[inv]
        return NormalItem


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
