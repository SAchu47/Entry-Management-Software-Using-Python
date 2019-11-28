# Host Home Page 
def Host():
    
    root1 = Tk()
    root1.title("Entry Management Software")
    root1.minsize(width=400,height=400)
    root1.geometry("600x500")


    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    
    def hostdetails():
    	global hostemail
    	hostname = en1.get()
    	hostemail = en2.get()
    	hemail = hostemail
    	hostphone = en3.get()
    	path = '/home/coming---soon/Desktop/summergeeks/hostdetails.txt' #path to file
    	file = open(path,'a')
    	file.write("Name : " + hostname + "\n" + "Email : " + hostemail + "\n" + "Phone : " + hostphone + "\n")
    	file.write("-----------------------------------------------------------------------------------------\n")
    	file.close()

    def hello():
	   	messagebox.showinfo("Host", "Your Done")

    
    # Login for the host
    def Login():
	    
	    global labelFrame
	    
	    
	    global en1,en2,en3,en4,SubmitBtn,btn1,btn2
	    
	    labelFrame = Frame(root1,bg='#044F67')
	    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)
	    
	    # Name
	    lb1 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
	    lb1.place(relx=0.05,rely=0.1)
	    
	    en1 = Entry(labelFrame)
	    en1.place(relx=0.3,rely=0.1, relwidth=0.62)
	    
	    # Email
	    lb2 = Label(labelFrame,text="Email : ", bg='#044F67', fg='white')
	    lb2.place(relx=0.05,rely=0.4)
	    
	    en2 = Entry(labelFrame)
	    en2.place(relx=0.3,rely=0.4, relwidth=0.62)
	    
	    # Phone
	    lb3 = Label(labelFrame,text="Phone : ", bg='#044F67', fg='white')
	    lb3.place(relx=0.05,rely=0.7)
	    
	    en3 = Entry(labelFrame)
	    en3.place(relx=0.3,rely=0.7, relwidth=0.62)
	   
	    #Submit Button 
	    btn2 = Button(root1,text="Login",bg='black', fg='white', command=lambda:[hostdetails(),hello(),root1.destroy()])
	    btn2.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    
    headingFrame1 = Frame(root1,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, Host", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root1,text="Click here to Open Application",bg='black', fg='white', command=Login)
    btn1.place(relx=0.25,rely=0.3, relwidth=0.5,relheight=0.1)
    


    root1.mainloop()
