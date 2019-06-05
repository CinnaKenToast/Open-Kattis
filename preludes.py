#notes = dict({"Ab minor":"G# minor", 
#            "D# major":"Eb major", 
#            "A# major":"Bb major", 
#            "D# minor":"Eb minor", 
#            "A# minor":"Bb minor",
#            "Gb major":"F# major", 
#            "C# major":"Db major", 
#            "Gb minor":"F# minor", 
#            "Db minor":"C# minor", 
#            "G# major":"Ab major"}) 

notes = dict({"A#":"Bb","C#":"Db","D#":"Eb","F#":"Gb","G#":"Ab","Bb":"A#","Db":"C#","Eb":"D#","Gb":"F#","Ab":"G#"})
i=1     
music = [1,1,1,1,1]
pitch = [1,1,1,1,1]  
for x in range (5):          
    music[x], pitch[x] = input().split() 
    if music[x] == "1":       
        break  

for x in range(music):
    if music[x] in notes:
        print("Case " + str(i) + ": " + notes.get(music[x]) + " " + pitch[x])
        i = i + 1
    else:
        print("Case " + str(i) + ": " + notes.get(music[x]) + " UNIQUIE")
        i = i + 1


 





    
