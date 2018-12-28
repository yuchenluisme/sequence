sentence=input("Sentence:")
screen_width=90
text_width=len(sentence)
box_width=text_width+10
left_margin=box_width//2
print()
print(''*left_margin+ '+'+'-'*(box_width-2)+'+')
print(''*left_margin+ '|'+' '*(box_width-2)+'|')
print(''*left_margin+ '|'+sentence)
print(''*left_margin+ '|'+' '*(box_width-2)+'|')
print(''*left_margin+ '+'+'-'*(box_width-2)+'+')