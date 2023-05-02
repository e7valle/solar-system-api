from flask import abort, Blueprint, jsonify, request, make_response
from app import db
from app.models.solar_system import Planet


planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"], 
        moons = request_body["moons"],
        color = request_body["color"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    name_query = request.args.get("name")

    if name_query is None:
        all_planets  = Planet.query.all()
    else:
        all_planets = Planet.query.filter_by(name=name_query)

    for planet in all_planets:
        response.append(planet.to_dict())

    return jsonify(response), 200 

@planet_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict(), 200

@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_data = request.get_json()

    planet.name = request_data["name"]
    planet.description = request_data["description"]
    planet.moons = request_data["moons"]
    planet.color = request_data["color"]

    db.session.commit()

    return {"msg": f"planet {planet_id} successfully updated"}, 200

@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return {"msg": f"planet {planet_id} successfully deleted"}, 200

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        return abort(make_response({"message": f"invalid id: {planet_id}"}, 400))
    
    return Planet.query.get_or_404(planet_id)