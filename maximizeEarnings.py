def maximize_earnings(earnings, k):
    n = len(earnings)
    dp = [0] * (n + 1)  # dp[i] representa la máxima ganancia hasta el día i-1

    # Iteramos desde el primer día hasta el último
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]  # Caso base: no trabajar el día i-1
        total = 0

        # Probamos todas las posibilidades de trabajar j días seguidos antes del día i
        for j in range(1, min(k, i) + 1):
            total += earnings[i - j]  # Ganancia total trabajando j días hasta el día i-1
            # Para trabajar j días, el último día trabajado sería i-j. Antes de eso, debe haber un día de descanso (i-j-1)
            descanso_previo = dp[i - j - 1] if i - j - 1 >= 0 else 0
            dp[i] = max(dp[i], total + descanso_previo)  # Elegimos el mejor resultado entre descansar o trabajar j días

    return dp[n]

print(maximize_earnings([1000, 2000, 3000, 4000, 5000], 3))