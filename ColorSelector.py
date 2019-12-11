class ColorSelector(object):
    colorArray = ['red','red-orange','orange','yellow-orange','yellow','yellow-green','green','blue-green','blue','blue-violet','violet','red-violet']
    def indexFinder(color):
        for i in range(len(ColorSelector.colorArray)):
            if ColorSelector.colorArray[i]==color:
                return i
    def triad(color):
        index = ColorSelector.indexFinder(color)
        return ' the triads are '+ColorSelector.colorArray[(index+4)%len(ColorSelector.colorArray)] +' and '+ ColorSelector.colorArray[(index+len(ColorSelector.colorArray)-4)%len(ColorSelector.colorArray)]

    def complementary(color):
        index = ColorSelector.indexFinder(color)
        return ' the complementary is '+ColorSelector.colorArray[(index+6)%len(ColorSelector.colorArray)]

    def splitComplements(color):
        index = ColorSelector.indexFinder(color)
        return ' the splitcomplements are '+ColorSelector.colorArray[(index+5)%len(ColorSelector.colorArray)] +' and '+ ColorSelector.colorArray[(index+7)%len(ColorSelector.colorArray)]
    def allCombinations(color):
        return ColorSelector.complementary(color)+'\n'+ColorSelector.splitComplements(color)+'\n'+ColorSelector.triad(color)
