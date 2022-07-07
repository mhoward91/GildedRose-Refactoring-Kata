from inventory_types.normal import NormalItem    #type: ignore

class ConjuredItem(NormalItem):
    
    @staticmethod
    def update_quality(item):
        if item.sell_in > 0:
            ConjuredItem.quality_decrease(item, 2)
        else:
            ConjuredItem.quality_decrease(item, 4)