from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import Serializer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
import os
from dotenv import load_dotenv


app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class SerializerMixin:
    def to_dict(self, include_relationships=False, skip_none=False):
        result = {}
        from datetime import date, datetime
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, (datetime, date)):
                value = value.isoformat()
            if skip_none and value is None:
                continue
            result[column.name] = value

        if include_relationships:
            for rel in self.__mapper__.relationships:
                related_obj = getattr(self, rel.key)
                if related_obj is not None:
                    if isinstance(related_obj, list):
                        result[rel.key] = [obj.to_dict() for obj in related_obj]
                    else:
                        result[rel.key] = related_obj.to_dict()

        return result


# Cafe TABLE Configuration
class Cafe(db.Model, SerializerMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")



## But GET is allowed by default on all routes.
# So this is much simpler:
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(all_cafes=[all_cafes.to_dict() for all_cafes in all_cafes])

@app.route("/search")
def search():
    search_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == search_location))
    all_cafes = result.scalars().all()
    if all_cafes:
        return jsonify(all_cafes=[all_cafes.to_dict() for all_cafes in all_cafes])
    else:
        return jsonify(error= {"error": "No cafes found"}), 404


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_toilet=bool(request.form.get("has_toilet")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the cafe."})
    else:
        return jsonify(error={"Not Found": "No cafe found with that ID"}), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def remove_cafe(cafe_id):
    api_key = request.args.get("api_key") or request.headers.get("X-API_KEY")
    if api_key == API_KEY:
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully removed the cafe."})
        else: return jsonify(error={"Not Found": "No cafe found with that ID"}), 404

    else:
        return jsonify(error={"Not Found": "No API key found"}), 404





if __name__ == '__main__':
    app.run(debug=True)
