durations = [120,295,50,440,200,350]
Invalid = False
for d in durations :
    if d<=0:
        Invalid = True
        break

    if Invalid:
        print("Invalid duration : contains non positive duration")
    else:
     total_duration = sum(durations)
print("Total duration : ",total_duration)
print("No of songs : " , len(durations))

repeated = False
seen = []
for d in durations:
         if d in seen:
             repeated = True
             break
         seen.append(d)
if total_duration<=300:
        print("Category: Too short Playlist\nRecommendation :  Add more")
elif total_duration>=3600:
        print("Category:  Too long Playlist\nRecommendation : Shorten")
elif repeated:
        print("Category :Repetive Playlist\nRecomendation : Add variety")
else:
       if len(durations)>1 and max(durations) - min(durations)>1000:
        print("Category:Irregular playlist\nRecommendation : Adjust song lengths for better balance")
       else :
           print("Category: Balanced playlist\nRecomendation : Good listening session")