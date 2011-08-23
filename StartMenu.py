import Creature
import TextBox
import Map
import random
import pygame
import Attributes
from pygame.locals import *
import pygame.time
import GlobalData
import PlayerData



class StartMenu:
    def __init__(self, currMap, team, player):
        self.map = currMap
        self.team = team
        self.font = pygame.font.Font(None, 24)

    def flipScreenBuffer(self):
        pygame.display.flip()    

    def menuMain(self):
        self.menu = MenuBox(self.map, self.team)
        self.open = True
        self.selection = 0
        while(True):
            self.menu.show()
            if self.selection == 0:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 1:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48+32), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 2:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48+64), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 3:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48+96), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 4:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48+128), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 5:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48+160), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 6:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48+192), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 7:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (514, 48+224), GlobalData.textureManager.spriteRects["battle"][1])        
            self.flipScreenBuffer()
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.quitFlag = 1
                    return
                elif e.type == KEYDOWN:
                    if e.key == K_UP:
                        self.selection -= 1
                        if self.selection < 0:
                            self.selection = 7   
                    elif e.key == K_DOWN:
                        self.selection += 1
                        if self.selection > 7:
                            self.selection = 0                        
                    elif e.key == K_END or e.key == 105:
                        return
                    elif e.key == K_RETURN:
                        if self.selection == 0:
                            self.menuItem()
                            break
                        elif self.selection == 1:
                            self.menuEquipment()
                            break 
                        elif self.selection == 2:
                            self.menuHTC()
                            break
                        elif self.selection == 3:
                            self.menuStatus()
                            break
                        elif self.selection == 4:
                            self.menuSettings()
                            break
                        elif self.selection == 5:
                            self.menuOrder()
                            break
                        elif self.selection == 6:
                            self.menuSave()
                            break
                        elif self.selection == 7:
                            self.menu.show()
                            self.box = TextBox.TextBox(144, 144, "  Are you sure you want to quit?")
                            self.boxOpen = True
                            self.select = 1
                            
                            while self.boxOpen:
                                self.box.draw()
                                GlobalData.display.getScreen().blit(self.font.render("            Yes            No", 0, (255,255,255)), (168, 168))
                                if self.select == 0:
                                    GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (264, 168), GlobalData.textureManager.spriteRects["battle"][1])
                                elif self.select == 1:
                                    GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (336, 168), GlobalData.textureManager.spriteRects["battle"][1])
                                pygame.display.flip()       
                                for e in pygame.event.get():
                                    if e.type == QUIT:
                                        self.quitFlag = 1
                                        return
                                    elif e.type == KEYDOWN:
                                        if e.key == K_RETURN:
                                            if self.select == 0:
                                                exit()
                                            else:
                                                self.boxOpen = False
                                                break                    
                                        elif e.key == K_LEFT:
                                            self.select -= 1
                                            if self.select < 0:
                                                self.select = 1   
                                        elif e.key == K_RIGHT:
                                            self.select += 1
                                            if self.select > 1:
                                                self.select = 0
                                                              
                pygame.event.pump()
        
        #while self.open:
        #    self.menu.show()       
        #    for e in pygame.event.get():
        #        if e.type == QUIT:
        #            self.quitFlag = 1
        #            return
        #        elif e.type == KEYDOWN:
        #            if e.key == 105:
        #                self.open = False

    def menuSave(self):
        #TODO
        pass

    def menuSettings(self):
        #TODO
        pass    

    def menuItem(self):
        self.chosen = False
        self.selection = 0
        while not self.chosen:
            self.menu.show()
            if self.selection == 0:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 1:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+32), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 2:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+64), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 3:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+96), GlobalData.textureManager.spriteRects["battle"][1])    
            self.flipScreenBuffer()
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.quitFlag = 1
                    return
                elif e.type == KEYDOWN:
                    #print len(self.WTCList)
                    if e.key == K_UP:
                        self.selection -=1
                        if self.selection < 0:
                            self.selection = len(self.team.roster) - 1       
                    elif e.key == K_DOWN:
                        self.selection += 1
                        if self.selection > len(self.team.roster) - 1:
                            self.selection = 0                      
                    elif e.key == K_END:
                        return
                    elif e.key == K_RETURN:
                        self.menuItemSelected(self.team.roster[self.selection])
                        self.chosen = True
                        break

    def menuEquipment(self):
        self.chosen = False
        self.selection = 0
        while not self.chosen:
            self.menu.show()
            if self.selection == 0:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 1:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+32), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 2:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+64), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 3:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+96), GlobalData.textureManager.spriteRects["battle"][1])    
            self.flipScreenBuffer()
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.quitFlag = 1
                    return
                elif e.type == KEYDOWN:
                    #print len(self.WTCList)
                    if e.key == K_UP:
                        self.selection -=1
                        if self.selection < 0:
                            self.selection = len(self.team.roster) - 1       
                    elif e.key == K_DOWN:
                        self.selection += 1
                        if self.selection > len(self.team.roster) - 1:
                            self.selection = 0                      
                    elif e.key == K_END:
                        return
                    elif e.key == K_RETURN:
                        self.menuEquipSelected(self.team.roster[self.selection])
                        self.chosen = True
                        break

    def menuHTC(self):
        self.chosen = False
        self.selection = 0
        while not self.chosen:
            self.menu.show()
            if self.selection == 0:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 1:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+32), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 2:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+64), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 3:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+96), GlobalData.textureManager.spriteRects["battle"][1])    
            self.flipScreenBuffer()
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.quitFlag = 1
                    return
                elif e.type == KEYDOWN:
                    #print len(self.WTCList)
                    if e.key == K_UP:
                        self.selection -=1
                        if self.selection < 0:
                            self.selection = len(self.team.roster) - 1       
                    elif e.key == K_DOWN:
                        self.selection += 1
                        if self.selection > len(self.team.roster) - 1:
                            self.selection = 0                      
                    elif e.key == K_END:
                        return
                    elif e.key == K_RETURN:
                        self.menuHTCSelected(self.team.roster[self.selection])
                        self.chosen = True
                        break
                        
    def menuStatus(self):
        self.chosen = False
        self.selection = 0
        while not self.chosen:
            self.menu.show()
            if self.selection == 0:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 1:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+32), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 2:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+64), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 3:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+96), GlobalData.textureManager.spriteRects["battle"][1])    
            self.flipScreenBuffer()
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.quitFlag = 1
                    return
                elif e.type == KEYDOWN:
                    #print len(self.WTCList)
                    if e.key == K_UP:
                        self.selection -=1
                        if self.selection < 0:
                            self.selection = len(self.team.roster) - 1       
                    elif e.key == K_DOWN:
                        self.selection += 1
                        if self.selection > len(self.team.roster) - 1:
                            self.selection = 0                      
                    elif e.key == K_END:
                        return
                    elif e.key == K_RETURN:
                        self.menuStatusSelected(self.team.roster[self.selection])
                        self.chosen = True
                        break

    def menuOrder(self):
        self.chosen = False
        self.selection = 0
        while not self.chosen:
            self.menu.show()
            if self.selection == 0:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 1:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+32), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 2:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+64), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 3:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+96), GlobalData.textureManager.spriteRects["battle"][1])    
            self.flipScreenBuffer()
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.quitFlag = 1
                    return
                elif e.type == KEYDOWN:
                    #print len(self.WTCList)
                    if e.key == K_UP:
                        self.selection -=1
                        if self.selection < 0:
                            self.selection = len(self.team.roster) - 1       
                    elif e.key == K_DOWN:
                        self.selection += 1
                        if self.selection > len(self.team.roster) - 1:
                            self.selection = 0                      
                    elif e.key == K_END:
                        return
                    elif e.key == K_RETURN:
                        self.menuOrderSelected(self.team.roster[self.selection])
                        self.chosen = True
                        break                     

    def menuWTC(self):
        self.chosen = False
        self.selection = 0
        while not self.chosen:
            self.menu.show()
            if self.selection == 0:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 1:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+32), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 2:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+64), GlobalData.textureManager.spriteRects["battle"][1])
            elif self.selection == 3:
                GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["battle"][0], (216, 96+96), GlobalData.textureManager.spriteRects["battle"][1])    
            self.flipScreenBuffer()
            for e in pygame.event.get():
                if e.type == QUIT:
                    self.quitFlag = 1
                    return
                elif e.type == KEYDOWN:
                    #print len(self.WTCList)
                    if e.key == K_UP:
                        self.selection -=1
                        if self.selection < 0:
                            self.selection = len(self.team.roster) - 1       
                    elif e.key == K_DOWN:
                        self.selection += 1
                        if self.selection > len(self.team.roster) - 1:
                            self.selection = 0                      
                    elif e.key == K_END:
                        return
                    elif e.key == K_RETURN:
                        self.menuWTCSelected(self.team.roster[self.selection])
                        self.chosen = True
                        break

    def menuItemSelected(self, player):
        self.itemList = []
        for x in player.shit:
            for y in x.types:
                if y.strip() == "ITEM":
                    self.itemList.append(x.name)

    def menuHTCSelected(self, player):
        self.HTCList = []
        for x in player.shit:
            for y in x.types:
                if y.strip() == "HTC":
                    self.HTCList.append(x.name)

    def menuEquipSelected(self, player):
        self.equipWpnList = []
        self.equipArmList = []
        for x in player.shit:
            for y in x.types:
                if y.strip() == "WPN":
                    self.equipWpnList.append(x.name)
        for x in player.shit:
            for y in x.types:
                if y.strip() == "ARM":
                    self.equipArmList.append(x.name)

    def menuOrderSelected(self, player):
        self.first = player
           

    def menuStatusSelected(self, player):
        pass

    def menuWTCSelected(self, player):
        self.WTCList = []
        for x in player.shit:
            for y in x.types:
                if y.strip() == "WTC":
                    self.WTCList.append(x.name)


#######################################
class MenuBox:    
    def __init__(self, themap, team):
        self.x = 48
        self.y = 48
        self.team = team
        self.width = 456-96
        self.height = 456-96     
        self.lines = []
        self.map = themap
        self.lineNum = 0
        self.facing = 9
        self.font = pygame.font.Font(None, 24)
        self.timer = GlobalData.timer
        
    def draw(self):
        final_lines = []
        requested_lines = self.text
        if self.font.size(requested_lines)> self.width - 24:
            words = requested_lines.split(' ')
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if self.font.size(test_line)[0] < self.width - 24:
                    accumulated_line = test_line 
                else: 
                    final_lines.append(accumulated_line) 
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
            for x in final_lines:
                if self.lineNum < 5:
                    self.lines.append(x)
                    self.lineNum += 1
                else:
                    for y in range(len(self.lines)-1):
                        self.lines[y] = self.lines[y+1]
                    self.lines[4] = x
        else: 
            if self.lineNum < 5:
                self.lines.append(requested_lines)
                self.lineNum += 1
            else:
                for x in range(len(self.lines)-1):
                    self.lines[x] = self.lines[x+1]
                self.lines[4] = requested_lines  

    def show(self):
        GlobalData.display.getScreen().fill((0,0,0))
        self.xCount = 15
        self.yCount = 15
        for x in range(self.xCount):
            for y in range(self.yCount):
                if x == 0:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][1])              
                    elif y == self.yCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][7])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][4])
                elif x == self.xCount - 1 :
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][3])              
                    elif y == self.yCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][9])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][6])
                else:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][2])              
                    elif y == self.yCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][8])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (self.x + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][5])                  
        self.yPlus = 0
        for x in self.lines:            
            GlobalData.display.getScreen().blit(self.font.render(x, 0, (255,255,255)), (self.x + 6, self.y + self.yPlus + 4))
            self.yPlus += 24        


        self.menuLines = ["Item", "Equipment", "HTC", "Status", "Settings", "Order", "Save", "Quit"]
        self.otherxCount = 6
        self.otheryCount = 11
        for x in range(self.otherxCount):
            for y in range(self.otheryCount):
                if x == 0:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][1])              
                    elif y == self.otheryCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][7])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][4])
                elif x == self.otherxCount - 1:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][3])              
                    elif y == self.otheryCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][9])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][6])
                else:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][2])              
                    elif y == self.otheryCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][8])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, self.y + y*24), GlobalData.textureManager.spriteRects["text"][5])                  
        self.yPlus = 0
        for x in self.menuLines:            
            GlobalData.display.getScreen().blit(self.font.render(x, 0, (255,255,255)), (456-48 + 6, self.y + self.yPlus + 4))
            self.yPlus += 32        

        self.yPlus = 0
	#Changed this to a while loop to prevent the stupid thing from assigning the index an object value        
	xhorizontal=0
        rosterarray = self.team.roster
        while xhorizontal <len(rosterarray):
            GlobalData.display.getScreen().blit(GlobalData.textureManager.textures[rosterarray[xhorizontal].currentSkin][0], (96,96), GlobalData.textureManager.spriteRects[rosterarray[xhorizontal].currentSkin][self.facing])
            GlobalData.display.getScreen().blit(self.font.render(xhorizontal, 0, (255,255,255)), (144, 96 + self.yPlus))
            self.facing += 1
            xhorizontal += 1
            if self.facing == 13:
                self.facing  = 9


        final_lines = []
        requested_lines = "Money   " + str(self.team.money) + " Location: " + str(self.map.name)
        if self.font.size(requested_lines)> 148 - 24:
            words = requested_lines.split(' ')
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if self.font.size(test_line)[0] < 148 - 24:
                    accumulated_line = test_line 
                else: 
                    final_lines.append(accumulated_line) 
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else: 
            final_lines = requested_lines
        GlobalData.displayLines = final_lines
        self.otherxCount = 6
        self.otheryCount = 4
        for x in range(self.otherxCount):
            for y in range(self.otheryCount):
                if x == 0:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][1])              
                    elif y == self.otheryCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][7])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][4])
                elif x == self.otherxCount - 1:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][3])              
                    elif y == self.otheryCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][9])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][6])
                else:
                    if y == 0:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][2])              
                    elif y == self.otheryCount-1:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][8])
                    else:
                        GlobalData.display.getScreen().blit(GlobalData.textureManager.textures["text"][0], (456-48 + x*24, 312 + y*24), GlobalData.textureManager.spriteRects["text"][5])                  
        self.yPlus = 0
        for x in GlobalData.displayLines:            
            GlobalData.display.getScreen().blit(self.font.render(x, 0, (255,255,255)), (456-48 + 6, 312 + self.yPlus + 4))
            self.yPlus += 32        
        #pygame.display.flip()
        #pygame.time.delay(150)
        self.timer.tick(8)
    
        
    def addText(self, text):       
        self.text = text
        self.open = True
        self.draw()
        self.show()
        pygame.display.flip()
       
