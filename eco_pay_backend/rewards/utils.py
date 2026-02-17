
def calculate_rewards(user, amount):
    earned_points = int(amount // 1000)
    user.points += earned_points

    if user.points >= 10:
        tokens = user.points // 10
        user.crypto_tokens += tokens
        user.points = user.points % 10

    user.save()
