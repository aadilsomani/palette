# Palette Prototype 
## Usage
* Clone or download this repository to a Windows machine
* If you do not have Python installed, use the run.bat to load Python
* Once the python shell opens, type:
  ```python
  from main import *
  ```
## Commands
* newAccount()
  * newAccount() takes three values
    * Username, Email and Password
  *The folder will include a *userData.json* file, which includes data such as posts, followers and following along with a folder for their posts
  
  Example:
  ```python
  newAccount("johndoe","johndoe@gmail.com","Johnny123")
  ```
* post()
  * post() takes three values
    * Username, Image Path and Caption
  * A folder named by the timestamp of the post will be created under the subdirectory of the user who is posting
  * The folder will include a *postDetails.json* file, which include analytical data such as likes and comments as well as its **unique ID**
  
  Example:
  ```python
  post("johndoe","C:/Images/Image.jpg","Check out this awesome image!!!! #Epic")
  ```
* increaseFollowing() and increaseFollowers
  * Each take two values
    * User (Main user being interacted with)
    * Follower/Person to be followed
    
  * This command will **update** the *userData.json* file with the new follower/followed account 
  * It will also record a follower count and update it accordingly
  
  Example:
  ```python
  increaseFollowing("johndoe","janedoe")
  ```
  This would in return increase *johndoe*'s by 1 and record who is being followed (*janedoe*) in *johndoe*'s *userData.json* file (found in **postDetails.json**)
  
* like()
  * like() takes three values
    * Username of poster, User liking the post and the post's **unique ID**
  * The function will iterate through the posts, find the correct post that is being liked amd accordingly modify its **postDetails.json** 
  file with the account that liked the post along with the post count
  
  Example:
  ```python
  like("johndoe","janedoe","fd06ac3b-da83-11ea-9a83-803253a6a5b8")
  ```
* comment()
  * comment() takes four values
    * Username of poster, Commenter, Body of Comment and the post's **unique ID** 
    * Works in a similar way to like, except the comment body itself is also recorded inthe **postDetails.json** file
    * The function will also update the total amount of comments in the same file
    
  Example:
  ```python
  comment("johndoe","janedoe","Awesome picture dude! This picture really relaxes me! Is it gonna go on sale one day?", "fd06ac3b-da83-11ea-9a83-803253a6a5b8")
  ```
