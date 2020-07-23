import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
# db_user = os.environ.get("DB_USER")
# db_password = os.environ.get("DB_PASS")


app.config["MONGO_DBNAME"] = "DictionaryDB"
app.config["MONGO_URI"] = "mongodb+srv://stanciudorin:conect86@myfirstcluster.awi3j.mongodb.net/DictionaryDB?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
@app.route("/show_words")
def show_words():
    return render_template("words.html", words=mongo.db.words.find())


@app.route("/add_word")
def add_word():
    return render_template("addword.html", categories=mongo.db.categories.find())


@app.route("/insert_word", methods=["POST"])
def insert_word():
    words = mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for("show_words"))


@app.route("/categories")
def categories():
    return render_template("categories.htm", words=mongo.db.categories.find())


@app.route("/edit_words/<word_id>")
def edit_words(word_id):
    the_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editword.html", word=the_word, categories=all_categories) 


@app.route("/update_word/<word_id>", methods=["POST"])
def update_word(word_id):
    words = mongo.db.words
    words.update({"_id": ObjectId(word_id)},
        {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word"),
            "description": request.form.get("description"),
        })
    return redirect(url_for("show_words"))


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    mongo.db.word.remove({"_id": ObjectId(word_id)})
    return redirect(url_for("show_words"))


@app.route("/get_categories")
def get_categories():
    return render_template("categories.html",
    categories=mongo.db.categories.find())


@app.route("/edit_category/<category_id>")
def edit_category(category_id):
    return render_template("editcategory.html",
    category=mongo.db.categories.find_one({"_id": ObjectId(category_id)}))


@app.route("/update_category/<category_id>", methods=["POST"])
def update_category(category_id):
    mongo.db.categories.update(
        {"_id": ObjectId(category_id)},
        {"category_name": request.form.get("category_name")})
    return redirect(url_for("get_categories"))


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
