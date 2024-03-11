class Node:
    def __init__ (self, val, next=None,prev=None):
        self.val= val
        self.next= next
        self.prev= prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head= Node(homepage)
        self.curr= self.head

    def visit(self, url: str) -> None:
       new= Node(url)
       self.curr.next= new
       new.prev= self.curr
       self.curr= self.curr.next
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr and self.curr.next:
                self.curr=self.curr.next
        return self.curr.val


    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr and self.curr.prev:
                self.curr=self.curr.prev
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)