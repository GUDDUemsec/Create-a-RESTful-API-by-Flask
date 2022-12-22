from flask import Flask, request, jsonify,render_template

app = Flask(__name__)
 
  
@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/test/<int:id>')
def show_blog(id):
   return f'test Number: {id}'
  
# TEMPLATES

@app.route("/index")
def manni():
    name = "rohan das"
    return render_template('index.html', name2 = name)
  
# Create a RESTful API 

@app.route('/post', methods=["POST","GET"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['query']}
     return jsonify(dictToReturn)


data={
 "Savala Nolan": {"_id": {
    "$oid": "63a070ee70fab6bb07cf5150"
  },
  "index": 0,
  "Titles": "Please Consider the Racial Impact of Your Halloween Decor",
  "Authors": "Savala Nolan",
  "Dates": "Oct 17",
  "Links": "https://momentum.medium.com/i-beg-you-consider-your-halloween-decor-carefully-dd6b722250b3?source=home---------127------------------0----------",
  "Contents": "Oh, it’s that time of year again! So here is a PSA to remind you that when your Halloween decorations include hanging fake bodies from trees, please consider the extent to which they look like the scene of a lynching and how that might impact Black and brown families in your neighborhood. I see some of these “hanging figures” every year. Some I’d call benign — like what is clearly a little ghost or bat or monster.But some are downright disturbing. These disturbing ones are often lifelike in size and detail, hung by an actual noose or rope, and with the look of bloody dismemberment and decay about them. I suppose they are meant to simply look ghoulish and spooky; but they strongly mirror the aftermath of a lynching, in which the victim’s body was often mutilated, left hanging and exposed to the elements, in public, for days or weeks.For many Black and brown people, that image of a mauled body/half-body hanging from a rope on a tree is instantly recognizable and deeply, deeply disturbing. I’ve never witnessed a lynching, but I am the direct descendant of lynched people, and I have Black elders in my family who, as children, either witnessed or were constantly living under the threat and specter of lynchings. (If a history lesson is helpful, consider, as I have written elsewhere, that the thousands of known lynchings in this country “were so thoroughly conceived as public spectacle that many were advertised in newspapers, and many culminated with photographs of the crowd below the corpse, crowds of dozens, hundreds, and up tens of thousands of people. Entrepreneurial spectators turned lynching photographs into postcards or prints, and the postcards were mailed to friends and family who could not make the live event. From beginning to end, lynchings functioned as powerful visual aids, teaching people of all races how the racial hierarchy worked, and showing them the cost of transgressing — or merely being suspected of transgressing — the color line.” You can read the entirety of that article here, and learn far more about lynching in an extraordinary report here.)So: If you’ve got one of these body-hanging-from-a-tree decorations up in your yard, please consider swapping it out for something that doesn’t rhyme with images of racialized terrorism, death and suffering.To be clear, I assume these decorations appear because of lack of historical knowledge and/or consideration, not because of malice. If it’s about malice, well, that’s a whole ’nother story and, frankly, you’re not who I’m talking to. I’m talking to — dare I say with? — people like many of my own family members: white people who mean well but are (still) cloaked in a relatively thick, protective layer of what I call “racial fog” that prevents them from seeing clearly how their actions or inactions impact those “below them” in the racial hierarchy.Every year, I end up writing a short-and-sweet version of this note to neighbors. Taking one for the team, you might call it. I always leave my phone number in case they want to talk. I generally sign it in community.And you know what? In every instance so far, a minor miracle has occurred: the decoration comes down and doesn’t return. True, I can’t know why the decoration came down. There could have been a lot of eye-rolling. There could have been a disagreement at that dinner table about the appropriate response to my little note. And if that’s the case, so be it. While I care about reaching people’s hearts, in this instance, I care more about the safety and comfort of my own family, from my child to my godfather to myself, while we walk the neighborhood to celebrate the season. I center us, and our right to a peaceful existence, because lest anyone forget, we live here, too. We live here too, with you, as we always have."
}
}

# @app.get('/datas')
def list_of_data():
   return {"datas":list(data.values())}

@app.route('/datas/<data_name>')
def get_data(data_name):
   return data[data_name] 

def create_data(new_data):
   data_name = new_data['Authors']
   data[data_name] = new_data
   return new_data   

@app.route('/datas', methods=['GET', 'POST'])
def datas_route():
   if request.method == 'GET':
       return list_of_data()
   elif request.method == "POST":
       return create_data(request.get_json(force=True)) 

def delete_data(data_name_for_delete):
   deleting_data = data[data_name_for_delete]
   del data[data_name_for_delete]
   return deleting_data

@app.route('/datas/<data_name>', methods=['GET', 'PUT', 'DELETE'])
def data_route(data_name):
   if request.method == 'GET':
       return get_data(data_name)
   elif request.method == "DELETE":
       return delete_data(data_name)
if __name__=='__main__':
    app.run(debug=True,host='localhost', port=81)