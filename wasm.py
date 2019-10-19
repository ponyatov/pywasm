# https://www.youtube.com/watch?v=r-A78RgMhZU

const = 'const'
mul   = 'mul'
add   = 'add'

class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def __repr__(self):
        return '[%s]' % self.items

class Machine(Stack):
    def __init__(self,code):
        Stack.__init__(self)
        self.code = code
    def add(self):
        R = self.pop() ; L = self.pop() ; self.push(L + R)
    def mul(self):
        R = self.pop() ; L = self.pop() ; self.push(L * R)
    def eval(self):
        for cmd in self.code:
            op = cmd[0] ; args = cmd[1:]
            print op,args
            {
                const:lambda: self.push(args[0]),
                add  :lambda: self.add(),
                mul  :lambda: self.mul()
            }[op]()
        return self
        
def example():
    # compute 2 + 3 * 0.1
    code = [
        (const,2),
        (const,3),
        (const,0.1),
        (mul,),
        (add,)
    ]

    print Machine(code).eval()

example()

