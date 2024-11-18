import math 


sifting_coefficiant = 0.5
p_estimation = 0.25
kr_efficiency = 1.22
qber = 3.8756673881673906 / 100
raw_keyrate = 451.26191626912447

ab_entropy = -qber*math.log2(qber)-(1-qber)*math.log2(1-qber)
ae_entropy = 1-ab_entropy

final_keyrate = raw_keyrate*sifting_coefficiant*p_estimation*(ae_entropy-kr_efficiency*ab_entropy)

print(final_keyrate)