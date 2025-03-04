word_dictionary={}

while True:
 print("the dictionary manegement system:")
 print("1.add a word and meaning")
 print("2.look up the word")
 print("3.list of all words")
 print("5.delete the word")
 print("4.update the dictionary word")
 print("6.exist")
 

 choice=input("enter your choice:")
 if choice=='1':
  word =input("enter the word:").lower()
  meaning=input("enter the meaning:")
  word_dictionary[word]=meaning
  print(f"word {word} added sucessfully.")

 elif choice=='2':
  word=input("enter the word to look up: ").lower()
  
  if word in word_dictionary:
    print(f"meaning of' {word}' :{word_dictionary[word]}")
  else:
   print(f"'{word}' is not found in dictionary.")

 elif choice=='3':
  if word_dictionary:
   print("list of word and meanings:")
   for word,meaning in word_dictionary.items():
    print(f"{word}: {meaning}")
  else:
   print("dictionary is empty.")

 elif choice=='4':
  word= input("enter the word to update meaning:").lower()
  updated_meaning=input("enter the new meaning:").lower()
  word_dictionary[word]=updated_meaning
  print("meaning updated sucessfully",word_dictionary)

 elif choice=='5' :
  word=input("enter the word to delete:" )
  if word in word_dictionary:
    del word_dictionary[word]
    print(f"word{word} deleted sucessfully.")
  else:
   print(f"word {word} not found in word dictionary")

 elif choice=='6':
  print("exiting the program.")
  break
 else:
  print("in valid choice try again")


  

