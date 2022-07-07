from inventory_types.normal import NormalItem    #type: ignore

class Brie(NormalItem):
    
    @staticmethod
    def update_quality(item):
        Brie.quality_increase(item, 1)
