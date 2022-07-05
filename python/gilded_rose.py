from inventory_types.normal import NormalItem   # type: ignore

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item_type = NormalItem  # TODO make item type variable according to Item.name attribute
            item_type.update_quality(item)
            item_type.update_sell_in(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
