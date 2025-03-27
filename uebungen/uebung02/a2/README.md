# Task02
O(f(n)): wächst höchstens wie f(n) -> obere Grenze

Ω(f(n)): wächst mindestens wie f(n) -> untere Grenze

Θ(f(n)): wächst genau wie f(n) -> obere & untere Grenze gleichzeitig

## 17 + 22 + 45 = O(1)
Ja: 17+22+45=84 sprich konstant (kein n), daher O(1).

## 5n³ + 12n² + 3n + 5 = Ω(n³)
Ja: n³ ist der höchste n wert, da omega heißt wächst mindestens so schnell wie das n³ passt es.

## 2ⁿ⁺¹ = O(2ⁿ)
Nein: 2ⁿ⁺¹ ist 2·2ⁿ sprich 2 mal so groß wie 2ⁿ und daher passt es nicht in die oberschranke Groß O.

## 2²ⁿ = O(2ⁿ)
Nein: 2²ⁿ ist (2ⁿ)² und wird so viel schneller größer als 2ⁿ. 
bei n = 10: 2ⁿ = 1024 aber 2²ⁿ = 2^1024 ist viel viel größer.

## log(n!) = Θ(n log n)
Ja: Siehe Stirling-Formel: log(n!) ≈ n log n -n

log(n!) ~ log(wrz[2 pi n] * [n/e]^n)

log(n!) ~ log(wrz[2 pi n]) + log([n/e]^n)

log(n!) ~ 1/2*log(2 pi n) + n*log(n) - n*log(e)

log(n!) ~ 1/2log(2 pi n) + n log (n) - n

Was wichtig: (egal) . . . .  (wichtig)

## 2ⁿ = O(n!)
Ja: n! wächst schneller viel schneller als 2ⁿ und daher passt 2ⁿ in die Obergrenze groß O.  

## n! = O(nⁿ)
Ja: n! wird langsamer größer als nⁿ also passt es in die Obergrenze groß O

## 6⁻⁵ · n¹·²⁵ = Θ(√n)
Nein: n¹·²⁵ wächst natürlich schneller als n⁰·⁵