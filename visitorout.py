# Visitor Checkout   
def Visitorout():
    
    root3 = Tk()
    root3.title("Entry Management Software")
    root3.minsize(width=400,height=400)
    root3.geometry("600x500")


    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    
    def checkoutdetails():
        checkoutname = en1.get()
        path = '/home/coming---soon/Desktop/summergeeks/visitordetails.txt'
        file = open(path,'a')
        file.write("Name : " + visitordetails[checkoutname][0] + "\n" + "Email : " + visitordetails[checkoutname][1] + "\n" + "Phone : " + visitordetails[checkoutname][2] + "\n"+ "CheckInTime : " + visitordetails[checkoutname][3] + "\n" + "checkOutTime : " + str(datetime.datetime.now()) + "\n")
        file.write("-----------------------------------------------------------------------------------------\n")
        file.close()

        #Email to the Visitor
        msgvi['To'] = visitordetails[checkoutname][1]
        msgvi["Subject"] = "Meetin Details From the Office"

        body1 = str("Name : " + visitordetails[checkoutname][0] + "\t\t\t" + "Email : " + visitordetails[checkoutname][1] + "\t\t\t" + "Phone : " + visitordetails[checkoutname][2] + "\t\t\t"+ "CheckInTime : " + visitordetails[checkoutname][3] + "\t\t\t" + "checkOutTime : " + str(datetime.datetime.now()) + "\n")
        msgvi.attach(MIMEText(body1, 'html'))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msgvi['To'], msgvi.as_string())
        server.quit() 
        del visitordetails[checkoutname]


    def hello():
        messagebox.showinfo("CheckOut", "Your Done")

    # Logout for Visitor 
    def Logout():
        
        global labelFrame
        
        
        
        global en1,en2,en3,en4,SubmitBtn,btn1,btn2
        
        labelFrame = Frame(root3,bg='#044F67')
        labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)
        
        # Name
        lb1 = Label(labelFrame,text="Name : ", bg='#044F67', fg='white')
        lb1.place(relx=0.05,rely=0.4)
        
        en1 = Entry(labelFrame)
        en1.place(relx=0.3,rely=0.4, relwidth=0.62)
        
        
       
        #Submit Button
        btn2 = Button(root3,text="Submit",bg='black', fg='white', command=lambda:[checkoutdetails(),hello(),root3.destroy()])
        btn2.place(relx=0.53,rely=0.9, relwidth=0.2,relheight=0.1)

    
    
    Canvas1 = Canvas(root3)

    Canvas1.config(bg="#FFF9C4",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    
    headingFrame1 = Frame(root3,bg="#333945",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    
    headingLabel = Label(headingFrame2, text="Have a nice day, Visitor", fg='black')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.6, relheight=0.5)
    
    btn1 = Button(root3,text="Click to Fill the Checkout Form",bg='black', fg='white', command=Logout)
    btn1.place(relx=0.25,rely=0.3, relwidth=0.5,relheight=0.1)

    root3.mainloop()
