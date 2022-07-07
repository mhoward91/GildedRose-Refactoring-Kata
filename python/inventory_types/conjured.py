from inventory_types.normal import NormalItem    #type: ignore

class ConjuredItem(NormalItem):
    
    @staticmethod
    def update_quality(item):
        if item.sell_in > 0:
            if item.quality >= 2:
                item.quality -= 2
        else:
            if item.quality >= 4: 
                item.quality -= 4