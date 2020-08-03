import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
import env as config

# Creating an instance of app and store it in the app variable
app = Flask(__name__)


app.config["MONGO_DBNAME"] = "DictionaryDB"
app.config["MONGO_URI"] = "mongodb+srv://stanciudorin:conect86@myfirstcluster.awi3j.mongodb.net/DictionaryDB?retryWrites=true&w=majority"

# Creating an instance of PyMongo
mongo = PyMongo(app)


# Displaying the list of categories and their words
@app.route("/")
@app.route("/show_words")
def show_words():
    words = list(mongo.db.words.find())
    return render_template("words.html", words=mongo.db.words.find()) # Returns everything in our words collection


@app.route("/edit")
def edit():
    return render_template("edit.html", words=mongo.db.words.find()) # Returns everything in our words collection
    

# Display the interface for when we are adding a word (display the addword page)
@app.route("/add_word")
def add_word():
    return render_template("addword.html", categories=mongo.db.categories.find()) #find function to fetch the categories


# Function to add words into our dictionary
@app.route("/insert_word", methods=["POST"])
def insert_word():
    words = mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for("show_words"))


# Displaying the interface of editing a word, display the page in an editable form
@app.route("/edit_words/<word_id>")
def edit_words(word_id):
    the_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editword.html", word=the_word, categories=all_categories) 


# Creating the function to update an existing word
@app.route("/update_word/<word_id>", methods=["POST"])
def update_word(word_id):
    words = mongo.db.words
    words.update_one({"_id": ObjectId(word_id)},
        {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word"),
            "description": request.form.get("description"),
        })

    return redirect(url_for("show_words"))


# Function to delete a word from our database and dictionary UX
@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    mongo.db.words.remove({"_id": ObjectId(word_id)})
    return redirect(url_for("edit"))


# Displaying the Categories list
@app.route("/get_categories")
def get_categories():
    return render_template("categories.html", categories=mongo.db.categories.find())


# Displaying the editable interface
@app.route("/edit_category/<category_id>")
def edit_category(category_id):
    return render_template("editcategory.html",
    category=mongo.db.categories.find_one({"_id": ObjectId(category_id)}))


# Function to update the category
@app.route("/update_category/<category_id>", methods=["POST"])
def update_category(category_id):
    mongo.db.categories.update(
        {"_id": ObjectId(category_id)},
        {"category_name": request.form.get("category_name")})
    return redirect(url_for("get_categories"))


# Delete a category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
