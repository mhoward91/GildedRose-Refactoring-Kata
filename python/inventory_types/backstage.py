from inventory_types.normal import NormalItem    #type: ignore

class BackstagePass(NormalItem):

    @staticmethod    
    def update_quality(item):
        if item.sell_in <= 0:
            item.quality = 0
        else:
            if item.sell_in <= 5:
                BackstagePass.quality_increase(item, 3)
            elif item.sell_in <= 10:
                BackstagePass.quality_increase(item, 2)
            else:
                BackstagePass.quality_increase(item, 1)
