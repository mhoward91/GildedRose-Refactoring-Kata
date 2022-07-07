from inventory_types.normal import NormalItem    #type: ignore

class Sulfuras(NormalItem):
    
    SULF_MAX_QUAL = 80

    @staticmethod
    def update_quality(item):
        item.quality = Sulfuras.SULF_MAX_QUAL

    @staticmethod
    def update_sell_in(item):
        pass