class NormalItem:

    MAX_QUAL = 50

    @staticmethod
    def update_quality(item):
        if item.sell_in > 0:
            if item.quality >= 1:
                item.quality -= 1
        else:
            if item.quality >= 2: 
                item.quality -= 2

    @staticmethod
    def update_sell_in(item):
        item.sell_in -= 1