import random

coding = input("1 for Encoding and 0 for Decoding ")

f = open('message.txt','r')
text =f.read()
f.close()

words = text.split(" ")
f = open('message.txt','w')

coding = True if coding == "1" else False

if coding:
    nwords = []

    for word in words:
        if len(word) >= 3:
           r1 = random.choice(["dsf", "jkr", "flk", "nke", "lsa","khf","ikj","swe","jyt","mbn","xcz"])
           stnew = r1 + word[1:] + word[0] + r1
           nwords.append(stnew)

        else:
            nwords.append(word[::-1])

    

    # print(" ".join(nwords))

else:
    nwords = []

    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)

        else:
            nwords.append(word[::-1])

    # print(" ".join(nwords))
    

f = open("message.txt", "w")
f.write(" ".join(nwords))
f.close()

print("Done!")
