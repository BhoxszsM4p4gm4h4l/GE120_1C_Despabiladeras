"""

Differentiate Procedural Programming from functional Programming
Programming requires a series of steps and sequences of task in order to accomplish the goal. With this, the level of thought 
to it can be categorized into two: procedural programming & functional programming. Both types understands the same goal however with a 
different approach. 
As the name suggests, procedural programming has a procedure to follow. Dito na papasok yung mga 'if-else', while loops and for loops, and so much 
more na mga structure controls. Hindi naman necessary na sequencial siya as compared to the typical na "procedure" because there are 
problems na required to be repeated until true. Generally, mas mahahaba tong type of programming kasi hindi pa naiintroduce ang mga functional
programming. 
In contrast to functional programming where it utilizes functions in order to make the tasks easier and more organized. For this type,
dito magagamit ang infamous quote na "divide and conquer" as one gets to himay himay a big problem into much smaller scales, kaya nga
ang tawag ay "divide" to make everything more digestable. With this, it is time to conquer those aforementioned smaller scale problems with
what we have -- functions. These functions consists of the codes to be used dun nga sa mga small problems. The beauty of this is pwedeng pwede
mo ulit ulitin yung function with different variables agad agad without making it into a bigger fuss compared dun sa procedural. You can just 
call on the function again and lagyan mo ng panibagong argument sa loob () and then the task can be ran down.

How does Git help in the Collaborative Development and Version Control Environment of programming
It is a collaborative platform in general lalo na para sa mga coders like it makes the codes of each other accessible with one another under 
repositories for collaborative processes. In gif, meron tayong mga versions ng codes na tinatawag na napupush back sa ating repositories
and dun na lumalabas yung mga changes na nagawa natin in that file. And how is this relevant? It lets the users compare the changes prior to
another ones modifications. For example, si A ay may ginawang file and nasave as this version A. Si B rin ay may ginawang pagbabago dun sa code
file and yun pala ay mas namali niya yung code. Mawawala ba forever yung code na tama from A? The correct version can be once again retrieved 
through these branches na makikita sa github. Additionally, makikita mo rin dito what went wrong or what went right too, thus making the user
experience more educational.

When should one use a while loop and when should one use for loop? Give examples in the field of Geomatics
In the case of While loops, it can be used to check whether the traverse to be sketched is still within the range of the error. As the user 
adds a new line with its data, the values should then be calculated until its the end of data gathering, and sana nakadisplay parin ang rec
para makita sa umpisa palang na kung puwede pa bang masalba itong attempt or malayo na talaga. 
For for loops, we can use it on operations that, in a way, has more conditions as compared to while. Rather than waiting for the condition to 
not be true, meron pa tayong pwedeng ibigay na something else hanggang sa maging totoo. We can use this method for adding up cummulative values hanggang its 
pinakapoint; then it can be broken. 


Discuss the divide and conquer paradigm in coding
In dealing with problems, especially yung mga malalaki, it would be best to simply do it within your pace. with this, mas maganda na hati hatiin muna ang m
mga problema into smaller problems para ayon, gawing maayos yung isang bagay. this topic goes well with functioning na programming kasi in this 
case, ginagamit na nila ang mga function. Within this, functions consists of the necessary operations to calculate
for the desired output. An example to this is from the past lessons wherein we have to create a complete and adjusted description of an area. It might seem 
much of a big deal at first considering that there are multiple conditions at play, however within further "separating" them, breaking them into smaller sections.
it destroys the illusion that it is impossible. Little by little, piece by piece, one wouldn't even notice that it is already finished!

Give an example of a task related to geomatics that is done manually and can be optimized using programming. What would be your plan-of-attack for this solution?
Programming has always made computations easier not only in the field of geomatics but also in every field imaginable. It is basically a premium 
calculator that can solve anything imaginable with under a few modifications. Usually, most students take time in calculating individual
raw data from the descriptions for a parcel of land. With programming, calculating for area of the subparcels will be made easy. Firstly, 
input all the required values; this is usually the bearings and the distances of the lines of the polygon.
After that there would be a choice whether to divide the parcel in terms of its direction, etc. 
firstly, the adjusted lat and dep as well as the bearings of each line is determined through the simple calculations to be coded. Then, a trial 
line should then be generated as a midpoint from two known points. Another thing is a closing line which is the line that cuts the polygon into half   The expected output of that are the distance and bearings
The descriptions created by the two lines is then determined, With that added, the areas of the halfed area can be determined through the dpd dma method.

"""