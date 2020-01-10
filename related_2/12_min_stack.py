class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.smallest = []
        self.num_s = 0
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        self.stack.append(number)
        if not self.smallest:
            self.smallest.append(number)
        else:
            self.smallest.append(min(number,self.smallest[-1]))
        # if number < self.smallest:
        #     self.smallest = number
        #     self.num_s = 1
        # elif number == self.smallest:
        #     self.num_s += 1

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.smallest.pop()
        # temp = self.stack.pop()
        # if temp == self.smallest:
        #     self.num_s -= 1
        return self.stack.pop()


    """
    @return: An integer
    """
    def min(self):
        # write your code here
        # if self.num_s <= 0:
        #     self.smallest = min(self.stack)
        #     self.num_s = self.stack.count(self.smallest)
        return self.smallest[-1]


if __name__ == "__main__":
    s = MinStack()
    s.push(1)
    print(s.pop())