
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

  
        self._members = []

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member['last_name'] = self.last_name
  
        if 'id' not in member:
            member['id'] = self._generateId()

        self._members.append(member)

    def delete_member(self, id):
     
        miembro = self.get_member(id)
        if miembro: 
            self._members.remove(miembro)
            return miembro

    def get_member(self, id):

        for miembro in self._members:
            if miembro['id'] == id:
                return miembro   


    def get_all_members(self):
        return self._members