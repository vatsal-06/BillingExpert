# ========Library======= #
from tkinter import*
import math
import random
from tkinter import messagebox as msg
import os


# ======App Class====== #
class Bill_App:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1340x700+0+0')
        self.root.title('Billing Expert')
        bg_color = '#00048a'
        self.root.config(bg=bg_color)

        title = Label(self.root, text='Billing Expert', bd=15, relief=GROOVE, bg=bg_color, fg='white',
                      font=('times new roman', 30, 'bold'), pady=2).pack(fill=BOTH)

        # =======Variables========== #

        # =======Cosmetics========== #
        self.soap = IntVar()
        self.deter = IntVar()
        self.paste = IntVar()
        self.cream = IntVar()
        self.gel = IntVar()
        self.spray = IntVar()

        # =======Grocery========== #
        self.bread = IntVar()
        self.milk = IntVar()
        self.vege = IntVar()
        self.eggs = IntVar()
        self.fruits = IntVar()
        self.puls_grain = IntVar()

        # =======Soft Drinks========== #
        self.cola = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        self.fanta = IntVar()
        self.thumbs = IntVar()
        self.pepsi = IntVar()

        # =======Price and Tax========== #
        self.t_cos = StringVar()
        self.t_gro = StringVar()
        self.t_soft = StringVar()
        self.tax_c = StringVar()
        self.tax_g = StringVar()
        self.tax_s = StringVar()

        # =======Customer Details========== #
        self.name = StringVar()
        self.phone = StringVar()
        self.bill_no = StringVar()

        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        self.bill_search = StringVar()

        # ======Customer Details Frame======= #
        F1 = LabelFrame(self.root, text='Customer Details', bd=10, relief=GROOVE,
                        font=('times new roman', 15, 'bold'), fg='gold', bg=bg_color)
        F1.place(x=0, y=70, relwidth=1)

        cname_lbl = Label(F1, text='Customer Name', bg=bg_color, fg='white', font=('times new roman', 18, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, textvariable=self.name, width=15, font='arial 15', bd=7, relief=SUNKEN)
        cname_txt.grid(row=0, column=1, padx=10, pady=5)

        cphone_lbl = Label(F1, text='Phone Number', bg=bg_color, fg='white', font=('times new roman', 18, 'bold'))
        cphone_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphone_txt = Entry(F1, textvariable=self.phone, width=15, font='arial 15', bd=7, relief=SUNKEN)
        cphone_txt.grid(row=0, column=3, padx=10, pady=5)

        cbill_lbl = Label(F1, text='Customer Bill No.', bg=bg_color, fg='white', font=('times new roman', 18, 'bold'))
        cbill_lbl.grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, textvariable=self.bill_search, width=15, font='arial 15', bd=7, relief=SUNKEN)
        cbill_txt.grid(row=0, column=5, padx=10, pady=5)

        bill_btn = Button(F1, command=self.find_bill, text='Search', width=12, bd=3, font='arial 15 bold')
        bill_btn.grid(row=0, column=6, padx=40, pady=10)

        # =========Cosmetics Frame========= #
        F2 = LabelFrame(self.root, text='Cosmetics', bd=10, relief=GROOVE,
                        font=('times new roman', 18, 'bold'), fg='gold', bg=bg_color)
        F2.place(x=0, y=150, width=325, height=380)

        bath_lbl = Label(F2, text='Bath Soap', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        bath_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        bath_txt = Entry(F2, textvariable=self.soap, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        bath_txt.grid(row=0, column=1, padx=10, pady=10)

        deter_lbl = Label(F2, text='Detergent', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        deter_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        deter_txt = Entry(F2, textvariable=self.deter, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        deter_txt.grid(row=1, column=1, padx=10, pady=10)

        paste_lbl = Label(F2, text='Toothpaste', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        paste_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        paste_txt = Entry(F2, textvariable=self.paste, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        paste_txt.grid(row=2, column=1, padx=10, pady=10)

        cream_lbl = Label(F2, text='Cream', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        cream_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        cream_txt = Entry(F2, textvariable=self.cream, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        cream_txt.grid(row=3, column=1, padx=10, pady=10)

        gel_lbl = Label(F2, text='All Pourpose Gel', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        gel_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        gel_txt = Entry(F2, textvariable=self.gel, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        gel_txt.grid(row=4, column=1, padx=10, pady=10)

        spray_lbl = Label(F2, text='Air Spray', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        spray_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        spray_txt = Entry(F2, textvariable=self.spray, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        spray_txt.grid(row=5, column=1, padx=10, pady=10)

        # =========Grocery Frame========= #
        F3 = LabelFrame(self.root, text='Grocery', bd=10, relief=GROOVE,
                        font=('times new roman', 18, 'bold'), fg='gold', bg=bg_color)
        F3.place(x=320, y=150, width=325, height=380)

        bread_lbl = Label(F3, text='Bread', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        bread_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        bread_txt = Entry(F3, textvariable=self.bread, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        bread_txt.grid(row=0, column=1, padx=10, pady=10)

        milk_lbl = Label(F3, text='Milk', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        milk_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        milk_txt = Entry(F3, textvariable=self.milk, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        milk_txt.grid(row=1, column=1, padx=10, pady=10)

        vege_lbl = Label(F3, text='Pack of Vegies', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        vege_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        vege_txt = Entry(F3, textvariable=self.vege, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        vege_txt.grid(row=2, column=1, padx=10, pady=10)

        egg_lbl = Label(F3, text='Dozen Eggs', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        egg_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        egg_txt = Entry(F3, textvariable=self.eggs, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        egg_txt.grid(row=3, column=1, padx=10, pady=10)

        fru_lbl = Label(F3, text='Pack of Fruits', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        fru_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        fru_txt = Entry(F3, textvariable=self.fruits, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        fru_txt.grid(row=4, column=1, padx=10, pady=10)

        pg_lbl = Label(F3, text='Pulses & Grains', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        pg_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        pg_txt = Entry(F3, textvariable=self.puls_grain, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        pg_txt.grid(row=5, column=1, padx=10, pady=10)

        # =========Soft Drinks Frame========= #
        F4 = LabelFrame(self.root, text='Soft Drinks', bd=10, relief=GROOVE,
                        font=('times new roman', 18, 'bold'), fg='gold', bg=bg_color)
        F4.place(x=640, y=150, width=325, height=380)

        cola_lbl = Label(F4, text='Coca Cola', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        cola_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        cola_txt = Entry(F4, textvariable=self.cola, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        cola_txt.grid(row=0, column=1, padx=10, pady=10)

        limca_lbl = Label(F4, text='Limca', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        limca_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        limca_txt = Entry(F4, textvariable=self.limca, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        limca_txt.grid(row=1, column=1, padx=10, pady=10)

        sprite_lbl = Label(F4, text='Sprite', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        sprite_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        sprite_txt = Entry(F4, textvariable=self.sprite, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        sprite_txt.grid(row=2, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text='Fanta', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        fanta_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')
        fanta_txt = Entry(F4, textvariable=self.fanta, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        fanta_txt.grid(row=3, column=1, padx=10, pady=10)

        thumbs_lbl = Label(F4, text='Thumbs Up', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        thumbs_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='w')
        thumbs_txt = Entry(F4, textvariable=self.thumbs, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        thumbs_txt.grid(row=4, column=1, padx=10, pady=10)

        pepsi_lbl = Label(F4, text='Pepsi', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        pepsi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        pepsi_txt = Entry(F4, textvariable=self.pepsi, width=10, font='arial 18 bold', bd=5, relief=SUNKEN)
        pepsi_txt.grid(row=5, column=1, padx=10, pady=10)

        # =========Bill Area========= #
        F5 = Frame(self.root, bd=10, relief=GROOVE, bg=bg_color)
        F5.place(x=960, y=160, width=380, height=370)
        bill_title = Label(F5, text='Bill', font='arial 18 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # =========Button Frame========= #
        F6 = LabelFrame(self.root, text='Bill Menu', bd=10, relief=GROOVE,
                        font=('times new roman', 18, 'bold'), fg='gold', bg=bg_color)
        F6.place(x=0, y=530, relwidth=1, height=170)

        m1_lbl = Label(F6, text='Total Cosmetic Price', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='w')
        m1_txt = Entry(F6, textvariable=self.t_cos, width=18, font='arial 16 bold', bd=7, relief=SUNKEN)
        m1_txt.grid(row=0, column=1, padx=1, pady=1)

        m2_lbl = Label(F6, text='Total Grocery Price', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='w')
        m2_txt = Entry(F6, textvariable=self.t_gro, width=18, font='arial 16 bold', bd=7, relief=SUNKEN)
        m2_txt.grid(row=1, column=1, padx=1, pady=1)

        m3_lbl = Label(F6, text='Total Soft Drinks Price', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='w')
        m3_txt = Entry(F6, textvariable=self.t_soft, width=18, font='arial 16 bold', bd=7, relief=SUNKEN)
        m3_txt.grid(row=2, column=1, padx=1, pady=1)

        c1_lbl = Label(F6, text='Cosmetic Tax', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        c1_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='w')
        c1_txt = Entry(F6, textvariable=self.tax_c, width=18, font='arial 16 bold', bd=7, relief=SUNKEN)
        c1_txt.grid(row=0, column=3, padx=1, pady=1)

        c2_lbl = Label(F6, text='Grocery Tax', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        c2_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='w')
        c2_txt = Entry(F6, textvariable=self.tax_g, width=18, font='arial 16 bold', bd=7, relief=SUNKEN)
        c2_txt.grid(row=1, column=3, padx=1, pady=1)

        c3_lbl = Label(F6, text='Soft Drinks Tax', font=('times new roman', 18, 'bold'), bg=bg_color, fg='white')
        c3_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='w')
        c3_txt = Entry(F6, textvariable=self.tax_s, width=18, font='arial 16 bold', bd=7, relief=SUNKEN)
        c3_txt.grid(row=2, column=3, padx=1, pady=1)

        btn_F = Frame(F6, bd=7, relief=GROOVE, bg=bg_color)
        btn_F.place(x=775, width=540, height=125)

        total_btn = Button(btn_F, command=self.total, text='Total', fg='black', pady=10, width=8, font='arial 15 bold', bd=5, relief=GROOVE)
        total_btn.grid(row=0, column=0, padx=8, pady=25)

        g_bill_btn = Button(btn_F, command=self.bill_area, text='Generate Bill', fg='black', pady=10, width=8, font='arial 15 bold', bd=5, relief=GROOVE)
        g_bill_btn.grid(row=0, column=1, padx=8, pady=25)

        clear_btn = Button(btn_F, command=self.clear_data, text='Clear', fg='black', pady=10, width=8, font='arial 15 bold', bd=5, relief=GROOVE)
        clear_btn.grid(row=0, column=2, padx=8, pady=25)

        exit_btn = Button(btn_F, command=self.exit, text='Exit', fg='black', pady=10, width=8, font='arial 15 bold', bd=5, relief=GROOVE)
        exit_btn.grid(row=0, column=3, padx=9, pady=25)

        self.welcome_bill()

    def total(self):
        self.c_soap_p = self.soap.get() * 40
        self.c_deter_p = self.deter.get() * 300
        self.c_paste_p = self.paste.get() * 60
        self.c_cream_p = self.cream.get() * 120
        self.c_gel_p = self.gel.get() * 60
        self.c_spray_p = self.spray.get() * 150

        self.cosmetic_total_price = float(
                                        self.c_soap_p +
                                        self.c_deter_p +
                                        self.c_paste_p +
                                        self.c_cream_p +
                                        self.c_gel_p +
                                        self.c_spray_p)

        self.t_cos.set('₹' + str(self.cosmetic_total_price))
        self.c_tax = round((self.cosmetic_total_price * 0.18), 2)
        self.tax_c.set('₹' + str(self.c_tax))

        self.c_bread_p = self.bread.get() * 30
        self.c_milk_p = self.milk.get() * 40
        self.c_vege_p = self.vege.get() * 100
        self.c_eggs_p = self.eggs.get() * 120
        self.c_fruits_p = self.fruits.get() * 100
        self.c_pg_p = self.puls_grain.get() * 150

        self.grocery_total_price = float(
                            self.c_bread_p +
                            self.c_milk_p +
                            self.c_vege_p +
                            self.c_eggs_p +
                            self.c_fruits_p +
                            self.c_pg_p)

        self.t_gro.set('₹' + str(self.grocery_total_price))
        self.g_tax = round((self.grocery_total_price * 0.12), 2)
        self.tax_g.set('₹' + str(self.g_tax))

        self.c_cola_p = self.cola.get() * 30
        self.c_limca_p = self.limca.get() * 30
        self.c_sprite_p = self.sprite.get() * 30
        self.c_fanta_p = self.fanta.get() * 30
        self.c_thumbs_p = self.thumbs.get() * 30
        self.c_pepsi_p = self.pepsi.get() * 30

        self.soft_drinks_total_price = float(
                                            self.c_cola_p +
                                            self.c_limca_p +
                                            self.c_sprite_p +
                                            self.c_fanta_p +
                                            self.c_thumbs_p +
                                            self.c_pepsi_p)

        self.t_soft.set('₹' + str(self.soft_drinks_total_price))
        self.s_tax = round((self.soft_drinks_total_price * 0.18), 2)
        self.tax_s.set('₹' + str(self.s_tax))

        self.total_bill = float(self.cosmetic_total_price +
                                self.grocery_total_price +
                                self.soft_drinks_total_price +

                                self.c_tax +
                                self.g_tax +
                                self.s_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, '\tWelcome to Vatsal\'s Retail Store\n')
        self.txtarea.insert(END, f'\n Bill Number: {self.bill_no.get()}')
        self.txtarea.insert(END, f'\n Customer Name: {self.name.get()}')
        self.txtarea.insert(END, f'\n Phone Number: {self.phone.get()}')
        self.txtarea.insert(END, f'\n================================================')
        self.txtarea.insert(END, f'\n Products\t\t\t\tQTY\t  Price')
        self.txtarea.insert(END, f'\n================================================')

    def bill_area(self):
        if self.name.get() == '' and self.phone.get() == '':
            msg.showerror('Error', 'Customer Details are Empty!')
        elif self.t_cos.get() == '₹0.0' and self.t_gro.get() == '₹0.0' and self.t_soft.get() == '₹0.0':
            msg.showerror('Error', 'No Product Selected!')
        else:
            self.welcome_bill()
            # ===============Cosmetics============= #
            if self.soap.get() != 0:
                self.txtarea.insert(END, f'\n Bath Soap\t\t\t\t{self.soap.get()}\t{self.c_soap_p}')
            if self.deter.get() != 0:
                self.txtarea.insert(END, f'\n Detergent\t\t\t\t{self.deter.get()}\t{self.c_deter_p}')
            if self.paste.get() != 0:
                self.txtarea.insert(END, f'\n Toothpaste\t\t\t\t{self.paste.get()}\t{self.c_paste_p}')
            if self.cream.get() != 0:
                self.txtarea.insert(END, f'\n Cream\t\t\t\t{self.cream.get()}\t{self.c_cream_p}')
            if self.gel.get() != 0:
                self.txtarea.insert(END, f'\n All Purpose Gel\t\t\t\t{self.gel.get()}\t{self.c_gel_p}')
            if self.spray.get() != 0:
                self.txtarea.insert(END, f'\n Air Spray\t\t\t\t{self.spray.get()}\t{self.c_spray_p}')

            # ===============Grocery============= #
            if self.bread.get() != 0:
                self.txtarea.insert(END, f'\n Bread\t\t\t\t{self.bread.get()}\t{self.c_bread_p}')
            if self.milk.get() != 0:
                self.txtarea.insert(END, f'\n Milk\t\t\t\t{self.milk.get()}\t{self.c_milk_p}')
            if self.vege.get() != 0:
                self.txtarea.insert(END, f'\n Pack of Vegies\t\t\t\t{self.vege.get()}\t{self.c_vege_p}')
            if self.eggs.get() != 0:
                self.txtarea.insert(END, f'\n Dozen Eggs\t\t\t\t{self.eggs.get()}\t{self.c_eggs_p}')
            if self.fruits.get() != 0:
                self.txtarea.insert(END, f'\n Pack of Fruits\t\t\t\t{self.fruits.get()}\t{self.c_fruits_p}')
            if self.puls_grain.get() != 0:
                self.txtarea.insert(END, f'\n Milk\t\t\t\t{self.puls_grain.get()}\t{self.c_pg_p}')

            # ===============Soft Drinks============= #
            if self.cola.get() != 0:
                self.txtarea.insert(END, f'\n Coca Cola\t\t\t\t{self.cola.get()}\t{self.c_cola_p}')
            if self.limca.get() != 0:
                self.txtarea.insert(END, f'\n Limca\t\t\t\t{self.limca.get()}\t{self.c_limca_p}')
            if self.sprite.get() != 0:
                self.txtarea.insert(END, f'\n Sprite\t\t\t\t{self.sprite.get()}\t{self.c_sprite_p}')
            if self.fanta.get() != 0:
                self.txtarea.insert(END, f'\n Fanta\t\t\t\t{self.fanta.get()}\t{self.c_fanta_p}')
            if self.thumbs.get() != 0:
                self.txtarea.insert(END, f'\n Thumbs Up\t\t\t\t{self.thumbs.get()}\t{self.c_thumbs_p}')
            if self.pepsi.get() != 0:
                self.txtarea.insert(END, f'\n Pepsi\t\t\t\t{self.pepsi.get()}\t{self.c_pepsi_p}')

            self.txtarea.insert(END, f'\n------------------------------------------------')

            if self.tax_c.get() != '₹0.0':
                self.txtarea.insert(END, f'\n Cosmetic Tax\t\t\t\t\t{self.tax_c.get()}')

            if self.tax_g.get() != '₹0.0':
                self.txtarea.insert(END, f'\n Grocery Tax\t\t\t\t\t{self.tax_g.get()}')

            if self.tax_s.get() != '₹0.0':
                self.txtarea.insert(END, f'\n Soft Drinks Tax\t\t\t\t\t{self.tax_s.get()}')

            self.txtarea.insert(END, f'\n------------------------------------------------')
            self.txtarea.insert(END, f'\n Total Amount\t\t\t\t\t₹{self.total_bill}')
            self.txtarea.insert(END, f'\n------------------------------------------------')
            self.save_bill()

    def save_bill(self):
        op = msg.askyesno('Save Bill', 'Do you want to save the Bill?')
        if op > 0:
            bill_data = self.txtarea.get('1.0', END)
            f1 = open('Customer Bills/' + str(self.bill_no.get()) + '.txt', 'w')
            f1.write(bill_data)
            f1.close()
            msg.showinfo('Saved', f'Bill {self.bill_no.get()} Saved Successfully!')
        else:
            return

    def find_bill(self):
        present = 'No'
        for i in os.listdir('Customer Bills/'):
            if i.split('.')[0] == self.bill_search.get():
                f1 = open(f'Customer Bills/{i}', 'r')
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = 'Yes'
        if present == 'No':
            msg.showerror('Error', 'Invalid Bill Number!')

    def clear_data(self):
        op = msg.askyesno('Clear', 'Do you want to Clear?')
        if op > 0:
            # =======Cosmetics========== #
            self.soap.set(0)
            self.deter.set(0)
            self.paste.set(0)
            self.cream.set(0)
            self.gel.set(0)
            self.spray.set(0)

            # =======Grocery========== #
            self.bread.set(0)
            self.milk.set(0)
            self.vege.set(0)
            self.eggs.set(0)
            self.fruits.set(0)
            self.puls_grain.set(0)

            # =======Soft Drinks========== #
            self.cola.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            self.fanta.set(0)
            self.thumbs.set(0)
            self.pepsi.set(0)

            # =======Price and Tax========== #
            self.t_cos.set('')
            self.t_gro.set('')
            self.t_soft.set('')
            self.tax_c.set('')
            self.tax_g.set('')
            self.tax_s.set('')

            # =======Customer Details========== #
            self.name.set('')
            self.phone.set('')
            self.bill_no.set('')
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.bill_search.set('')
            self.welcome_bill()

    def exit(self):
        op = msg.askyesno('Exit', 'Do you want to Exit?')
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
