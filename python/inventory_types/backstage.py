from inventory_types.normal import NormalItem    #type: ignore

class BackstagePass(NormalItem):

    @staticmethod    
    def update_quality(item):
        if item.sell_in <= 0:
            item.quality = 0
        else:
            increase = BackstagePass.qual_increase(item)
            if item.quality + increase <= NormalItem.MAX_QUAL:
                item.quality += increase
            else:
                item.quality = NormalItem.MAX_QUAL

    @staticmethod
    def qual_increase(item):
        if item.sell_in <= 5:
            return 3
        if item.sell_in <= 10:
            return 2
        else:
            return 1

