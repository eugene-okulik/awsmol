class Flowers:
    def __init__(self, name, color, price, length, life):
        self.__name = name
        self.__color = color
        self.__price = price
        self.__length = length
        self.life = life

    @property
    def name(self):
        return self.name

    @property
    def color(self):
        return self.__color

    @property
    def price(self):
        return self.__price


class ArtificialFlowers(Flowers):
    def __init__(self, name, color, price, length):
        super().__init__(name, color, price, length, 0)
        self.fresh = False


class WildFlowers(Flowers):
    def __init__(self, name, color, price, length, life):
        super().__init__(name, color, price, length, life)
        self.fresh = True


class Bouquet:
    def __init__(self):
        self.flowers = []

    def collect_flower(self, flower):
        self.flowers.append(flower)

    def cost(self):
        total_cost = 0
        for flower in self.flowers:
            total_cost += flower.price
        return total_cost

    def flower_life(self):
        flo_life = sum(flower.life for flower in self.flowers)
        return flo_life / len(self.flowers)

    def sorting(self, param):
        return sorted(self.flowers, key=lambda x: getattr(x, param))

    def search(self, param, value):
        return [flower for flower in self.flowers if getattr(flower, param) == value]


rose = Flowers('Rose', 'Red', 500, 70, 7)
sunflower = WildFlowers('Sunflower', 'Yellow', 700, 80, 10)
lily = ArtificialFlowers('Lily', 'White', 100, 50)

bouquet = Bouquet()
bouquet.collect_flower(rose)
bouquet.collect_flower(rose)
bouquet.collect_flower(rose)
bouquet.collect_flower(sunflower)
bouquet.collect_flower(sunflower)
bouquet.collect_flower(sunflower)

print(bouquet.cost())
print(bouquet.flower_life())
print(bouquet.sorting('price'))
print(bouquet.search('color', 'Yellow'))
