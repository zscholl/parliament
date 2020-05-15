import json
import yaml

class Finding:
    """ Class for storing findings """

    issue = ""
    detail = ""
    location = {}
    severity = ""
    title = ""
    description = ""
    ignore_locations = {}

    def __init__(self, issue, detail, location):
        self.issue = issue
        self.detail = detail
        self.location = location

    def __repr__(self):
        """ Return a string for printing """
        return "{} - {} - {}".format(self.issue, self.detail, self.location)
    
    def __hash__(self):
        return hash((self.issue, self.detail, json.dumps(self.location)))
    
    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.issue == other.issue and self.detail == other.detail and self.location == other.location

    def to_json(self):
        """ Return a json representation of finding """
        return {"issue": self.issue, "title": self.title, "severity": self.severity, "description": self.description, "detail": self.detail, "location": self.location}
