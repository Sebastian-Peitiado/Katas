from gilded_rose import GildedRose, Item


"""
-------- day 0 --------
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7
Sulfuras, Hand of Ragnaros, 0, 80
Sulfuras, Hand of Ragnaros, -1, 80
Backstage passes to a TAFKAL80ETC concert, 15, 20
Backstage passes to a TAFKAL80ETC concert, 10, 49
Backstage passes to a TAFKAL80ETC concert, 5, 49
Conjured Mana Cake, 3, 6

-------- day 1 --------
name, sellIn, quality
+5 Dexterity Vest, 9, 19
Aged Brie, 1, 1
Elixir of the Mongoose, 4, 6
Sulfuras, Hand of Ragnaros, 0, 80
Sulfuras, Hand of Ragnaros, -1, 80
Backstage passes to a TAFKAL80ETC concert, 14, 21
Backstage passes to a TAFKAL80ETC concert, 9, 50
Backstage passes to a TAFKAL80ETC concert, 4, 50
Conjured Mana Cake, 2, 5

"""
items = [
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
]

"""
"Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;

    Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but
    Quality drops to 0 after the concert


"""


# Update quality decrementa en un dia el valor sell in
def test_01():
    item = Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
    )

    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.sell_in == 14


# la calidad de los objetos "especiales" incrementa en 1 cuando faltan más de 10 días
def test_02():
    item = Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
    )

    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 21


# la calidad de los objetos "especiales" incrementa en 2 cuando faltan 10 días o menos
def test_03():
    item = Item(
        name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20
    )

    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 22


# la calidad de los objetos "especiales" incrementa en 3 cuando faltan 5 días o menos
def test_04():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)

    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 23


# la calidad de los objetos "especiales" cae a 0 cuando sell in es menor que cero
def test_05():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=23)

    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 0


# los items comunes decrementan en 1 la quality conforme pasan los dias
def test_06():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 19


# los items comunes decrementan en 2 la quality una vez pasada la fecha de vencimiento
def test_07():
    item = Item(name="+5 Dexterity Vest", sell_in=-1, quality=20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 18


# los items especiales no pueden superar los 50 de quality
def test_08():
    item = Item(name="Aged Brie", sell_in=-1, quality=50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 50


# sulfuras no pueden superar los 80 de quality
def test_09():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=1, quality=80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 80


# sulfuras no puede bajar de 80 de quality incluso cuando paso el vencimiento
def test_10():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 80


# los items comunes decrementan en 2 la quality una vez pasada la fecha de vencimiento
def test_11():
    item = Item(name="+5 Dexterity Vest", sell_in=-1, quality=20)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()

    assert item.quality == 18


# La representación en str es la correcta
def test_12():
    item = Item(name="+5 Dexterity Vest", sell_in=-1, quality=20)
    assert item.__repr__() == "+5 Dexterity Vest, -1, 20"
