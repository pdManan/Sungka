import pyglet
import Interface
import Engine
import random

class MainWindow(pyglet.window.Window):

	def __init__(self):
	
		pyglet.window.Window.__init__(self, width=1000, height=600, caption="Sungka",resizable=False)
		
		#Essentials
		#self.batch_draw = pyglet.graphics.Batch()
		#self.Pearls = Pearl(batch = self.batch_draw)
		self.backgroundimage=pyglet.sprite.Sprite(pyglet.resource.image('resources/background.png'),x=0, y=0)
		self.backgroundgrassleft=pyglet.sprite.Sprite(pyglet.resource.image('resources/lowerleft.png'),x=0, y=0)
		self.backgroundgrassright=pyglet.sprite.Sprite(pyglet.resource.image('resources/upperright.png'),x=self.width-324, y=self.height-460)  
		self.font_directory=pyglet.font.add_directory('resources')
		self.Bellamy=pyglet.font.add_file('resources/BELLAMY-REGULAR.otf')
		self.CFJackStory=pyglet.font.add_file('resources/CFJACKSTORY-REGULAR.ttf')
		self.backgroundimage.visible=False
		self.Instructions=Engine.readFile('resources/instructions.txt')
		self.DataFile=Engine.readFile('data.txt')
		
		#Title with outline
		self.title=pyglet.text.Label('Sunga',font_name="Bellamy",font_size=100, bold=True, x=self.width/2, y=self.height/2+self.height/4-50, anchor_x='center')
		self.title_outline=pyglet.text.Label('Sungka',font_name="Bellamy",font_size=100, bold=True, x=self.width/2+5, y=(self.height/2+self.height/4)-54, anchor_x='center',color=(0,0,0,255))
		
		#Instructions Label
		self.Instructions_Label=pyglet.text.Label('', font_name='CF Jack Story', font_size=20, color=(0,0,0,255), x=self.width/2, y=self.height-90, anchor_x='center',multiline=True, width=900)
		self.Data_Label=pyglet.text.Label('', font_name='CF Jack Story', font_size=20, color=(0,0,0,255), x=self.width/2, y=self.height-90, anchor_x='center',multiline=True, width=900)
		
		#Buttons
		self.startButton=Interface.Buttons('Start',font="CF Jack Story",size=30,x=self.width/2,y=self.height/2-30)
		self.scoresButton=Interface.Buttons('Scores',font="CF Jack Story",size=30,x=self.width/2,y=self.height/2-105)
		self.helpButton=Interface.Buttons('Help',font="CF Jack Story",size=30,x=self.width/2,y=self.height/2-180)
		self.backButton=Interface.Buttons('',font="CF Jack Story",size=25,x=50,y=self.height-60)
		self.buttonlist=[self.startButton,self.scoresButton,self.helpButton,self.backButton]
		
		#Sungka Buttons
		self.zeroButton=Interface.SungkaButtons('',font="Bellamy",size=30,x=240,y=100)
		self.oneButton=Interface.SungkaButtons('',font="Bellamy",size=30,x=330,y=100)
		self.twoButton=Interface.SungkaButtons('',font="Bellamy",size=30,x=415,y=100)
		self.threeButton=Interface.SungkaButtons('',font="Bellamy",size=30,x=500,y=100)
		self.fourButton=Interface.SungkaButtons('',font="Bellamy",size=30,x=585,y=100)
		self.fiveButton=Interface.SungkaButtons('',font="Bellamy",size=30,x=670,y=100)
		self.sixButton=Interface.SungkaButtons('',font="Bellamy",size=30,x=755,y=100)
		self.sungkabuttons=[self.zeroButton,self.oneButton,self.twoButton,self.threeButton,self.fourButton,self.fiveButton,self.sixButton]
		
		#Sungka Label *STONE COUNTERS* *PLAYER*
		self.zeroPlayerLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=240,y=220)
		self.onePlayerLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=330,y=220)
		self.twoPlayerLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=415,y=220)
		self.threePlayerLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=500,y=220)
		self.fourPlayerLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=585,y=220)
		self.fivePlayerLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=670,y=220)
		self.sixPlayerLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=755,y=220)
		self.playerBaseLabel=Interface.BaseLabel('',font="CF Jack Story",size=70,x=125,y=240)
		
		#Sungka Label *STONE COUNTERS* *ENEMY*
		self.zeroEnemyLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=240,y=330)
		self.oneEnemyLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=330,y=330)
		self.twoEnemyLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=415,y=330)
		self.threeEnemyLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=500,y=330)
		self.fourEnemyLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=585,y=330)
		self.fiveEnemyLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=670,y=330)
		self.sixEnemyLabel=Interface.SungkaLabel('',font="Bellamy",size=30,x=755,y=330)
		self.enemyBaseLabel=Interface.BaseLabel('',font="CF Jack Story",size=70,x=875,y=240)
		
		self.statusL=pyglet.text.Label('',font_name="CF Jack Story",font_size=100, bold=True, x=self.width/2, y=self.height/2+self.height/4-30, anchor_x='center')
		self.scoreL=pyglet.text.Label('',font_name="CF Jack Story",font_size=100, bold=True, x=self.width/2, y=self.height/2+self.height/4-200, anchor_x='center')
		
		#Sungka Data
		self.enemyhouse=[7]*7
		self.playerhouse=[7]*7
		self.enemyBase=0
		self.playerBase=0
		self.score=(self.playerBase,self.enemyBase)
		
	#On Start
	def update(self,dt):
		self.zeroPlayerLabel.text=str(self.playerhouse[0])
		self.onePlayerLabel.text=str(self.playerhouse[1])
		self.twoPlayerLabel.text=str(self.playerhouse[2])
		self.threePlayerLabel.text=str(self.playerhouse[3])
		self.fourPlayerLabel.text=str(self.playerhouse[4])
		self.fivePlayerLabel.text=str(self.playerhouse[5])
		self.sixPlayerLabel.text=str(self.playerhouse[6])
		self.playerBaseLabel.text=str(self.playerBase)
		self.zeroEnemyLabel.text=str(self.enemyhouse[0])
		self.oneEnemyLabel.text=str(self.enemyhouse[1])
		self.twoEnemyLabel.text=str(self.enemyhouse[2])
		self.threeEnemyLabel.text=str(self.enemyhouse[3])
		self.fourEnemyLabel.text=str(self.enemyhouse[4])
		self.fiveEnemyLabel.text=str(self.enemyhouse[5])
		self.sixEnemyLabel.text=str(self.enemyhouse[6])
		self.enemyBaseLabel.text=str(self.enemyBase)
		
		if self.enemyhouse!=[0]*7 and self.playerhouse==[0]*7:
			i=1
			em=random.randint(0,6)
			while self.enemyhouse[em]==0:
				em=random.randint(0,6)		
			print("enemy move =",em)
			placeholder,self.enemyhouse[em]=self.enemyhouse[em],0
			tempi=-em
			#movements
			while placeholder>0:
				print(placeholder)
				print(self.enemyhouse)
				print(self.playerhouse)
					
				#adding in enemy houses
				if i-tempi<7 and i-tempi>-1:
					#continuing the loop
					if self.enemyhouse[i-tempi]!=0 and placeholder==1:
						placeholder+=self.enemyhouse[i-tempi]
						self.enemyhouse[i-tempi]=0
						i+=1
						
					#taking the players house points	
					elif self.enemyhouse[i-tempi]==0 and placeholder==1:
						self.enemyBase+=1+self.playerhouse[i-tempi]
						self.playerhouse[i-tempi]=0
						placeholder-=1
						i+=1
						
					#normal	
					else:
						self.enemyhouse[i-tempi]+=1
						placeholder-=1
						i+=1
						
						
				#adding in enemy base	
				elif i-tempi==7:
					self.enemyBase+=1
					placeholder-=1
					inp=i
					i+=1
					
					if placeholder==0:
						em=random.randint(0,6)
						while self.enemyhouse[em]==0 and self.enemyhouse!=[0]*7:
							em=random.randint(0,6)
						placeholder,self.enemyhouse[em]=self.enemyhouse[em],0
						tempi=-em
						i=1
						
						
				#adding in player house		
				elif inp-i<=0 and inp-i>=-6:
					if self.playerhouse[inp-i]!=0 and placeholder==1:
						placeholder+=self.playerhouse[inp-i]
						self.playerhouse[inp-i]=0
						i+=1
						
						
					elif self.playerhouse[inp-i]==0 and placeholder==1:
						self.playerhouse[inp-i]+=1
						placeholder-=1
						i+=1
					else:
						self.playerhouse[inp-i]+=1
						placeholder-=1
						i+=1
						
						
				#adding in last place of player house		
				elif inp-i==-7:
					if self.playerhouse[inp-i]!=0 and placeholder==1:
						placeholder+=self.playerhouse[inp-i]
						self.playerhouse[inp-i]=0
						tempi=i+1
						i+=1
						
						
					elif self.playerhouse[inp-i]==0 and placeholder==1:
						self.playerhouse[inp-i]+=1
						placeholder-=1
						tempi=i+1
						i+=1
						
					else:
						self.playerhouse[inp-i]+=1
						placeholder-=1
						tempi=i+1
						i+=1
			self.update(0)		
		if self.enemyhouse==[0]*7 and self.playerhouse==[0]*7:
			self.score=(self.playerBase,self.enemyBase)
			self.enemyhouse=[7]*7
			self.playerhouse=[7]*7
			self.enemyBase=0
			self.playerBase=0
			if self.score[0]>self.score[1]:
				stat="Win"
			elif self.score[0]<self.score[1]:
				stat="Lose"
			else:
				stat="Draw"
			self.statusL.text=stat
			Engine.appendData(playerscore=self.score[0],enemyscore=self.score[1],status=stat)
			self.scoreL.text=str(self.score[0])+' VS '+str(self.score[1])
			self.backgroundgrassleft.visible=True
			self.backgroundgrassright.visible=True
			self.zeroButton.text=""
			self.oneButton.text=""
			self.twoButton.text=""
			self.threeButton.text=""
			self.fourButton.text=""
			self.fiveButton.text=""
			self.sixButton.text=""
			self.zeroPlayerLabel.text=""
			self.onePlayerLabel.text=""
			self.twoPlayerLabel.text=""
			self.threePlayerLabel.text=""
			self.fourPlayerLabel.text=""
			self.fivePlayerLabel.text=""
			self.sixPlayerLabel.text=""
			self.playerBaseLabel.text=""
			self.zeroEnemyLabel.text=""
			self.oneEnemyLabel.text=""
			self.twoEnemyLabel.text=""
			self.threeEnemyLabel.text=""
			self.fourEnemyLabel.text=""
			self.fiveEnemyLabel.text=""
			self.sixEnemyLabel.text=""
			self.enemyBaseLabel.text=""
			self.backgroundimage.visible=False
			self.DataFile=Engine.readFile('data.txt')
		
			
	def on_draw(self): 
		pyglet.gl.glClearColor(1,.859,.345,1)
		self.clear()
		self.backgroundgrassleft.draw()
		self.backgroundgrassright.draw()
		self.backgroundimage.draw()
		self.Instructions_Label.draw()
		self.backButton.draw()
		self.title_outline.draw()
		self.title.draw()
		self.startButton.draw()
		self.scoresButton.draw()
		self.helpButton.draw()
		self.zeroButton.draw()
		self.oneButton.draw()
		self.twoButton.draw()
		self.threeButton.draw()
		self.fourButton.draw()
		self.fiveButton.draw()
		self.sixButton.draw()
		self.statusL.draw()
		self.scoreL.draw()
		self.Data_Label.draw()
		
		self.zeroPlayerLabel.draw()
		self.onePlayerLabel.draw()
		self.twoPlayerLabel.draw()
		self.threePlayerLabel.draw()
		self.fourPlayerLabel.draw()
		self.fivePlayerLabel.draw()
		self.sixPlayerLabel.draw()
		self.playerBaseLabel.draw()
		self.zeroEnemyLabel.draw()
		self.oneEnemyLabel.draw()
		self.twoEnemyLabel.draw()
		self.threeEnemyLabel.draw()
		self.fourEnemyLabel.draw()
		self.fiveEnemyLabel.draw()
		self.sixEnemyLabel.draw()
		self.enemyBaseLabel.draw()
		#self.Pearls.draw()  

	#hover of mouse on buttons
	def on_mouse_motion(self,x,y,dx,dy):
		for buttons in self.buttonlist:
			buttons.MouseCheck(x,y)
		for buttons in self.sungkabuttons:
			buttons.MouseCheck(x,y)
			
	#on button press
	def on_mouse_press(self,x, y, button, modifiers):
		for buttons in self.buttonlist:
			#soundplay
			if buttons.MouseCheck(x, y):
			
				if buttons==self.startButton:
					self.backgroundimage.visible=True
					self.backgroundgrassleft.visible=False
					self.backgroundgrassright.visible=False
					self.backButton.text="Back"
					self.title.text=""
					self.title_outline.text=""
					self.startButton.text=""
					self.scoresButton.text=""
					self.helpButton.text=""
					self.zeroButton.text="1"
					self.oneButton.text="2"
					self.twoButton.text="3"
					self.threeButton.text="4"
					self.fourButton.text="5"
					self.fiveButton.text="6"
					self.sixButton.text="7"
					self.zeroPlayerLabel.text=str(self.playerhouse[0])
					self.onePlayerLabel.text=str(self.playerhouse[1])
					self.twoPlayerLabel.text=str(self.playerhouse[2])
					self.threePlayerLabel.text=str(self.playerhouse[3])
					self.fourPlayerLabel.text=str(self.playerhouse[4])
					self.fivePlayerLabel.text=str(self.playerhouse[5])
					self.sixPlayerLabel.text=str(self.playerhouse[6])
					self.playerBaseLabel.text=str(self.playerBase)
					self.zeroEnemyLabel.text=str(self.enemyhouse[0])
					self.oneEnemyLabel.text=str(self.enemyhouse[1])
					self.twoEnemyLabel.text=str(self.enemyhouse[2])
					self.threeEnemyLabel.text=str(self.enemyhouse[3])
					self.fourEnemyLabel.text=str(self.enemyhouse[4])
					self.fiveEnemyLabel.text=str(self.enemyhouse[5])
					self.sixEnemyLabel.text=str(self.enemyhouse[6])
					self.enemyBaseLabel.text=str(self.enemyBase)
					
				elif buttons==self.scoresButton:
					self.backgroundgrassleft.visible=False	
					self.backgroundgrassright.visible=True
					self.backButton.text="Back"
					self.title.text=""
					self.title_outline.text=""
					self.startButton.text=""
					self.scoresButton.text=""
					self.helpButton.text=""
					self.Data_Label.text=self.DataFile
					
				elif buttons==self.helpButton:
					self.backgroundgrassleft.visible=False
					self.backgroundgrassright.visible=False
					self.backButton.text="Back"
					self.title.text=""
					self.title_outline.text=""
					self.startButton.text=""
					self.scoresButton.text=""
					self.helpButton.text=""
					self.Instructions_Label.text=self.Instructions
					
				elif buttons==self.backButton:
					self.enemyhouse=[7]*7
					self.playerhouse=[7]*7
					self.enemyBase=0
					self.playerBase=0
					self.backgroundgrassleft.visible=True
					self.backgroundgrassright.visible=True
					self.backgroundimage.visible=False
					self.Instructions_Label.text=""
					self.backButton.text=""
					self.title.text="Sungka"
					self.title_outline.text="Sungka"
					self.startButton.text="Start"
					self.scoresButton.text="Scores"
					self.helpButton.text="Help"
					self.zeroButton.text=""
					self.oneButton.text=""
					self.twoButton.text=""
					self.threeButton.text=""
					self.fourButton.text=""
					self.fiveButton.text=""
					self.sixButton.text=""
					self.zeroPlayerLabel.text=""
					self.onePlayerLabel.text=""
					self.twoPlayerLabel.text=""
					self.threePlayerLabel.text=""
					self.fourPlayerLabel.text=""
					self.fivePlayerLabel.text=""
					self.sixPlayerLabel.text=""
					self.playerBaseLabel.text=""
					self.zeroEnemyLabel.text=""
					self.oneEnemyLabel.text=""
					self.twoEnemyLabel.text=""
					self.threeEnemyLabel.text=""
					self.fourEnemyLabel.text=""
					self.fiveEnemyLabel.text=""
					self.sixEnemyLabel.text=""
					self.enemyBaseLabel.text=""
					self.statusL.text=""
					self.scoreL.text=""
					self.Data_Label.text=""
		
		for buttons in self.sungkabuttons:
			if buttons.MouseCheck(x,y):
				self.zeroButton.text=""
				self.oneButton.text=""
				self.twoButton.text=""
				self.threeButton.text=""
				self.fourButton.text=""
				self.fiveButton.text=""
				self.sixButton.text=""
				inp=self.sungkabuttons.index(buttons)
				print(inp)
				
				if self.playerhouse!=[0]*7:
					placeholder,self.playerhouse[inp]=self.playerhouse[inp],0
					inp=inp-7
					i=1
					while placeholder>0:
						print(placeholder)
						print(self.enemyhouse)
						print(self.playerhouse)
						if inp-i<=0 and inp-i>=-7:
							if self.playerhouse[inp-i]!=0 and placeholder==1:
								placeholder+=self.playerhouse[inp-i]
								self.playerhouse[inp-i]=0
								i+=1
								
								
							elif self.playerhouse[inp-i]==0 and placeholder==1:
								self.playerBase+=1+self.enemyhouse[inp-i]
								self.enemyhouse[inp-i]=0
								placeholder-=1
							else:
								self.playerhouse[inp-i]+=1
								placeholder-=1
								i+=1
								
						elif inp-i==-8:
							self.playerBase+=1
							placeholder-=1
							tempi=i+1
							i+=1
							
							if placeholder==0:
								if self.playerhouse==[0]*7:
									pass
								else:
									break
								
								
						elif i-tempi<6 and i-tempi>-1:
							if self.enemyhouse[i-tempi]!=0 and placeholder==1:
								placeholder+=self.enemyhouse[i-tempi]
								self.enemyhouse[i-tempi]=0
								i+=1
								
								
							elif self.enemyhouse[i-tempi]==0 and placeholder==1:
								self.enemyhouse[i-tempi]+=1
								placeholder-=1
								i+=1
								
								
							else:
								self.enemyhouse[i-tempi]+=1
								placeholder-=1
								i+=1
								

							
						elif i-tempi==6:
							if self.enemyhouse[i-tempi]!=0 and placeholder==1:
								placeholder+=self.enemyhouse[i-tempi]
								inp=i
								self.enemyhouse[i-tempi]=0
								i+=1
								
								
							elif self.enemyhouse[i-tempi]==0 and placeholder==1:
								self.enemyhouse[i-tempi]+=1
								inp=i
								placeholder-=1
								i+=1
								
							else:
								self.enemyhouse[i-tempi]+=1
								placeholder-=1
								inp=i
								i+=1
								
						'''
						print()
						print(placeholder)
						print()
						print("   ",self.enemyhouse,"|",self.enemyBase)
						print(self.playerBase,"|",self.playerhouse)
						'''
					#enemy move
					else:
						if self.enemyhouse!=[0]*7:
							i=1
							em=random.randint(0,6)
							while self.enemyhouse[em]==0:
								em=random.randint(0,6)		
							print("enemy move =",em)
							placeholder,self.enemyhouse[em]=self.enemyhouse[em],0
							tempi=-em
							#movements
							while placeholder>0:
								print(placeholder)
								print(self.enemyhouse)
								print(self.playerhouse)
									
								#adding in enemy houses
								if i-tempi<7 and i-tempi>-1:
									#continuing the loop
									if self.enemyhouse[i-tempi]!=0 and placeholder==1:
										placeholder+=self.enemyhouse[i-tempi]
										self.enemyhouse[i-tempi]=0
										i+=1
										
									#taking the players house points	
									elif self.enemyhouse[i-tempi]==0 and placeholder==1:
										self.enemyBase+=1+self.playerhouse[i-tempi]
										self.playerhouse[i-tempi]=0
										placeholder-=1
										i+=1
										
									#normal	
									else:
										self.enemyhouse[i-tempi]+=1
										placeholder-=1
										i+=1
										
										
								#adding in enemy base	
								elif i-tempi==7:
									self.enemyBase+=1
									placeholder-=1
									inp=i
									i+=1
									
									if placeholder==0:
										em=random.randint(0,6)
										while self.enemyhouse[em]==0 and self.enemyhouse!=[0]*7:
											em=random.randint(0,6)
										placeholder,self.enemyhouse[em]=self.enemyhouse[em],0
										tempi=-em
										i=1
										
										
								#adding in player house		
								elif inp-i<=0 and inp-i>=-6:
									if self.playerhouse[inp-i]!=0 and placeholder==1:
										placeholder+=self.playerhouse[inp-i]
										self.playerhouse[inp-i]=0
										i+=1
										
										
									elif self.playerhouse[inp-i]==0 and placeholder==1:
										self.playerhouse[inp-i]+=1
										placeholder-=1
										i+=1
									else:
										self.playerhouse[inp-i]+=1
										placeholder-=1
										i+=1
										
										
								#adding in last place of player house		
								elif inp-i==-7:
									if self.playerhouse[inp-i]!=0 and placeholder==1:
										placeholder+=self.playerhouse[inp-i]
										self.playerhouse[inp-i]=0
										tempi=i+1
										i+=1
										
										
									elif self.playerhouse[inp-i]==0 and placeholder==1:
										self.playerhouse[inp-i]+=1
										placeholder-=1
										tempi=i+1
										i+=1
										
									else:
										self.playerhouse[inp-i]+=1
										placeholder-=1
										tempi=i+1
										i+=1
										
							'''
							print()
							print(placeholder)
							print()
							print("   ",self.enemyhouse,"|",self.enemyBase)
							print(self.playerBase,"|",self.playerhouse)
							'''
				else:
					if self.enemyhouse!=[0]*7:
						i=1
						em=random.randint(0,6)
						while self.enemyhouse[em]==0:
							em=random.randint(0,6)		
						print("enemy move =",em)
						placeholder,self.enemyhouse[em]=self.enemyhouse[em],0
						tempi=-em
						#movements
						while placeholder>0:
							print(placeholder)
							print(self.enemyhouse)
							print(self.playerhouse)
							#adding in enemy houses
							if i-tempi<7 and i-tempi>-1:
								#continuing the loop
								if self.enemyhouse[i-tempi]!=0 and placeholder==1:
									placeholder+=self.enemyhouse[i-tempi]
									self.enemyhouse[i-tempi]=0
									i+=1
									
								#taking the players house points	
								elif self.enemyhouse[i-tempi]==0 and placeholder==1:
									self.enemyBase+=1+self.playerhouse[i-tempi]
									self.playerhouse[i-tempi]=0
									placeholder-=1
									i+=1
									
								#normal	
								else:
									self.enemyhouse[i-tempi]+=1
									placeholder-=1
									i+=1
									
									
							#adding in enemy base	
							elif i-tempi==7:
								self.enemyBase+=1
								placeholder-=1
								inp=i
								i+=1
								if placeholder==0:
									em=random.randint(0,6)
									while self.enemyhouse[em]==0:
										em=random.randint(0,6)
									placeholder,self.enemyhouse[em]=self.enemyhouse[em],0
									tempi=-em
									i=1
									
									
							#adding in player house		
							elif inp-i<=0 and inp-i>=-6:
								if self.playerhouse[inp-i]!=0 and placeholder==1:
									placeholder+=self.playerhouse[inp-i]
									self.playerhouse[inp-i]=0
									i+=1
									
									
								elif self.playerhouse[inp-i]==0 and placeholder==1:
									self.playerhouse[inp-i]+=1
									placeholder-=1
									i+=1
									
								else:
									self.playerhouse[inp-i]+=1
									placeholder-=1
									i+=1
									
									
							#adding in last place of player house		
							elif inp-i==-7:
								if self.playerhouse[inp-i]!=0 and placeholder==1:
									placeholder+=self.playerhouse[inp-i]
									self.playerhouse[inp-i]=0
									tempi=i+1
									i+=1
									
									
								elif self.playerhouse[inp-i]==0 and placeholder==1:
									self.playerhouse[inp-i]+=1
									placeholder-=1
									tempi=i+1
									i+=1
									
								else:
									self.playerhouse[inp-i]+=1
									placeholder-=1
									tempi=i+1
									i+=1
				print('--------------------------------')
				print(placeholder)
				print(self.enemyhouse)	
				print(self.playerhouse)
				placeholder=0
				for x in range(len(self.sungkabuttons)):
					if self.playerhouse[x]==0:
						self.sungkabuttons[x].text=""
					else:
						self.sungkabuttons[x].text=str(x+1)
				self.update(0)
				
if __name__== '__main__':
	window=MainWindow()
		
	pyglet.app.run()