def findNumberOfTiles(floorWidth,floorHeight,tileWidth,tileHeight):
    floorArea = floorWidth * floorHeight
    individualTileArea = tileWidth * tileHeight
    return float(floorArea) / float(individualTileArea)

def findCost(floorWidth, floorHeight, tileWidth, tileHeight,costofTile):
    return costofTile * findNumberOfTiles(floorWidth,floorHeight,tileWidth,tileHeight)


tileCost = input('Enter the cost of tile: ')
floorWidth = input('Enter the width of the floor: ')
floorHeight = input('Enter the height of the floor: ')
tileWidth = input('Enter the width of tiles: ')
tileHeight = input('Enter the height of tiles: ')

print str(findCost(floorWidth,floorHeight,tileWidth,tileHeight,tileCost))
