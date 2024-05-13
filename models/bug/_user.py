from dataclasses import dataclass


@dataclass
class User:
    self: str
    name: str
    key: str
    avatarUrls: dict
    displayName: str
    active: bool
    timeZone: str

    def to_dict(self):
        return {
            "self": self.self,
            "name": self.name,
            "key": self.key,
            "avatarUrls": self.avatarUrls,
            "displayName": self.displayName,
            "active": self.active,
            "timeZone": self.timeZone
        }
