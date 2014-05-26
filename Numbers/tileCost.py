def findNumberOfTiles(floorWidth,floorHeight,tileWidth,tileHeight):
    floorArea = floorWidth * floorHeight
    individualTileArea = tileWidth * tileHeight
    return float(floorArea) / float(individualTileArea)

def findCost(floorWidth, floorHeight, tileWidth, tileHeight,costofTile):
    return costofTile * findNumberOfTiles(floorWidth,floorHeight,tileWidth,tileHeight)

print str(findCost(50.2,50.2,1.5,1.5,10.50))
