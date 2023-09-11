class Cat():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    def wakeup(self):
        print(self.name.title() +"walking in the yard")
    def wash(self):
        print(self.name.title() +"washed up.")
    def drink(self):
        print(self.name.title() +"drinking milk.")

my_cat = Cat('Abrikos ', 3, 'gray')
friend_cat = Cat('Persik ', 1, 'orange')
print("My cat's name is "+my_cat.name.title()+".")
print("My cat is "+str(my_cat.age)+" years old.")
print("My cat's color is "+my_cat.color.title()+".")
my_cat.wakeup()
print("\nFriend's cat name is "+str(friend_cat.name.title())+".")
print("Friend's cat is "+str(friend_cat.age)+" years old.")
print("Friend's cat color is "+friend_cat.color.title()+".")
friend_cat.wash()
friend_cat.drink()
