morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
letter = ".... . .-.. .-.. ---"
answer = ''
splitlist = letter.split(" ")
keys = list(morse.keys())
values = list(morse.values())
for s in splitlist:
    for m in range(len(morse)):
        if s == keys[m]:
            answer+=values[m]
print(answer)

llist = [-1, -2, -3, -4]
llist.sort()
print(llist)