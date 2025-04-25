from kanren import Relation, facts, run, var, conde, eq

# 1. parent: ota-ona
parent = Relation()
facts(parent,
      ("John", "Jim"),
      ("John", "Bob"),
      ("Bob", "Alice"),
      ("Jim", "Carol"),
      ("Anna", "Jim"),
      ("Anna", "Bob"),
      ("Alice", "Mia")
)

# 2. gender: jins (ayol yoki erkak)
female = Relation()
male = Relation()
facts(female, ("Anna",), ("Alice",), ("Carol",), ("Mia",))
facts(male, ("John",), ("Jim",), ("Bob",))

# 3. grandparent: buva yoki buvi
def grandparent(grand, grandchild):
    mid = var()
    return conde((parent(grand, mid), parent(mid, grandchild)))

# 4. sibling: aka-uka / opa-singil
def sibling(p1, p2):
    parent1 = var()
    return conde((parent(parent1, p1), parent(parent1, p2), ~eq(p1, p2)))

# 5. sister: opa/singil
def sister(p1, p2):
    return conde((sibling(p1, p2), female(p1)))

# 6. brother: aka/uka
def brother(p1, p2):
    return conde((sibling(p1, p2), male(p1)))
x = var()

# 1. Alice ning buvalari/buvisi
print("Alice ning buvalari/buvisi:", run(0, x, grandparent(x, "Alice")))

# 2. Bob ning opa yoki singillari kim?
print("Bobning opa/singillari:", run(0, x, sister(x, "Bob")))

# 3. Jim ning akasi yoki ukasi kim?
print("Jimning aka/ukalari:", run(0, x, brother(x, "Jim")))

# 4. Carol ning opa yoki ukasi kim?
print("Carolning opa/ukalari:", run(0, x, sibling(x, "Carol")))

# 5. John kimga buva yoki buvi bo‘ladi?
print("John buva bo‘lganlar:", run(0, x, grandparent("John", x)))

#natija
#Alice ning buvalari/buvisi: ('John', 'Anna')
#Bobning opa/singillari: ()
#Jimning aka/ukalari: ('Bob',)
#Carolning opa/ukalari: ()
#John buva bo‘lganlar: ('Alice', 'Carol')
