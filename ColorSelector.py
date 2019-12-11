class ColorSelector(object):
    colorArray = ['red','red-orange','orange','yellow-orange','yellow','yellow-green','green','blue-green','blue','blue-violet','violet','red-violet']
    def indexFinder(color):
        for i in ColorSelector.colorArray:
            if ColorSelector.colorArray[i]==color:
                return i
    def triad(color,self):
        index = self.indexFinder(color)
        return self.colorArray[(index+4)%len(self.colorArray)] + self.colorArray[(index+len(self.colorArray)-4)%len(self.colorArray)]

    def complementary(color):
        index = ColorSelector.indexFinder(color)
        return ColorSelector.colorArray[(index+6)%len(ColorSelector.colorArray)]

    def splitComplements(color,self):
        index = self.indexFinder(color)
        return self.colorArray[(index+5)%len(self.colorArray)] + self.colorArray[(index+7)%len(self.colorArray)]
