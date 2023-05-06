from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    moons = db.Column(db.Integer)
    color = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "moons": self.moons,
            "color": self.color
        }



    @classmethod
    # youre creating yourself and returning yourself
    # I'm putting all the data into the constructor.....

    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"],
            description = planet_data["description"],
            moons = planet_data["moons"],
            color = planet_data["color"] 
        )
    
    # planets = Planets.from_dict(planet_data)
    # vs 
    # planets_obj = Planets()
    # planets = planets_obj.from_dict(planet_data)