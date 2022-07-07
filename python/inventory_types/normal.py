class NormalItem:

    MAX_QUAL = 50

    @staticmethod
    def update_quality(item):
        if item.sell_in > 0:
            NormalItem.quality_decrease(item, 1)
        else:
            NormalItem.quality_decrease(item, 2)
    
    @staticmethod
    def quality_increase(item, increase):
        if item.quality + increase <= NormalItem.MAX_QUAL:
            item.quality += increase
        else:
            item.quality = NormalItem.MAX_QUAL

    @staticmethod    
    def quality_decrease(item, decrease):
        if item.quality - decrease >= 0:
            item.quality -= decrease
        else:
            item.quality = 0

    @staticmethod
    def update_sell_in(item):
        item.sell_in -= 1
