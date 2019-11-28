# Visitor Home Page   
def Visitor():
    
    root2 = Tk()
    root2.title("Entry Management Software")
    root2.minsize(width=400,height=400)
    root2.geometry("600x500")


    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    
    def checkindetails():
    	checkinname = en1.get()
    	checkinemail = en2.get()
    	checkinphone = en3.get()
    	visitordetails[checkinname] = [checkinname, checkinemail, checkinphone, str(datetime.datetime.now())]
    	
    	
    	#Email to Host
    	msg['To'] = hemail
    	msg["Subject"] = "CheckIn Details Of Visitor"

    	body = str("Name : " + checkinname + "\n" + "Email : " + checkinemail + "\n" + "Phone : " + checkinphone + "\n")
    	msg.attach(MIMEText(body, 'html'))

    	server = smtplib.SMTP("smtp.gmail.com", 587)
    	server.starttls()
    	server.login(msg['From'], password)
    	server.sendmail(msg['From'], msg['To'], msg.as_string())
    	server.quit()
		

    def hello():
	   	messagebox.showinfo("CheckIn", "Your Done")

    # Login for Visitor
    def Login():
	    
	    global labelFrame
	    
	    
	    
	    global en1,en2,en3,en4,SubmitBtn,btn1,btn2
	    
	    labelFrame = Frame(root2,bg='#044F67')
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
	    btn2 = Button(root2,text="Submit",bg='black', fg='white', command=lambda:[checkindetails(),hello(),root2.destroy()])
	    btn2.place(relx=0.53,rely=0.9, relwidth=0.2,relheight=0.1)


   	
    
    Canvas1 = Canvas(root2)

    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root2,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Hello, Visitor", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)
    
    btn1 = Button(root2,text="Click to Fill the Application",bg='black', fg='white', command=Login)
    btn1.place(relx=0.25,rely=0.3, relwidth=0.5,relheight=0.1)
    
    root2.mainloop()
