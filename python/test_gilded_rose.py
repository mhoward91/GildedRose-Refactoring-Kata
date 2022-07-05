# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_normal_qual(self):
        """a normal item loses quality each day until the sell by date"""
        items = [Item("Normal Item", 5, 30)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 29)

    def test_normal_doublequal(self):
        """a normal item loses quality twice as fast after the sell by date"""
        items = [Item("Normal Item", -5, 30)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 28)

    def test_normal_sellin(self):
        """the sell_in for a normal item decreases by 1 each day"""
        items = [Item("Normal Item", -5, 30)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].sell_in, -6)

    def test_brie_qual(self):
        """brie increases in quality with time, up to 50"""
        items = [Item("Aged Brie", 10, 40)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 41)

    def test_brie_max_qual(self):
        """brie quality does not exceed 50"""
        items = [Item("Aged Brie", 10, 50)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 50)

    def test_brie_sellin(self):
        """brie sell_in decreases by 1 each day"""
        items = [Item("Aged Brie", 10, 50)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].sell_in, 9)
        
    def test_sulfuras_qual(self):
        """sulfuras quality does not change from 80"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 80)

    def test_sulfuras_sellin(self):
        """sulfuras sell_in remains constant"""
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].sell_in, 10)
     
    def test_backstage_qual_single(self):
        """backstage quality increases by 1 with greater than 10 days until concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 21)

    def test_backstage_qual_double(self):
        """backstage quality increases by 2 with between 10 and 6 days until concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 22)

    def test_backstage_qual_triple(self):
        """backstage quality increases by 3 with between 5 and 1 day(s) until concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 23)

    def test_backstage_qual_zero(self):
        """backstage quality is 0 after the concert"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 0)

    def test_backstage_max_qual(self):
        """backstage quality can never exceed 50"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 48)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].quality, 50)

    def test_backstage_sellin(self):
        """backstage sell_in reduces by 1 each day"""
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 48)]
        inventory = GildedRose(items)
        inventory.update_quality()
        self.assertEqual(inventory.items[0].sell_in, -1)


if __name__ == '__main__':
    unittest.main()
