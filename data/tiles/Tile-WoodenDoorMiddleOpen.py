from Tile import tile

class woodenDoorMiddleOpen (tile):
    def __init__(self,parentWorld,colRow):
        super().__init__(parentWorld,colRow,18,1,255)
        self.durability = 20
        self.drop = 10
        self.physical = False
        self.lightBlock = 0
        self.updatePic()
        self.tool = "axe"

    def special(self):
        if self.parentWorld.tiles[self.column][self.row + 1][self.z] == None:
            self.parentWorld.removeTile(self.column,self.row,self.z)
        elif self.parentWorld.tiles[self.column][self.row + 1][self.z].tileType != 19:
            self.parentWorld.removeTile(self.column,self.row,self.z)
            
        if self.parentWorld.tiles[self.column][self.row - 1][self.z] == None:
            self.parentWorld.removeTile(self.column,self.row,self.z)
        elif self.parentWorld.tiles[self.column][self.row - 1][self.z].tileType != 17:
            self.parentWorld.removeTile(self.column,self.row,self.z)

    def onClick(self, obj):
        self.changeTile(21)
        self.parentWorld.tiles[self.column][self.row - 1][self.z].changeTile(20)
        self.parentWorld.tiles[self.column][self.row + 1][self.z].changeTile(22)        
        self.relight()

def setter(parentWorld, colRow):
    x = woodenDoorMiddleOpen(parentWorld, colRow)
    return x
