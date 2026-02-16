class HaircutAIAgent:
    def __init__(self, hair_length):
        self.hair_length = hair_length

    def recommend_haircut(self):
        if self.hair_length < 5:
            return "You should try a short haircut!"
        elif 5 <= self.hair_length <= 15:
            return "A medium-length hairstyle would look great on you."
        else:
            return "Consider going for a long hairstyle!"