class node:
    def __init__(self,name,pnr,time):

        self.next=None
        self.name=name
        self.pnr=pnr
        self.time=time
        
class linked_list:

    def __init__(self):
        self.head=None

    def add(self,name,pnr,time):


        new_node=node(name,pnr,time)
        new_node.next=self.head
        self.head=new_node


    def find(self,pnr):
        temp=self.head
        k=0
        while temp:
            if temp.pnr==pnr:
                print(temp)
                print(k)
                break
            else:
                temp=temp.next
                k+=1
                

    # def cancel(self):

    #     if self.head is None:
    #         new_node=self.head
    #     else:
    #         temp=self.head
    #         while self.head:
    #             temp=temp.next
    #             temp.next=self.head



    def display(self):
        temp=self.head
        while temp:
            print(f"PNR:{temp.pnr}\n Name: {temp.name} \n TIme: {temp.time}")
            temp=temp.next

s=linked_list()
s.add(8922,"hyper",432232)
s.add(1203,"oron",9086)
s.display()
s.find(1203)