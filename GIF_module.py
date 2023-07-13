
def GIF(root_name,object_name,*args,**kwargs):
	file_name=kwargs.get('file_name','1.gif')
	speed=kwargs.get('speed',10)
	loops=kwargs.get('loops',1)
	time_del=(10-speed)/100
	def play_gif(root_name):
		from PIL import Image,ImageTk,ImageSequence
		import time
		global img
		img=Image.open(file_name)
		for img in ImageSequence.Iterator(img):
			img=ImageTk.PhotoImage(img)
			object_name.config(image=img)
			root_name.update()
			time.sleep(time_del)
		

	for i in range(loops):
		play_gif(root_name)




