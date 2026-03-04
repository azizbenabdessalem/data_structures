class TreeNode:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 2
        if self.parent :
            prefix = spaces + "|__"
        else :
            prefix = spaces

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        count = 0
        p = self.parent

        while p:
            count += 1
            p = p.parent

        return count



def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    cellphone = TreeNode("Cell Phone")
    tv = TreeNode("TV")

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    mac = TreeNode("Mac")
    surface = TreeNode("Surface")
    thinkpad = TreeNode("Thinkpad")

    laptop.add_child(mac)
    laptop.add_child(surface)
    laptop.add_child(thinkpad)

    iphone = TreeNode("iPhone")
    samsung_phone = TreeNode("Samsung")
    pixel = TreeNode("Google Pixel")

    cellphone.add_child(iphone)
    cellphone.add_child(samsung_phone)
    cellphone.add_child(pixel)

    lg = TreeNode("LG")
    sony = TreeNode("Sony")
    samsung_tv = TreeNode("Samsung")

    tv.add_child(lg)
    tv.add_child(sony)
    tv.add_child(samsung_tv)



    return root



if __name__ == '__main__':
   root =  build_product_tree()
   root.print_tree()

   pass
