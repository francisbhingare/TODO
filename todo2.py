#to do list using class
import uuid
# from uuid i/mport *
class todo:
    todolist=[]
    def readtodo(self):
        print(self.todolist)
    def addtodo(self):
        title=input("enter todo")
        desc=input("enter desc")
        todoobj={"id" : uuid.uuid4(),
             "title":title,
             "desc":desc}
        self.todolist.append(todoobj)
    def updatetodo(self):
        id=input("enter todoname")
        title=input("enter todo")
        desc=input("enter desc")
        for i in self.todolist:
            if i["id"]==id:
                i["title"]=title
                i["desc"]=desc
    def delete(self):
        id=input("enter todoname")
        for todo in self.todolist:
            if todo["id"]==id:
                self.todolist.remove(todo)

    def choicetodo(self):
        choice=" "
        while choice !="9":
            choice=int(input("enter the choice"))
            if choice==1:
                self.addtodo()
                self.readtodo()
            elif choice==2:
                self.updatetodo()
                self.readtodo()
            elif choice==3:
                self.readtodo()
            elif choice==4:
                self.delete()
                self.readtodo()
            else:
                print("enter a valid choice")
obj=todo()
obj.choicetodo()
