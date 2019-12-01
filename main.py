from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time

#Email setup
msg = MIMEMultipart()
msg['From'] = "asccc7093@gmail.com"
msgvi = MIMEMultipart()
password = "ANSA7093*#"


root = Tk()
root.title("Entry Management Software")
root.minsize(width=400,height=400)
root.geometry("600x500")   
visitordetails = {}
hemail = ""
   
# Host Home Page 
def Host():
    
    root1 = Tk()
    root1.title("Entry Management Software")
    root1.minsize(width=400,height=400)
    root1.geometry("600x500")


    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    
    def hostdetails():
    	global hemail
    	hostname = en1.get()
    	hostemail = en2.get()
    	hemail = hostemail
    	hostphone = en3.get()
    	path = '/home/coming---soon/Desktop/summergeeks/hostdetails.txt'
    	file = open(path,'a')
    	file.write("Name : " + hostname + "\n" + "Email : " + hostemail + "\n" + "Phone : " + hostphone + "\n")
    	file.write("-----------------------------------------------------------------------------------------\n")
    	file.close()

    def hello():
	   	messagebox.showinfo("Host", "Your Done")

    
    # Login for host
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

    	body = str("Name : " + checkinname + "\t\t\t" + "Email : " + checkinemail + "\t\t\t" + "Phone : " + checkinphone + "\t\t\t")
    	msg.attach(MIMEText(body, 'html'))
    	#time.sleep(10)
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

# Take n greater than 0.25 and less than 5
same=True
n=0.3

# Adding a background image
background_image =Image.open("office.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="Welcome to Office", fg='black')
headingLabel.place(relx=0.25,rely=0.1, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="Host",bg='black', fg='white', command=Host)
btn1.place(relx=0.40,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Visitor checkin",bg='black', fg='white', command=Visitor)
btn2.place(relx=0.40,rely=0.5, relwidth=0.2,relheight=0.1)

btn3 = Button(root,text="Visitor checkout",bg='black', fg='white', command=Visitorout)
btn3.place(relx=0.40,rely=0.7, relwidth=0.2,relheight=0.1)

root.mainloop()
