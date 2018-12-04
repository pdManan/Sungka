import pyglet


class Buttons(pyglet.text.Label):
	def __init__(self,text,font,size,x,y):
		self.size=int(size)
		pyglet.text.Label.__init__(self,text, font_name=font, font_size=size, bold=True, color=(0,0,0,255) , x=x, y=y,anchor_x='center',width=100,height=75)
	
	def MouseCheck(self, mouseX, mouseY):
		if self.text!="":
			if self.x <= mouseX <= self.x + self.width and self.y <= mouseY <= self.y + self.height:
				self.font_size=(self.size*1.2)//1
				return True
			self.font_size=self.size
		return False
		
class SungkaButtons(pyglet.text.Label):
	def __init__(self,text,font,size,x,y):
		self.size=int(size)
		pyglet.text.Label.__init__(self, text, font_name=font, font_size=size, bold=True, color=(0,0,0,255) , x=x, y=y,width=50,height=75, align="center")
	
	def MouseCheck(self, mouseX, mouseY):
		if self.text!="":
			if self.x <= mouseX <= self.x + self.width and self.y <= mouseY <= self.y + self.height:
				self.font_size=(self.size*1.2)//1
				return True
			self.font_size=self.size
		return False	
class SungkaLabel(pyglet.text.Label):
	def __init__(self,text,font,size,x,y):
		self.size=int(size)
		pyglet.text.Label.__init__(self, text, font_name=font, font_size=size, bold=True, color=(255,255,255,255) , x=x, y=y,anchor_x='center')

class BaseLabel(pyglet.text.Label):
	def __init__(self,text,font,size,x,y):
		self.size=int(size)
		pyglet.text.Label.__init__(self, text, font_name=font, font_size=size, bold=True, color=(255,255,255,255) , x=x, y=y,anchor_x='center')






		
'''
class Pearl(pyglet.sprite.Sprite):
    def __init__(self, batch):
        pyglet.sprite.Sprite.__init__(self, pyglet.resource.image('resources/pearl.png'))
'''