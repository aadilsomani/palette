import os
import shutil
from datetime import datetime
import json
import uuid

def newAccount(username,email,password):
    newUser={
    "username": username,
    "posts": 0,
    "email": email,
    "password":password,
    "followers": {},
    "followercount": 0,
    "following": {},
    "followingcount": 0

}
    folderpath = os.path.join("users", username)
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        with open("./users/" + username + "/userData.json", 'w+', encoding='utf-8') as f:
            json.dump(newUser, f, ensure_ascii=False, indent=4)
    else:
        print("Username is taken!")

def post(username, imagepath, caption):

    timenow = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    directory = "./users/" + username + "/posts/"+str(timenow)
    #Increases the post count
    with open("./users/" +username +"/userData.json",'r',encoding="utf8") as f:
        dataDictionary=json.loads(f.read())
        dataDictionary["posts"]+=1
    with open("./users/" + username + "/userData.json", 'w', encoding="utf8") as f:
        json.dump(dataDictionary, f, ensure_ascii=False, indent=4)
    folderpath = os.path.join("users",str(username),"posts", str(timenow))
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
    shutil.copy(imagepath, folderpath)
    postDetails = {
        "caption":caption,
        "timestamp":str(timenow),
        "likes":{},
        "comments":{},
        "id":str(uuid.uuid1())
    }
    jsonDir= directory+"/postDetails.json"
    with open(jsonDir, 'w+', encoding='utf-8') as f:
        json.dump(postDetails, f, ensure_ascii=False, indent=4)

def increaseFollowing(user,follower):

    with open("./users/" +user +"/userData.json",'r',encoding="utf8") as f:
        dataDictionary=json.loads(f.read())
        following = False
        for x in dataDictionary["following"]:
            try:
                currentFollowing = ([dataDictionary['following'][follower]])
            except:
                currentFollowing=""
            if "['" + follower + "']" == str(currentFollowing):
                print("User already follows!")
                following = True
        if following == False:
            dataDictionary["followingcount"]+=1
            dataDictionary["following"][follower] = follower
            with open("./users/" + user + "/userData.json", 'w', encoding="utf8") as f:
                json.dump(dataDictionary, f, ensure_ascii=False, indent=4)


def increaseFollower(user,follower):

    with open("./users/" +user +"/userData.json",'r',encoding="utf8") as f:
        dataDictionary=json.loads(f.read())
        following = False
        for x in dataDictionary["followers"]:
            try:
                currentFollower=([dataDictionary['followers'][follower]])
            except:
                currentFollower=""
            if "['"+follower+"']" == str(currentFollower):
                print("User already follows!")
                following=True
        if following==False:
            dataDictionary["followercount"]+=1
            dataDictionary["followers"][follower] = follower
            with open("./users/" + user + "/userData.json", 'w', encoding="utf8") as f:
                json.dump(dataDictionary, f, ensure_ascii=False, indent=4)

def like(user, liker, postid):

    for post in os.listdir("./users/" + user + "/posts/"):
        with open("./users/" + user + "/posts/" + post +"/postDetails.json","r", encoding="utf8") as f:
            dataDictionary=json.loads(f.read())
            try:
                if dataDictionary["id"] == str(postid):
                    f.close()
                    dataDictionary["likes"][liker]=liker
                    dataDictionary["likecount"]=(len(dataDictionary['likes']))
                    with open("./users/" + user + "/posts/" + post +"/postDetails.json", 'w', encoding="utf8") as a:
                        json.dump(dataDictionary, a, ensure_ascii=False, indent=4)
            except KeyError:
                continue

def comment(user, commenter, comment, postid):

    for post in os.listdir("./users/" + user + "/posts/"):
        with open("./users/" + user + "/posts/" + post +"/postDetails.json","r", encoding="utf8") as f:
            dataDictionary=json.loads(f.read())
            try:
                if dataDictionary["id"] == str(postid):
                    f.close()
                    dataDictionary["comments"][commenter]=comment
                    dataDictionary["commentcount"]=(len(dataDictionary['comments']))
                    with open("./users/" + user + "/posts/" + post +"/postDetails.json", 'w', encoding="utf8") as a:
                        json.dump(dataDictionary, a, ensure_ascii=False, indent=4)
            except KeyError:
                continue