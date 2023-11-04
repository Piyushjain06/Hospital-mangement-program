import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
import os

from datetime import datetime


# Function to admit a patient
def admit():
    fin = open("pdata.csv", "r")
    r = csv.reader(fin)
    hd_id = int(input("Enter the hopital's ID: "))
    f = 0
    still = "y"
    while still == "y":
        for i in r:
            if i == []:
                continue
            elif int(i[0]) == hd_id:
                c = i
                print("Record found Successfully")
                f = 1
                still = "n"

            elif f == 0:
                print("\nrecord not found")
                print("---------------------------------------------")
                still = input("Do you want to add more (y/n) :")

    if f != 0:
        name = c[1]
        add = c[2]
        zip_code = c[3]
        company = c[4]
        pan = c[5]

        dt0 = datetime.now()
        dt = dt0.strftime("%d/%m/%Y %H:%M:%S")

        fout = open("Admin_record.csv", "a+")

        w = csv.writer(fout, delimiter=",")

        reader = csv.reader(fout)
        l = []
        for j in reader:
            if j == []:
                continue
            elif j[0] == hd_id:
                l.append(j)

        ipd_id = len(l) + 1
        bedno = input("Enter bed allotted to the patient: ")
        doctor = input("Enter the name of the doctor: ").title().strip()
        w.writerow(
            [ipd_id, name, add, zip_code, bedno, doctor, company, hd_id, pan, dt]
        )


# function to discharge a patient
def discharge():
    dt0 = datetime.now()
    dt = dt0.strftime("%d/%m/%Y %H:%M:%S")
    record_list0 = []
    with open("Admin_record.csv", "r") as fout:
        record = csv.reader(fout)
        for i in record:
            if i == []:
                continue
            else:
                record_list0.append(i)
    record_list = []
    for i in record_list0:
        if i not in record_list:
            record_list.append(i)
    print(record_list)
    print("---------------------------------------------------")
    id1 = input("\nEnter the Hospital's ID: ")
    print("---------------------------------------------------")
    flag2 = True
    for f in range(len(record_list)):
        if record_list[f][0] == id1:
            record_list[f][9] = str(dt)
            flag2 = False
            break

    if flag2 == True:
        print("\nPatient associated with ID: '", id1, "' was not found ")
        print("---------------------------------------------------")
    with open("Admin_record.csv", "w") as fin:
        wr = csv.writer(fin, delimiter=",")
        wr.writerows(record_list)
    if flag2 == False:
        print("\nPatient associated with ID: '", id1, "' was Successfully Discharged ")


# function to modify a record ( patient' phone number)
def modfi():
    with open("pdata.csv", "r") as fin:
        reader1 = csv.reader(fin)
        l = []
        for i in reader1:
            if i != []:
                l.append(i)
    id1 = input("\nEnter the Hospital' id: ")
    print("---------------------------------------------------")
    flag = False
    for i in range(len(l)):
        if l[i][0] == id1:
            print("Hospital id", "Name", "address", "Phone No", "pan no")
            print(f"\nThe current record  is {l[i]} ")
            print("---------------------------------------------------")
            y = int(input("\nEnter the updated Phone Number: "))
            print("---------------------------------------------------")
            l[i][4] = y
            print(f"\nUpdated record is {l[i]}")
            print("---------------------------------------------------")
            flag = True
            break
    if flag == False:
        print(f"\nRecord associated with hospital id {id1} is not present ")
    with open("pdata.csv", "w") as fout:
        writer1 = csv.writer(fout, delimiter=",")
        writer1.writerows(l)


# search a record
def searchh():
    with open("pdata.csv", "r") as fin:
        reader1 = csv.reader(fin)
        l = []
        for i in reader1:
            if i != []:
                l.append(i)
    id1 = input("\nEnter the Hospital' id: ")
    print("---------------------------------------------------")
    flag = False
    for i in range(len(l)):
        if l[i][0] == id1:
            print("Hospital id", "Name", "address", "Phone No", "pan no")
            print(l[i])
            print("---------------------------------------------------")
            flag = True
    if flag == False:
        print(f"\nRecord associated with hospital id {id1} is not present ")


# insert a record
def insr():
    fout = open("pdata.csv", "a")
    w = csv.writer(fout, delimiter=",")
    still = "y"

    while still == "y" or still == "yes":
        hd_id = int(input("Enter the Hospital ID: "))
        print("-------------------------------------------------------------")
        name = (
            input(f"\nEnter the name of the patient with hopital ID {hd_id}:  ")
            .title()
            .strip()
        )
        print("-------------------------------------------------------------")
        state = (
            input("\nEnter the State <Eg: New Delhi> of the Patient: ").title().strip()
        )
        print("-------------------------------------------------------------")
        pincode = int(input("\nEnter patient's home's zip code (Pin code): "))
        print("-------------------------------------------------------------")
        addr = input("\nEnter patient's address: ").strip()
        print("-------------------------------------------------------------")
        company = input("\nEnter the Phone Number of the Patient/Gaurdian ")
        print("-------------------------------------------------------------")
        pan = input("\nEnter the PAN number of the patient: ")
        print("---------------------------------------------")
        still = input("Do you want to add more (y/n) :")
        w.writerow([hd_id, name, addr, state + "," + str(pincode), company, pan])
    fout.close()


# delete a record
def del1():
    with open("pdata.csv", "r") as fin:
        reader1 = csv.reader(fin)
        l = []
        for i in reader1:
            if i != []:
                l.append(i)
    id1 = input("\nEnter the Hospital ID : ")
    flag = False
    for i in range(len(l)):
        if l[i][0] == id1:
            print(f"\nThe record found is {l[i]} ")
            l.pop(i)
            print("\nRecord has been successfully deleted! ")
            flag = True
            break
    if flag == False:
        print(f"\nRecord associated with ID number {id1} is not present ")
    with open("pdata.csv", "w") as fout:
        writer1 = csv.writer(fout, delimiter=",")
        writer1.writerows(l)


# display all the record present
def show():
    with open("pdata.csv", "r") as fout:
        reader1 = csv.reader(fout)
        print(["Hospital id", "Name", "address", "Phone No ", "pan no"])
        for i in reader1:
            if i != []:
                print("\n", i)


# bill gen
def billing():
    # reading data of patient from a csv
    with open("Admin_record.csv", "r") as fout:
        record_list = []
        record = csv.reader(fout)

        for i in record:
            if i == []:
                continue
            else:
                record_list.append(i)

    id1 = input("\nEnter the IP ID: ")
    print("---------------------------------------------------")
    flag2 = True

    for f in record_list:
        if f[0] == id1:
            rec = f
            print(rec)
            flag2 = False
            break

    if flag2 == True:
        print("\nPatient associated with ID: '", id1, "' was not found ")
    name = f[1]
    # creating a canvas ie page of the pdf using report lab module
    c = canvas.Canvas(f"'{name}'.pdf", pagesize=letter, bottomup=0)

    # creating logo of the page
    c.drawImage("Logo.png", 20, 20, width=50.4, height=50.4)

    # name of the hospital
    c.setFont("Helvetica-Bold", 20)
    c.drawString(88, 48, "CITY HOSPITAL")

    # heading 1
    c.setFont("Helvetica", 11)
    c.drawString(88, 63, "Super Speciality Hospital")

    # heading 2
    c.setFont("Helvetica-Bold", 12)
    c.drawString(200, 108, "Bill of Supply Inpatient Bill for Corporate(Summary)")
    c.line(200, 111.6, 495, 111.6)
    # line 2
    c.line(0, 310, 612, 310)
    # line 3
    c.line(0, 340, 612, 340)
    # heading 3
    c.drawString(5, 330, "Sl. No. ")
    c.drawString(77, 330, "Service Name")
    c.drawString(249, 330, "Amount(Rs.)")
    c.drawString(371, 330, "Discount(Rs.)")
    c.drawString(500, 330, "Net Amount(Rs.)")
    # lastline
    c.setFont("Helvetica", 10)
    c.drawString(5, 665, f"Print Date: {datetime.today()}")
    c.setFont("Helvetica", 12)
    c.drawString(10, 685, "City Hospital")
    c.drawString(10, 705, "Paschim Vihar, New Delhi-11063")
    c.drawString(10, 725, "24-Hour Helpline: +91-11-3050-3050")
    c.drawString(10, 745, "E:cityhospital@gmail.com")
    c.drawString(10, 770, "www.cityhospital.com")
    # patient details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(10, 150, f"IP ID: {rec[0]}")
    c.drawString(10, 170, f"Patient Name: {rec[1]}")
    c.drawString(10, 190, f"Patient's Address: {rec[2]},")
    c.drawString(117, 200, f"{rec[3]}")
    c.drawString(10, 230, f"Bed No. : {rec[4]}")
    c.drawString(10, 250, f"Doctor: {rec[5]} ")
    c.drawString(10, 280, f"Phone No : {rec[6]} ")
    c.drawString(360, 150, f"Hospital ID: {rec[7]}")

    c.drawString(360, 190, f"Bill Date:  {datetime.today()}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    c.drawString(360, 210, f"Bill Time:  {current_time}")
    c.drawString(360, 227, f"Admission Date & Time:  {rec[8]}")
    c.drawString(360, 247, f"Discharge Date & Time:  {current_time}")
    c.drawString(360, 270, f"PAN No. : {rec[9]}")
    c.drawString(360, 290, "GST Bill no. : 12345679")
    c.setFont("Helvetica", 12)

    # consultation fees
    c.drawString(5, 355, "1")
    c.drawString(80, 355, "Consultation")
    c.drawString(252, 355, f"{1500}")
    c.drawString(373, 355, f"{200}")
    c.drawString(503, 355, f"{1300}")

    print("---------------------------------------------------")
    drugs = int(input("\nEnter the Amount of drugs: "))
    print("---------------------------------------------------")
    medical = int(input("\nEnter the amount of medical consumables: "))
    print("---------------------------------------------------")
    procedures = int(input("\nEnter the amount of Procedures: "))
    print("---------------------------------------------------")
    room1 = int(input("\nEnter the rent of the room: "))
    print("---------------------------------------------------")

    # amount of drugs
    c.setFont("Helvetica", 12)
    c.drawString(5, 375, "2")
    c.drawString(80, 375, "Drugs")
    c.drawString(252, 375, f"{drugs}")
    c.drawString(373, 375, "0")
    c.drawString(503, 375, f"{drugs}")

    # amount of medical consumables
    c.setFont("Helvetica", 12)
    c.drawString(5, 395, "3")
    c.drawString(80, 395, "Medical Consumables")
    c.drawString(252, 395, f"{medical}")
    c.drawString(373, 395, "0")
    c.drawString(503, 395, f"{medical}")
    c.setFont("Helvetica", 12)

    # amount of procedures
    c.drawString(5, 415, "4")
    c.drawString(80, 415, "Procedures")
    c.drawString(252, 415, f"{procedures}")
    c.drawString(373, 415, "0")
    c.drawString(503, 415, f"{procedures}")
    c.setFont("Helvetica", 12)

    # room rent
    c.drawString(5, 435, "5")
    c.drawString(80, 435, "Room Rent")
    c.drawString(252, 435, f"{room1}")
    c.drawString(373, 435, f"{500}")
    c.drawString(503, 435, f"{room1-500}")
    c.setFont("Helvetica-Bold", 16)

    # grand total
    c.drawString(
        430, 647, f"Grand Total: {1300 + drugs + medical + procedures + room1 - 500}"
    )
    c.line(0, 630, 612, 630)
    c.line(0, 650, 612, 650)
    c.setFont("Helvetica", 10)
    c.drawString(503, 665, f"Hospital id: {f[7]}")
    c.showPage()
    #checking a folder named bill data. if not present creating it and saving pdf in it

    if "bill data" not in os.listdir():
        os.makedirs("bill data")
        os.chdir("bill data")
        c.save()
    else:
        os.chdir("bill data")
        c.save()
    

def report1():
    #reading a record from csv file
    with open("Admin_record.csv", "r") as fout:
        record_list = []
        record = csv.reader(fout)

        for i in record:
            if i == []:
                continue
            else:
                record_list.append(i)

    id1 = input("\nEnter the IP ID: ")
    print("---------------------------------------------------")
    flag2 = True

    for f in record_list:
        if f[0] == id1:
            rec = f
            print(rec)
            flag2 = False
            break

    if flag2 == True:
        print("\nPatient associated with ID: '", id1, "' was not found ")

    name = f[1]
    # creating a canvas ie page of the pdf using report lab module
    c1 = canvas.Canvas(f"{name}.pdf", pagesize=letter, bottomup=0)

    # logo
    c1.drawImage("Logo.png", 20, 20, width=50.4, height=50.4)

    # name of the hospital
    c1.setFont("Helvetica-Bold", 20)
    c1.drawString(88, 48, "CITY HOSPITAL")

    # heading 1
    c1.setFont("Helvetica", 11)
    c1.drawString(88, 63, "Super Speciality Hospital")

    # heading 2
    c1.setFont("Helvetica-Bold", 12)
    c1.drawString(250, 108, "Complete Blood Test")
    c1.line(200, 111.6, 420, 111.6)
    # line 2
    c1.line(0, 310, 612, 310)
    # line 3
    c1.line(0, 340, 612, 340)
    # heading 3
    c1.drawString(5, 330, "Sl. No. ")
    c1.drawString(77, 330, "Service Name")
    c1.drawString(249, 330, "Amount(Rs.)")
    c1.drawString(371, 330, "Discount(Rs.)")
    c1.drawString(500, 330, "Net Amount(Rs.)")
    # lastline
    c1.setFont("Helvetica", 10)
    c1.drawString(5, 665, f"Print Date: {datetime.today()}")
    c1.setFont("Helvetica", 12)
    c1.drawString(10, 685, "City Hospital")
    c1.drawString(10, 705, "Paschim Vihar, New Delhi-11063")
    c1.drawString(10, 725, "24-Hour Helpline: +91-11-3050-3050")
    c1.drawString(10, 745, "E:cityhospital@gmail.com")
    c1.drawString(10, 770, "www.cityhospital.com")

    print("Enter the Following Results")
    x = input("HAEMOGLOBIN:")
    y = input("RBC:")
    z = input("MCV:")
    a = input("MCH:")
    b = input("MCHC:")
    c = input("RDW:")
    d = input("WBC:")
    e = input("NEUTROPHILS:")
    f = input("LYMPHOCYTES:")
    g = input("MONOCYTES:")
    h = input("PLATELETS:")
    c1.setFont("Helvetica-Bold", 12)
    c1.drawString(10, 150, f"IP ID: {rec[0]}")
    c1.drawString(10, 170, f"Patient Name: {rec[1]}")
    c1.drawString(10, 190, f"Patient's Address: {rec[3]},")
    c1.drawString(117, 200, f"{rec[4]}")
    c1.drawString(10, 230, f"Bed No. : {rec[4]}")
    c1.drawString(10, 250, f"Doctor: {rec[5]} ")
    c1.drawString(10, 280, f"Company:  {rec[6]} ")
    c1.drawString(360, 150, f"Hospital ID: {rec[7]}")

    c1.drawString(360, 190, f"Report Date :  {datetime.today()}")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    c1.drawString(360, 210, f"Report Time:  {current_time}")
    c1.drawString(360, 230, f" Sample  Date & Time:  {rec[8]}")
    c1.drawString(360, 250, f"PAN No. : {rec[9]}")
    c1.setFont("Helvetica", 12)

    c1.drawString(27, 355, "HAEMOGLOBIN ")
    c1.drawString(235, 355, f"{x} g/dl")
    c1.drawString(500, 355, "11-14.5")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 385, "RBC")
    c1.drawString(235, 385, f"{y} * 10E12/L")
    c1.drawString(500, 385, "3.61-5.2")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 405, "M.C.V")
    c1.drawString(235, 405, f"{z}fL")
    c1.drawString(500, 405, "78.1-95.3")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 425, "M.C.H")
    c1.drawString(235, 425, f"{a}pg")
    c1.drawString(500, 425, "25.3-31.7")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 445, "M.C.H.C")
    c1.drawString(235, 445, f"{b}g/dl")
    c1.drawString(500, 445, "30.3-34.4")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 465, "R.D.W")
    c1.drawString(235, 465, f"{c}%")
    c1.drawString(500, 465, "12.1-16.9")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 495, "W.B.C")
    c1.drawString(235, 495, f"{d}*10E9/L")
    c1.drawString(500, 495, "4.6-10.8")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 515, "NEUTROPHILS")
    c1.drawString(235, 515, f"{e}%")
    c1.drawString(500, 515, "34.9-76.2")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 535, "LYMPHOCYTES")
    c1.drawString(235, 535, f"{f}%")
    c1.drawString(500, 535, "17.5-45")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 555, "MONOCYTES")
    c1.drawString(235, 555, f"{g}%")
    c1.drawString(500, 555, "3.9-10")

    c1.setFont("Helvetica", 12)
    c1.drawString(27, 575, "PLATELETS")
    c1.drawString(235, 575, f"{h}*10E9/L")
    c1.drawString(500, 575, "154-433")
    c1.showPage()
    if "Report data" not in os.listdir():
        os.makedirs("Report data")
        os.chdir("Report data")
    else:
        os.chdir("Report data")
    c1.save()


def menu():
    print(
        """\n          M E N U
-------------------------------
Choice    --->       Function

--------  --->      ----------
1         --->     Display all the records present
-----------------------------------------------------------------
2         --->     Insert/Modify/Delete/Search a  record
-----------------------------------------------------------------
3         --->     Admit a Patient
----------------------------------------------------------------------
4         --->     Discharge a Patient 
-----------------------------------------------------------------
5         --->     Create Bill
-----------------------------------------------------------------
6         --->     Create Complete Blood Test Report
-----------------------------------------------------------------
7        --->      EXIT"""
    )


def menu2():
    print(
        """\n          M E N U
-------------------------------
Choice    --->       Function
--------  --->      ----------

1        --->     Insert a new Record
-----------------------------------------------------------------
2        --->     Modify a record
----------------------------------------------------------------------
3        --->     Delete a Record
-----------------------------------------------------------------
4        --->     Search a  Record
-----------------------------------------------------------------
5         --->     Exit"""
    )


# main action block
try:
    still = "y"
    while still == "y" or still == "yes":
        menu()
        choice = int(input("Enter the choice: "))
        if choice == 1:
            show()
        elif choice == 2:
            menu2()
            choice1 = int(input("Enter the choice"))
            if choice1 == 1:
                insr()
            elif choice1 == 2:
                modfi()
            elif choice1 == 3:
                del1()
            elif choice1 == 4:
                searchh()
            elif choice == 5:
                exit()

        elif choice == 3:
            admit()
        elif choice == 4:
            discharge()
        elif choice == 5:
            billing()
            print
        elif choice == 6:
            report1()
        elif choice == 7:
            exit()

        still = input("Do you want to continue(Y/N):").strip().lower()
except Exception:
    print("Something went wrong")
