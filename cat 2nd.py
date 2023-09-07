class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def wakeup(self):
        print(self.name.title() +"walking in the yard")
    def wash(self):
        print(self.name.title() +"washed up.")
    def drink(self):
        print(self.name.title() +"drinking milk.")

my_cat = Cat('Maffin ', 3)
friend_cat = Cat('Barsik ', 1)
print("My cat's name is "+my_cat.name.title()+".")
print("My cat is "+str(my_cat.age)+" years old.")
my_cat.wakeup()
print("\nFriend's cat name is "+str(friend_cat.name.title())+".")
print("Friend's cat is "+str(friend_cat.age)+" years old.")
friend_cat.wash()
friend_cat.drink()
