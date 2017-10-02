# -*- coding: utf-8 -*-
# The line above has been added to show ascii art properly
# Python script written by syrius
# Proof of concept that Marcus is morally and spiritually a broken dog
# Contact: code2lulz@protonmail.com

print("Introducing Marcus, a small neurotic retarded dog")
print("""\
          __
 \ ______/ V`-,
  }        /~~
 /_)^ --,r'
|b      |b
""")
print ("What\'s your name ?")
name = raw_input("--> ")
print ("Which exercise would you like to work with Marcus today, %s?") % name
print ("1- Sit")
print ("2- Give your paw")
print ("3- Kill yourself")
exercise = raw_input("--> ")
if exercise == "1":
    print("""\
       _
      _V.-o
     / |`-'
    (7_\\
    """)
    print ("Good dog!")
elif exercise == "2":
    print("""\
    ╭∩╮（︶︿︶）╭∩╮
    """)
    print("-------------------------")
    print("O RLY!? You ungrateful dog!")
    print("Please choose the punishment to give to Marcus")
    print("1- Kick his a$s")
    print("2- Do nothing")
    punishment = raw_input("--> ")
    if punishment == "1":
        print("""
         aie aie aie              
                ''',
        o_)O \)____)"
         \_        )
           '',,,,,,
             ||  ||
            "--'"--'
        """)
    if punishment == "2":
        print("Marcus, you lucky bastard. %s just gave you a pass to live another day.") % name
elif exercise == "3":
    print ("""
     /^------^/
     V  o o  V
      |  Y  |
       \ Q /
       """)
else:
    print("Not a valid option. Go back to school you moron.")
