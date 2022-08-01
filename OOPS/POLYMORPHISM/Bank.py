class Bank:
  bank_name="SBI"
  def accntcrtn(self,name,ac_no):
        self.name=name
        self.ac_no=ac_no
        self.min=2000
        self.balance=self.min
  def deposite(self,dp_amnt):
        self.dp_amnt=dp_amnt
        self.balance=self.balance+self.dp_amnt
        print("your",Bank.bank_name,"account has been credited amount",self.dp_amnt)
        print("Your",Bank.bank_name,"total amount is",self.balance)
  def withdraw(self,amount):
      self.w_amount=amount
      if self.w_amount>self.balance:
          print("Insufficient balance")
      else:
          self.balance=self.balance-self.w_amount
          print("Your",Bank.bank_name,"account debited",self.dp_amnt)
          print("Your account balance=",self.balance)

ob=Bank()
ob.accntcrtn("Ashly",34667)
ob.deposite(30000)
ob.withdraw(320)




