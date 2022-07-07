from inventory_types.normal import NormalItem    #type: ignore

class Brie(NormalItem):
    
    def update_quality(item):
        if item.quality < NormalItem.MAX_QUAL:
            item.quality += 1