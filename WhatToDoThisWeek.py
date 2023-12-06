import random

a = "Video Making"
b = "Content Creation"
c = "Home Decor"
d = "Read"
e = "Photo Books"
f = "New Meals"
g = "Evaluating Businesses"
h = "Financial Planning"
i = "Modeling Agency for Mom"
j = "Update LinkedIn Profile"
k = "Create Website for Kye"
l = "2024 Holiday Brain Storming"

options = [a, b, c, d, e, f, g, h, i, j, k, l]

def choose_a_focus():
    num = random.randrange(0, len(options))
    print("This week, your project will be:\n" + options[num])

choose_a_focus()

