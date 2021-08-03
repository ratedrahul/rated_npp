from datetime import datetime
from tkinter import *
from tkinter import font, colorchooser, filedialog, messagebox,ttk
from tkinter import PhotoImage
import os

window = Tk()
window.geometry('1250x650+0+0')
window.title('  Rinku Notepad Single ++ ')
# window.wm_iconbitmap('pp.ico')

# current_font_family = 'Arial'
# current_font_size = 22
foreground_color = 'white'
background_color = '#454545'
old_text =''
# file_im = PhotoImage(file = 'C:\\Users\\rahul\\Downloads\\icon.ico')
main_menu = Menu()
# file_im = PhotoImage(file ='start_bar.ico')
# file_im = PhotoImage(file = '1.icon')
f = Menu(main_menu,tearoff = False)
e = Menu(main_menu,tearoff = False)
v = Menu(main_menu,tearoff = False)
t = Menu(main_menu,tearoff = False)
a = Menu(main_menu,tearoff = False)


############################### Toolbar ###########################

def old_settings(current_font = 'Arial',current_fontsize = 22):
# def old_settings():
	global background_color
	global foreground_color
	global current_font_family
	global current_font_size
	global old_text
	# global save_status
	try:
		with open("sample.bin",'r') as rf:
			c = rf.read()
	# print(c)
	# print('and this will be')
	# print(settings)
		settings = c[:40].split('\n')
		current_font_family = settings[0]
		if int(settings[1])%2 == 0:
			current_font_size = settings[1]
		else:
			current_font_size = settings[1]+1

		old_text = c[c.index('@@@@')+4:] 
		background_color = settings[2]
		foreground_color = settings[3]
		# save_status = settings[4]
		# print('saved status is -- ',save_status)
		# print('abhi font size he',current_font_size)
	except Exception as e:
		# print('runnning except block here in fetching')
		# print(e)
		# with open("sample.bin",'w') as wf:
		# 	wf.write(str(current_font)+'\n')
		# 	wf.write(str(current_fontsize)+'\n')
		# 	wf.write(background_color+'\n')
		# 	wf.write(foreground_color+'\n')
		# 	wf.write('@@@@'+' ')
		# 	wf.write(str(text_editor.get(1.0,END)))
		current_font_family = current_font
		current_font_size = current_fontsize

old_settings()





# print(current_font_size)
# print(current_font_family)
tool_bar = ttk.Label(window)
tool_bar.pack(side= TOP, fill = X ,pady = 3)

##### Font Box ############
font_tuples = font.families()
font_family = StringVar()
font_box = ttk.Combobox(tool_bar,width = 25, textvariable = font_family, state = 'readonly')
font_box['values']= font_tuples
font_box.current(font_tuples.index(current_font_family))
font_box.grid(row= 0, column = 0, padx = 5)

# sizebar 

size_var = IntVar()
font_size = ttk.Combobox(tool_bar,width= 4,textvariable = size_var, state = 'readonly')
font_size['values'] = tuple(range(8,80,2))
# print(font_size['values'])
font_size.current(font_size['values'].index(str(current_font_size)))
font_size.grid(row = 0, column = 4, padx = 5 )

#Bold Italic buttons

bold_img = PhotoImage(file = 'bold.png')
italic_img = PhotoImage(file = 'italic.png')

Bold = ttk.Button(tool_bar,image= bold_img)
Bold.grid(row = 0, column = 6,padx = 5)
italic = ttk.Button(tool_bar,image= italic_img)
italic.grid(row = 0, column = 7,padx = 5)

#font color button

pen = PhotoImage(file = 'color.png')
PenColor= ttk.Button(tool_bar,image = pen)
PenColor.grid(row = 0, column = 8)
# BACKGROUND COLOR BUTTON

bc_img = PhotoImage(file = 'BC.png')

BC = ttk.Button(tool_bar,image= bc_img)
BC.grid(row = 0, column = 9,padx = 5)
# italic = ttk.Button(tool_bar,image= italic_img)
# italic.grid(row = 0, column = 7,padx = 5)

# dark color

defpic = PhotoImage(file = 'default.png')
dphoto = PhotoImage(file = 'Green.png')
def_button = Button(tool_bar,image = defpic)
def_button.grid(row = 0, column = 13, padx = 5)
dark_button = Button(tool_bar,image = dphoto)
# dark_button.pack()
dark_button.grid(row = 0, column = 14, padx = 5)
# Align Buttons

copied_list = []

pastes = StringVar()
paste_combo_b = ttk.Combobox(tool_bar, width = 15, textvariable = pastes,state = 'readonly')

# entryconfigure("Copy",command=lambda: w.event_generate("<<Copy>>"))
paste_combo_b['values'] = copied_list
paste_combo_b.grid(row =0,column = 17,  padx = 5)
# print(copied_list)
save_rand = PhotoImage(file = 'saverandomly.png')
save_randomly_Button = Button(tool_bar, image = save_rand)
save_randomly_Button.grid(row =0,column = 18,  padx = 5)
	# pass


al = PhotoImage(file = 'align_l.png')
align_l = Button(tool_bar,image = al)
align_l.grid(row = 0, column = 10, padx = 5)
alc = PhotoImage(file = 'align_c.png')
align_c = Button(tool_bar,image = alc)
align_c.grid(row = 0, column = 11, padx = 5)
alr = PhotoImage(file = 'align_r.png')
align_r = Button(tool_bar,image = alr)
align_r.grid(row = 0, column = 12, padx = 5)

##################################################################
################## Text Editor ##########
# print('This two from text editor ')
# print(foreground_color)
# print(background_color)
text_editor = Text(window)
text_editor.config(fg = foreground_color,bg = background_color,wrap = 'word',insertbackground = 'white', relief = FLAT,undo = True,width = 64)
scroll_bar = Scrollbar(window)
text_editor.focus_set()
scroll_bar.pack(side = RIGHT ,fill = Y)
text_editor.pack(fill = BOTH, expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)
text_editor.insert(1.0,old_text)
# if save_status == 'False':
# 	old_text = old_text.strip()
# 	text_editor.insert(1.0,old_text)
# else:
# 	pass
text_editor.config(font = (current_font_family,current_font_size))
#################################################################
## Paste Clear button
def paste_clear(event = None):
	global copied_list
	MsgBox = messagebox.askquestion ('Clear All Copied Data','Are you sure you want to clear Complete Paste List',icon = 'warning')
	if MsgBox == 'yes':
		# print(copied_list)
		copied_list.clear()
		# print('after')
		# print(copied_list)
		copied_list = ['Empty']
		paste_combo_b['values'] = copied_list
		
		paste_combo_b.current(copied_list.index('Empty'))
	   # root.destroy()
	else:
		messagebox.showinfo('Return','You will now return to the application screen')

paste_p = PhotoImage(file = 'new11.png')

udb = Button(tool_bar,text = 'Paste Options',image = paste_p,fg = 'red',command= paste_clear)

# udb = Button(tool_bar,image = ud, command = text_editor.edit_undo)
udb.grid(row = 0, column = 16)


####### font familiy and font size functionality

def line_del(event = None):
	content = text_editor.get(1.0,'end')
	tes = content[:content.rfind('\n',0,-1)]

	# print(content)
	# print(type(content))
	# con = content.split('\n')
	# te = con.remove(con[-1])
	# tes = str(te)[1:-1]
	# print(con)

	text_editor.delete(1.0,END)
	text_editor.insert(INSERT,tes)

	# text_editor.tag_config('left',justify = LEFT)

def change_font(event = None):
	global current_font_family
	global current_font_size
	current_font_family = font_family.get()
	current_font_size = size_var.get()
	text_editor.config(font= (current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)

def change_font_size(event = None):
	global current_font_family
	global current_font_size

	current_font_family  = font_family.get()
	current_font_size = size_var.get()
	text_editor.config(font = (current_font_family,current_font_size))
# text_editor.config(font=(current_font_family,current_font_size))
font_size.bind("<<ComboboxSelected>>",change_font_size)

def change_font_minus(event = None):
	global current_font_family
	global current_font_size

	current_font_size = str(int(current_font_size) -2)
	text_editor.config(font = (current_font_family,current_font_size))

def change_font_plus(event = None):
	global current_font_family
	global current_font_size

	current_font_size = str(int(current_font_size)+2)
	text_editor.config(font = (current_font_family,current_font_size))
	
######### Bold button ############3


def change_bold(event = None):
	text_property = font.Font(font = text_editor['font'])
	if text_property.actual()['weight'] == 'normal':
		text_editor.config(font = (current_font_family,current_font_size,'bold'))
	if text_property.actual()['weight'] == 'bold':
		text_editor.config(font = (current_font_family, current_font_size,'normal'))		
Bold.config(command = change_bold)

##### Italic Button #####


def change_italic(event = None):
	text_property = font.Font(font = text_editor['font'])
	if text_property.actual()['slant'] == 'italic':
		text_editor.config(font = (current_font_family,current_font_size, 'roman'))
	if text_property.actual()['slant'] == 'roman':
		text_editor.config(font = (current_font_family,current_font_size, 'italic'))

italic.config(command = change_italic)

###### Font Color ####

def change_font_color(event = None):
	color_var = colorchooser.askcolor()
	global foreground_color
	foreground_color = color_var[1]
	text_editor.config(fg = foreground_color)

PenColor.config(command = change_font_color)

##### Background Color #####
def change_bg_color():
	global background_color
	color_b = colorchooser.askcolor()
	background_color = color_b[1]
	text_editor.config(bg = background_color)

BC.config(command = change_bg_color)

########### Dark Bg ####################
def bg_co():
	# bg_color = colorchooser.askcolor()
	global background_color
	global foreground_color
	background_color = '#093333'
	foreground_color = '#ffffff'

	text_editor.config(bg = background_color, fg = foreground_color)
dark_button.config(command = bg_co)


# Bold.bind('<Button-1>',change_bold)
############## Align Functionality #################
def align_left():
	text_content = text_editor.get(1.0,'end')
	# text_editor.tag_delete()
	text_editor.tag_config('left',justify = LEFT)
	text_editor.delete(1.0,END)
	text_editor.insert(INSERT,text_content,'left')


	# text_editor.
align_l.config(command = align_left)
def align_centre():
	text_content = text_editor.get(1.0,'end')
	# text_editor.tag_delete()
	text_editor.tag_config('center',justify = CENTER)
	text_editor.delete(1.0,END)
	text_editor.insert(INSERT,text_content,'center')


	# text_editor.
align_c.config(command = align_centre)

def align_right():
	text_content = text_editor.get(1.0,'end')
	# text_editor.tag_delete()
	text_editor.tag_config('right',justify = RIGHT)
	text_editor.delete(1.0,END)
	text_editor.insert(INSERT,text_content,'right')
# help(Label)
	# text_editor.
align_r.config(command = align_right)
#################### Status Bar #########################

status_bar = ttk.Label(window, text = 'Status Bar')
# status_bar.config(expand = False)
status_bar.pack(side = BOTTOM,after = tool_bar)
# status_bar.place(x=525, y=525, anchor="se")


text_changed = False
def new_status(event = None):
	global text_changed
	# if text_editor.entryconfigure(command=lambda: w.event_generate("<<Copy>>")):
	
	if text_editor.edit_modified():
		text_changed = True
		tstr =str(text_editor.get(1.0,END))
		words = len(tstr.split())
		line = len(tstr.split('\n'))
		characters = len(tstr)
		# words = len(text_editor.get(1.0,'end-1c').split())
		# line = len(text_editor.get(1.0,'end-1c').split('\n'))
		# characters = len(text_editor.get(1.0,'end-1c'))
		status_bar.config(text = f'{url}      Line: {line-1} Words: {words} Characters: {characters-1} ')
		# print("******************************************************")
		# print(f'Line: {line} Words: {words} Characters: {characters} ')
	text_editor.edit_modified(False)

	# print('txt editor . modified wala false kyu aa rha he check kro')


text_editor.bind('<<Modified>>',new_status)


# def undoo(event = None):
# 	# text_editor.config(undo = True)
# 	pass

# udb.config(command = undoo)
#################################################3
###################### file commands###################3
url = ''
opened = False
def open_file(event = None):
	global url
	global opened
	url = filedialog.askopenfilename(initialdir=os.getcwd(),title = 'Select File',filetypes = (('Text file','.txt'),('All file','*.*')))
	try:
		with open (url,'r') as fr:
			text_editor.delete(1.0,END)
			text_editor.insert(1.0,fr.read())
			opened = True
	except Exception as e:
		print('open file me error aaya',e)

		return

	window.title(os.path.basename(url)) 

def new_file(event =None):
	global url
	url = ''
	# po = str(text_editor.get(1.0,END))
	text_editor.delete(1.0,	END)

def save(event = None):
	global url
	# global save_status
	# try:
	if url:
		content = str(text_editor.get(1.0,END))
		# print('here url is in if block of save',url)
		try:
			with open(url,'w',encoding = 'utf-8') as fw:
				fw.write(content)
				fw.close()
		except:
			with open(url.name,'w',encoding = 'utf-8') as fw:
				fw.write(content)
				fw.close()

	else:
		# if url 
		url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',filetypes = (('Text File','*.txt'),('All Files','*.*')))
		# print('here url is in else block of save',url)
		# print('yaha url hogi',url)
		if url:

			content2 = str(text_editor.get(1.0,END))
			url.write(content2)
			url.close()
			window.title(os.path.basename(url.name))
		else:
			# print('url not found')
			pass
def save_as(event = None):
	global url
	# global save_status
	try:
		content = text_editor.get(1.0,END)
		url = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt',filetypes = (('Text File','*.txt'),('All Files','*.*')))
		# print('here url is in if block of saveas',url)
		url.write(content)
		url.close()
		# url = 
		# content = str(text_editor.get(1.0,END))
		# with open(url,'w',encoding = 'utf-8') as fw:
		# 	fw.write(content)
			# fw.close()
	except Exception as e:
		# print('save as ka error',e)
		return


# text_changed = False
def save_old_setting():
	with open("sample.bin","w") as ow:
			ow.write(current_font_family+'\n')
			ow.write(str(current_font_size)+'\n')
			ow.write(background_color+'\n')
			ow.write(foreground_color+'\n')
			# ow.write(save_status+'\n')
			ow.write('@@@@')
			# ow.write(str(text_editor.get(1.0,END)))

def save_old_setting_txt(event = None):
	with open("sample.bin","w") as ow:
		ow.write(current_font_family+'\n')
		ow.write(str(current_font_size)+'\n')
		ow.write(background_color+'\n')
		ow.write(foreground_color+'\n')
		# ow.write(save_status+'\n')
		ow.write('@@@@')
		ow.write(str(text_editor.get(1.0,END)))

def direct_close(event = None):
	# global save_status
	# save_status = 'False'
	save_old_setting_txt()
	window.destroy()

def exit_func(event = None):
	global url
	global text_changed
	# global save_status
	global opened
	ct = text_editor.get(1.0, END)


	if len(ct) == 0:
		window.destroy()
	if not url:
		save_old_setting_txt()
		window.destroy()
		return
	try:
		if text_changed:
			if opened:
				obox = messagebox.askyesnocancel('Warning','Do you want to save Changes?')
				if obox is True:
					content = str(text_editor.get(1.0,END))
					with open(url,'w',encoding = 'utf-8') as fw:
						fw.write(content)
					# save_status = True
					window.destroy()
				elif obox is False:
					new()
					save_old_setting()
					# save_old_setting()
					window.destroy()
					# return

			else:
				mbox = messagebox.askyesnocancel('Warning','Do you want to save this file?')
				if mbox is True:
					save()
					# new()
					save_old_setting()

					window.destroy()
				elif mbox is False:
					save_old_setting()
					window.destroy()
		# else:
		# 	# print('Executing exit fun')
		# 	# new_file()
		# 	# save_old_setting()
		# 	window.destroy()
	except Exception as e:
		# print(e)

		return
def find_func(event = None):

	def find():
		word = find_input.get()
		text_editor.tag_remove('match','1.0',END)
		matches = 0
		if word:
			start_pos = "1.0"
			while True:
				start_pos = text_editor.search(word,start_pos, stopindex = END)
				if not start_pos:

					break
				end_pos = f'{start_pos}+{len(word)}c'
				text_editor.tag_add('match',start_pos,end_pos)
				matches+=1
				start_pos = end_pos
				text_editor.tag_config('match',foreground = 'red',background = 'yellow')

	# find()



	def replace():
		word= find_input.get()
		replace_text = replace_input.get()
		content = text_editor.get(1.0,END)
		new_content = content.replace(word,replace_text)
		text_editor.delete(1.0,END)		
		text_editor.insert(1.0,new_content)

	filedialogue = Toplevel()
	filedialogue.title('Find/Replace')
	filedialogue.geometry('450x250+500+200')
	filedialogue.resizable(0,0)

	## Frame
	find_frame = ttk.LabelFrame(filedialogue, text = 'Find/Replace')
	find_frame.pack(pady = 20)

	## labels
	text_find_label = ttk.Label(find_frame,text = 'Find: ')
	text_replace_label = ttk.Label(find_frame, text = 'Replace')

	## entry
	find_input = ttk.Entry(find_frame,text = 'Find',width = 30)
	replace_input = ttk.Entry(find_frame, text = 'Replace', width = 30)

	## button
	find_button = ttk.Button(find_frame, text = 'Find', command = find)
	replace_button = ttk.Button(find_frame, text = 'Replace',command = replace)

	## label grid
	text_find_label.grid(row = 0, column = 0,padx = 4,pady = 4)
	text_replace_label.grid(row = 1, column = 0, padx = 4, pady = 4)

	## entry grid
	find_input.grid(row = 0, column = 1, padx = 4, pady = 4)
	replace_input.grid(row = 1, column = 1, padx = 4, pady = 4)

	# Button grid
	find_button.grid(row = 2, column = 0, padx = 8, pady = 4)	
	replace_button.grid(row = 2, column = 1, padx = 8, pady = 4)

def copy_all(event = None):
	copied_list.append(text_editor.get(1.0,END))

def paste_all(event =None):
	# text_editor.insert(INSERT,copied_list[-1])
	text_editor.insert(INSERT,pastes.get())

def cut(event = None):
	# copied_list.append(text_editor.get(1.0,END))
	window.clipboard_clear()
	window.clipboard_append(text_editor.get(1.0,END))
	text_editor.delete(1.0,END)


opp = PhotoImage(file = os.path.join("Icons","open.png"))
neww = PhotoImage(file = os.path.join("Icons","new.png"))
sa = PhotoImage(file = os.path.join("Icons","save.png"))
sav = PhotoImage(file = os.path.join("Icons","save_as.png"))
exx = PhotoImage(file = os.path.join("Icons","exit.png"))

########## Main Menu Functionalities #########################


f.add_command(label = ' Open ',image = opp, compound = LEFT, accelerator = 'ctrl+o',command = open_file)
f.add_command(label = ' New ',image = neww, compound = LEFT, accelerator = 'ctrl+n', command = new_file)
f.add_command(label = ' Save ',image = sa, compound = LEFT, accelerator = 'ctrl+s',command = save)
f.add_command(label = ' Save as', image = sav, compound = LEFT, accelerator = 'ctrl+S',command = save_as)
f.add_command(label = ' Exit ',image = exx, compound = LEFT, accelerator = 'alt+f4', command = exit_func)


fin = PhotoImage(file = os.path.join("Icons","find.png"))
cpp = PhotoImage(file = os.path.join("Icons","copy.png"))
ppp = PhotoImage(file = os.path.join("Icons","paste.png"))
cuu = PhotoImage(file = os.path.join("Icons","cut.png"))
clr = PhotoImage(file = os.path.join("Icons","clear_all.png"))



e.add_command(label = ' Find ', compound = LEFT, image =fin ,accelerator = 'Ctrl+F', command = find_func)
e.add_command(label = ' Copy all', compound = LEFT, image = cpp,accelerator = 'Control+Shift',command = copy_all)
e.add_command(label = ' Paste ', compound = LEFT, image = ppp,accelerator = 'Ctrl+v',command = lambda:text_editor.event_generate("<Control v>"))
e.add_command(label = ' Cut all',compound = LEFT, image = cuu,accelerator = 'Full Cut', command = cut)
e.add_command(label = ' Clear All ', compound = LEFT, image = clr,accelerator = 'Ctrl+Alt+X',command = lambda:text_editor.delete(1.0,END))
# e.add_command(label = ' undo ', compound = LEFT, image = ,accelerator = 'Ctrl+Z', command = lambda:text_editor.event_generate("<Control z>"))

show_statusbar = BooleanVar()
show_statusbar.set(True)
show_toolbar = BooleanVar()
show_toolbar.set(True)
def copy(event = None):
	global copied_list
	c =text_editor.selection_get()
	if len(copied_list)< 30:
		copied_list.append(c)
		# print('copied list will be ',copied_list)
		paste_combo_b['values'] = copied_list[::-1]
		try:
			paste_combo_b.current(copied_list.index(copied_list[0]))
		except Exception as e:
			# print(e)
			pass
	else:
		copied_list.remove(copied_list[0])
		copy()


def hide_toolbar():
	global show_toolbar
	if show_toolbar:
		tool_bar.pack_forget()
		show_toolbar = False
	else:
		text_editor.pack_forget()
		status_bar.pack_forget()
		tool_bar.pack(side = TOP, fill = X)
		text_editor.pack(fill = BOTH, expand = True)
		status_bar.pack(side = BOTTOM)
		show_toolbar = True

def hide_statusbar():
	global show_statusbar
	if show_statusbar:
		status_bar.pack_forget()
		show_statusbar = False
	else:
		status_bar.pack(side = BOTTOM)
		show_statusbar = True


v.add_checkbutton(label = 'Tool Bar ',onvalue = True, offvalue = 0,compound = LEFT, variable = show_toolbar,command = hide_toolbar)
v.add_checkbutton(label = 'Status Bar ',onvalue = True, offvalue = 0,compound = LEFT,variable = show_statusbar,command = hide_statusbar)
# v.add_checkbutton(label = 'Side Lines ',onvalue = True, offvalue = 0,compound = LEFT)

# v.add_checkbutton(l)
##### Reset function###########################
def reset(event = None):
	global current_font_size
	global current_font_family
	current_font_family = 'Consolas'
	current_font_size = 14
	# text_editor.config()

	text_editor.config(fg = 'white',bg = '#454545',font = (current_font_family,current_font_size))
	font_box.current(font_tuples.index(current_font_family))
	font_size.current(font_size.index(current_font_size))

def_button.config(command = reset)
#################Color Theme########################

theme_choosen = StringVar()
count = 0
color_icon = {'r_rose':'r_rose_icon.png','Light Default':'light_default.png','Full Dark':'light_default.png','Dark':'dark.png','Monokai':'monokai.png','Night Blue':'night_blue.png'}

# r_rose_icon = PhotoImage(file = os.path.join("Icons",'r_rose.png'))
r_rose_icon = PhotoImage(file = "redr.png")
light_default_icon = PhotoImage(file = "light_default.png")
light_plus_icon = PhotoImage(file = "light_plus.png")
dark_icon = PhotoImage(file = "dark.png")
monokai_icon = PhotoImage(file = "monokai.png")
night_blue_icon = PhotoImage(file = "night_blue.png")
# li = {'light_default.png','light_plus.png','dark.png','monokai.png','night_blue.png'}

# dasf afd  
color_t =(r_rose_icon,light_default_icon,light_plus_icon,dark_icon,monokai_icon,night_blue_icon)

color_dict = {
	'r_rose':('#ffffff','#620000'),
	'Light Default':('#000000','#ffffff'),
	'Full Dark':('#ffffff','#000000'),
	'Dark':('#ffffff','#474747'),
	# 'Monokai Sepia':('#ffffff','#9f8960'),
	'Monokai Sepia':('#000000','#b8a88a'),
	'Night Blue':('#ededed','#002651')
}

## Color Theme
def change_theme(event = None):
	global background_color
	global foreground_color

	choosen_THEME = theme_choosen.get()
	color_tuple = color_dict.get(choosen_THEME)
	# tu = theme_choosen.get()
	foreground_color = color_tuple[0]
	background_color = color_tuple[1]
	text_editor.config(fg = foreground_color,bg = background_color, insertbackground = foreground_color)

count = 0
for i in color_dict:
	t.add_radiobutton(label =i,image = color_t[count], variable = theme_choosen,compound =LEFT,command = change_theme)
	# t.add_radiobutton(label =i,image = color_t[count], variable = theme_choosen,compound =LEFT,command = change_theme)
	count+=1

def save_randomly_func(event = None):
	# from time import asctime
	# kk = asctime()
	
	fil = datetime.now().strftime('%d%m%Y %H%M%S')
	conten = text_editor.get(1.0,'end')
	file = conten[:10]
	liss = ['\\','/','*','?','<','>','|','\n']
	for i in file:
		if i in liss:
			file = file[:file.index(i)]
			break
	filename = os.path.expanduser('~')+'\\Documents\\My Saved Texts\\'+file+' ,'+fil+'.txt'
	# filename = os.path.join(os.path.expanduser('~')+'\\Documents\\My Saved Texts\\'+file+fil+'.txt')
	try:
		with open(filename,'w') as f:
			f.write(conten)
		messagebox.showinfo('Document Saved ','Document Saved in Folder \n'+filename)
		window.destroy()
	except Exception as e:
		print('save randomly wala error',e)
		with open('NoName_Rename_Else_Will_Be_Delete.txt','w') as f:
			f.write(conten)
		messagebox.showinfo('Document Saved ','Document Saved in home Folder \n'+os.getcwd())
		window.destroy()


	# first = text_editor[:10]+random.randint()

save_randomly_Button.config(command = save_randomly_func)
def kk(event = None):
	# m = messagebox()
	# messagebox('Kya re','bhai')
	messagebox.showinfo(title="About Developer", message='Thank you for choosing our softwares\nwrite at - rahulj6688@gmail.com for further queries & support')

def key(event = None):
	messagebox.showinfo(title="Keyboard Shortcuts", message='''Increase/Decr Font Size : Ctrl+ or ctrl - 
Delete current line : Ctrl + k
Paste from Lists : ctrl+F1,F2,F3
Save file with Random name : Ctrl + `
or Ctrl + Esc
Open any file : Ctrl + o
Save: Ctrl + s
Save_randomly : Ctrl+r
Delete from Last : Ctrl + d
Full Screen : F11 or Escape
Find : Ctrl+f
Bold/Italic : Ctrl+b/Ctrl+i
Undo/Redo : Ctrl+z/Ctrl+y''')



menun = Menu(main_menu,tearoff = False)
a.add_cascade(label ='Keyboard Shortcuts ',command = key)
a.add_cascade(label =' About us ',command = kk)




##################################################################



main_menu.add_cascade(label= 'File',menu = f)
main_menu.add_cascade(label = 'Edit',menu = e)
main_menu.add_cascade(label = 'View',menu = v)
main_menu.add_cascade(label = 'Theme',menu = t)
main_menu.add_cascade(label = 'About',menu = a)

# kkkk = Menu()
# kkkk.add_cascade(label = 'kya ')

window.config(menu = main_menu)


# input()

### bind Shortcut Keys
window.bind("<Control-n>",new_file)
window.bind("<Control-o>",open_file)
window.bind("<Control-s>",save)
window.bind("<Control-Alt-s>",save_as)
window.bind("<Alt-F4>",exit_func)
window.bind("<Control-w>",exit_func)
window.bind("<Control-f>",find_func)
# window.bind("<Control-z>",undoo)
window.bind("<Control-c>",copy)
# window.bind("<Control-->",find_func)
window.bind_all("<Control-minus>",change_font_minus)
window.bind_all("<Control-plus>",change_font_plus)
window.bind("<Control-k>",line_del)
window.bind("<Control-`>",save_randomly_func)
window.bind("<Control-r>",save_randomly_func)
window.bind("<Control-b>",change_bold)
window.bind("<Control-i>",change_italic)

# entryconfigure("Copy",command=lambda: w.event_generate("<<Copy>>"))
# window.clipboard_clear()
# 	window.clipboard_append(text_editor.get(1.0,END))
# kk = (window.__dir__())
# kk = sorted(kk)
# print(kk)
def f1(event):
	global copied_list
	# print('yaha event \fhe',event)
	kk = str(event)
	inp = kk[kk.index('keysym=')+7:kk.index('keysym=')+9]
	di = {}
	di['F1'] = -1
	di['F2'] = -2
	di['F3'] = -3
	di['F4'] = -4
	try:
		text_editor.insert(INSERT,str(copied_list[di[inp]]))
	except:
		pass


# window.attributes('-fullscreen', True)

######### Edited part

# def toggle_fullscreen(event=None):
#     # state = not state  # Just toggling the boolean
#     return "break"

# def end_fullscreen(self, event=None):
#     self.state = False
#     self.tk.attributes("-fullscreen", False)
#     return "break"
# state = False
# self.tk.bind("<F11>", self.toggle_fullscreen)
# self.tk.bind("<Escape>", self.end_fullscreen)
state1 = 0
def fullscreen(event = None):
	global state1
	# state1 = 1
	if state1 == 1:
		window.attributes("-fullscreen", False)
		state1 = 0
	else:
		window.attributes("-fullscreen", True)
		state1 = 1
window.bind("<Control-F1>",f1)
window.bind("<Control-F2>",f1)
window.bind("<Control-F3>",f1)
window.bind("<Control-F4>",f1)
window.bind("<F11>",fullscreen)
window.bind("<Escape>",fullscreen)

# window.bind("<Control-q>",save_randomly_func)
# paste_combo_b.bind("<<ComboboxSelected>>", paste_it)
paste_combo_b.bind("<<ComboboxSelected>>", paste_all)
# window.bind()
# window.bind("<Control-x>",copy)
# window.bind("<Control-MouseWheel>",find_func)
nphoto = PhotoImage(file = 'new1.png')
n_button = Button(tool_bar,image = nphoto,command = new_file)
# dark_button.pack()
n_button.grid(row = 0, column = 15, padx = 5)
# def callback():
# 	exit_func()
# 	global url
	
	# global text_changed
	# print(url)
	# if url:
	# 		print(text_editor.edit_modified())
	# 		content = str(text_editor.get(1.0,END))
	# 		with open(url,'w',encoding = 'utf-8') as fw:
	# 			fw.write(content)
	# 			# fw.close()
	# if text_editor.edit_modified():
	# 	print('yes')
	# else:
	# 			print('no')
	# 		print(text_editor.edit_modified())
	# 		# 	exit_func()
			# else:
			# 	window.destroy()
	# else:
	# 	pass
		# exit_func()
	# if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
	#     root.destroy()
# root = Tk()
# bar = ttk.Label(window, text = 'Status Bar')
# status_bar.pack(side = BOTTOM)
# window.wm_maxsize(text_editor,600,1200)
window.protocol("WM_DELETE_WINDOW", direct_close)
window.mainloop()