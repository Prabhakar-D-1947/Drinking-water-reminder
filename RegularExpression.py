import re

pattern  = "was"

text ='''Toys for Bob, Inc. is an American video game developer based in Novato, California, and founded in 1989.
The founders, Paul Reiche III and Fred Ford (both pictured),
met when Reiche sought a programmer to develop Star Control, and developed several games, 
including The Horde, Pandemonium!, and The Unholy War. In the early 2000s, the studio transitioned 
to working on licensed games before being laid off by Crystal Dynamics. It was incorporated in 2002
and Activision became their publisher before they acquired the studio in 2005. 
Credited with inventing the toys-to-life genre, the 2011 release of Skylanders: 
Spyro's Adventure was considered a technological and commercial breakthrough. '''

match = re.search(pattern, text)
print(match)


# ------------Read documentation of regular expression------------------
#website name -- regexr.com or python documentation