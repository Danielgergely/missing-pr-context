from models.bug import Votes


class VotesMapper:

    @staticmethod
    def dict_to_model(_dict: dict) -> Votes:
        return Votes(self=_dict.get("self"),
                     votes=_dict.get("votes"),
                     hasVoted=_dict.get("hasVoted"))
