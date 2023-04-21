from flask import Blueprint, jsonify 

class Planet:
    def __init__(self, id, name, description, moons, color):
        self.id = id
        self.name = name
        self.description = description
        self.moons = moons
        self.color = color

planet1 = Planet(1, "Mercury", "Mercury is hot", 0, "gray")
planet2 = Planet(2, "Venus", "No moons here", 0, "yellow")
planet3 = Planet(3, "Earth", "Life is good here", 1, "blue-green")

planet_list = [planet1, planet2, planet3]

planet_bp = Blueprint("planet", __name__, url_prefix="/planet")

@planet_bp.route("", methods=["GET"])
def get_planets():
    response = []
    for planet in planet_list:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "moons": planet.moons,
            "color": planet.color
        }
        response.append(planet_dict)

    return jsonify(response), 200 

@planet_bp.route("/<id>", methods=["GET"])
def get_one_planet(id):
    try:
        planet_id = int(id)
    except ValueError:
        return {"message": f"Invalid id: {id}"}, 400
    
    for planet in planet_list:
        if planet.id == planet_id:
            return jsonify({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "moons": planet.moons,
                "color": planet.color
            }), 200
    return {"message": f"id {planet_id} not found"}, 404
        