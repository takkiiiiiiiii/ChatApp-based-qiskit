import matplotlib.pyplot as plt

# データのリスト
data = [25.503968253968253, 25.992063492063494, 22.023809523809522, 23.214285714285715, 26.785714285714285, 23.41269841269841, 25.396825396825395, 25.892857142857146, 24.206349206349206, 25.198412698412696, 25.198412698412696, 26.984126984126984, 25.694444444444443, 23.61111111111111, 23.41269841269841, 23.41269841269841, 25.396825396825395, 25.992063492063494, 25.793650793650798, 27.976190476190478, 26.686507936507937, 25.0, 23.115079365079367, 24.801587301587304, 25.595238095238095, 24.305555555555554, 25.892857142857146, 23.41269841269841, 26.091269841269842, 26.58730158730159, 24.00793650793651, 26.58730158730159, 25.297619047619047, 25.198412698412696, 25.0, 25.396825396825395, 23.41269841269841, 25.694444444444443, 25.992063492063494, 23.809523809523807, 25.496031746031743, 23.809523809523807, 25.297619047619047, 22.817460317460316, 26.884920634920633, 24.702380952380953, 24.900793650793652, 25.694444444444443, 25.396825396825395, 25.61111111111111, 24.107142857142858, 23.809523809523807, 25.892857142857146, 23.908730158730158, 25.198412698412696, 26.488095238095237, 27.083333333333332, 26.900793650793652, 24.801587301587304, 25.892857142857146, 24.00793650793651, 23.511904761904763, 26.488095238095237, 25.0, 26.884920634920633, 26.091269841269842, 25.297619047619047, 23.214285714285715, 24.6031746031746, 22.61904761904762, 25.992063492063494, 26.190476190476193, 25.694444444444443, 24.305555555555554, 25.595238095238095, 26.884920634920633, 25.0, 24.900793650793652, 27.380952380952383, 24.503968253968253, 25.198412698412696, 24.702380952380953, 24.900793650793652, 27.876984126984127, 22.817460317460316, 26.686507936507937, 23.908730158730158, 23.511904761904763, 26.686507936507937, 25.099206349206348, 25.099206349206348, 24.801587301587304, 23.015873015873016, 24.6031746031746, 23.71031746031746, 23.908730158730158, 26.091269841269842, 24.404761904761905, 25.892857142857146, 23.214285714285715, 24.702380952380953, 24.6031746031746, 22.22222222222222, 26.58730158730159, 24.404761904761905, 25.892857142857146, 25.892857142857146, 26.488095238095237, 24.107142857142858, 25.297619047619047, 24.206349206349206, 25.496031746031743, 25.694444444444443, 24.503968253968253, 24.305555555555554, 23.908730158730158, 23.313492063492063, 24.00793650793651, 27.579365079365083, 25.198412698412696, 24.900793650793652, 26.488095238095237, 24.6031746031746, 24.404761904761905, 24.503968253968253, 25.297619047619047, 27.083333333333332, 24.702380952380953, 25.297619047619047, 25.0, 25.0, 25.992063492063494, 25.198412698412696, 27.281746031746028, 25.099206349206348, 26.38888888888889, 24.503968253968253, 24.107142857142858, 24.107142857142858, 24.900793650793652, 25.595238095238095, 25.396825396825395, 27.48015873015873, 25.496031746031743, 25.511904761904763, 24.00793650793651, 22.916666666666664, 24.503968253968253, 24.900793650793652, 25.396825396825395, 27.305555555555554, 26.28968253968254, 25.793650793650798, 26.488095238095237, 26.091269841269842, 25.992063492063494, 24.00793650793651, 25.694444444444443, 26.686507936507937, 25.6031746031746, 25.198412698412696, 25.198412698412696, 27.18253968253968, 25.0, 25.496031746031743, 23.015873015873016, 27.18253968253968, 25.694444444444443, 26.190476190476193, 25.908730158730158, 26.785714285714285, 24.6031746031746, 23.313492063492063, 26.091269841269842, 26.488095238095237, 25.496031746031743, 24.503968253968253, 25.396825396825395, 26.206349206349206, 26.28968253968254, 26.190476190476193, 23.41269841269841, 25.297619047619047, 25.297619047619047, 25.396825396825395, 26.488095238095237, 23.511904761904763, 25.503968253968253, 25.099206349206348, 24.801587301587304, 26.190476190476193, 25.396825396825395, 25.396825396825395, 24.6031746031746, 25.496031746031743, 27.281746031746028, 24.503968253968253, 27.976190476190478, 26.091269841269842, 26.190476190476193, 23.41269841269841, 25.099206349206348, 23.61111111111111, 25.892857142857146, 25.71031746031746, 26.6031746031746, 24.801587301587304, 23.115079365079367, 25.496031746031743, 24.900793650793652, 23.115079365079367, 25.496031746031743, 26.38888888888889, 23.71031746031746, 25.992063492063494, 25.0, 25.396825396825395, 22.916666666666664, 24.702380952380953, 26.984126984126984, 26.28968253968254, 25.0, 24.702380952380953, 23.313492063492063, 25.793650793650798, 24.107142857142858, 26.686507936507937, 24.503968253968253, 23.313492063492063, 26.190476190476193, 25.198412698412696, 24.900793650793652, 26.28968253968254, 25.099206349206348, 25.595238095238095, 25.595238095238095, 23.115079365079367, 24.6031746031746, 26.190476190476193, 25.396825396825395, 23.41269841269841, 24.503968253968253, 25.809523809523807, 25.992063492063494, 25.793650793650798, 25.198412698412696, 24.107142857142858, 23.41269841269841, 23.908730158730158, 24.107142857142858, 25.793650793650798, 24.00793650793651, 24.206349206349206, 26.884920634920633, 25.496031746031743, 23.015873015873016, 25.694444444444443, 22.61904761904762, 23.809523809523807, 24.404761904761905, 24.206349206349206, 25.297619047619047, 24.702380952380953, 25.595238095238095, 26.190476190476193, 23.41269841269841, 26.58730158730159, 24.900793650793652, 24.404761904761905, 25.992063492063494, 24.00793650793651, 25.396825396825395, 23.809523809523807, 25.0, 26.984126984126984, 24.900793650793652, 26.686507936507937, 23.809523809523807, 25.793650793650798, 25.099206349206348, 25.793650793650798, 25.0, 24.00793650793651, 25.099206349206348, 27.18253968253968, 25.496031746031743, 25.892857142857146, 24.900793650793652, 25.892857142857146, 27.579365079365083, 24.305555555555554, 24.801587301587304, 25.595238095238095, 25.297619047619047, 24.503968253968253, 26.58730158730159, 25.694444444444443, 25.595238095238095, 23.511904761904763, 26.785714285714285, 25.099206349206348, 24.00793650793651, 26.58730158730159, 25.496031746031743, 26.091269841269842, 22.71825396825397, 25.992063492063494, 25.198412698412696, 24.206349206349206, 24.404761904761905, 25.0, 24.503968253968253, 25.892857142857146, 26.190476190476193, 24.00793650793651, 27.876984126984127, 25.099206349206348, 24.503968253968253, 26.686507936507937, 27.18253968253968, 25.099206349206348, 25.992063492063494, 24.206349206349206, 23.908730158730158, 27.18253968253968, 26.801587301587304, 26.190476190476193, 24.801587301587304, 26.28968253968254, 25.099206349206348, 23.61111111111111, 24.206349206349206, 25.496031746031743, 25.793650793650798, 25.198412698412696, 26.190476190476193, 24.00793650793651, 25.396825396825395, 25.198412698412696, 26.785714285714285, 24.702380952380953, 25.694444444444443, 28.273809523809522, 25.396825396825395, 26.6031746031746, 22.71825396825397, 25.099206349206348, 24.801587301587304, 25.0, 25.892857142857146, 26.58730158730159, 23.908730158730158, 24.404761904761905, 26.190476190476193, 25.305555555555554, 24.503968253968253, 25.496031746031743, 25.694444444444443, 25.694444444444443, 25.694444444444443, 24.801587301587304, 25.198412698412696, 25.297619047619047, 26.785714285714285, 27.18253968253968, 25.099206349206348, 25.793650793650798, 26.091269841269842, 26.984126984126984, 24.6031746031746, 26.58730158730159, 25.198412698412696, 25.694444444444443, 25.099206349206348, 26.190476190476193, 23.41269841269841, 25.694444444444443, 24.6031746031746, 23.61111111111111, 25.099206349206348, 24.404761904761905, 24.404761904761905, 23.511904761904763, 24.305555555555554, 27.380952380952383, 23.61111111111111, 24.702380952380953, 22.817460317460316, 26.38888888888889, 24.00793650793651, 23.511904761904763, 25.396825396825395, 26.28968253968254, 25.099206349206348, 24.305555555555554, 23.511904761904763, 24.6031746031746, 26.091269841269842, 25.099206349206348, 25.793650793650798, 25.099206349206348, 23.115079365079367, 23.908730158730158, 26.686507936507937, 25.297619047619047, 24.503968253968253, 26.686507936507937, 24.801587301587304, 25.297619047619047, 25.496031746031743, 24.702380952380953, 23.511904761904763, 26.190476190476193, 25.694444444444443, 26.984126984126984, 24.503968253968253, 23.41269841269841, 25.099206349206348, 24.503968253968253, 24.900793650793652, 23.115079365079367, 26.884920634920633, 24.900793650793652, 27.083333333333332, 24.305555555555554, 25.694444444444443, 25.099206349206348, 25.892857142857146, 24.305555555555554, 26.38888888888889, 26.28968253968254, 25.396825396825395, 23.61111111111111, 25.992063492063494, 23.214285714285715, 25.793650793650798, 25.396825396825395, 22.123015873015873, 25.793650793650798, 23.809523809523807, 24.702380952380953, 24.900793650793652, 26.091269841269842, 24.702380952380953, 25.099206349206348, 24.00793650793651, 24.00793650793651, 24.6031746031746, 26.488095238095237, 25.496031746031743, 24.900793650793652, 25.793650793650798, 26.38888888888889, 24.702380952380953, 24.801587301587304, 25.396825396825395, 26.785714285714285, 25.694444444444443, 24.6031746031746, 22.61904761904762, 23.511904761904763, 23.809523809523807, 26.28968253968254, 24.503968253968253, 24.6031746031746, 25.793650793650798, 24.503968253968253, 26.58730158730159, 25.595238095238095, 23.71031746031746, 23.313492063492063, 24.702380952380953, 24.503968253968253, 26.190476190476193, 25.793650793650798, 25.0, 25.0, 24.305555555555554, 25.0, 24.801587301587304, 26.38888888888889, 23.214285714285715, 24.702380952380953, 26.091269841269842, 25.099206349206348, 25.099206349206348, 24.900793650793652, 25.496031746031743, 25.793650793650798, 24.801587301587304, 25.396825396825395, 25.198412698412696, 23.115079365079367, 24.900793650793652, 25.099206349206348, 25.595238095238095, 23.214285714285715, 24.900793650793652, 24.900793650793652, 25.992063492063494, 25.694444444444443, 25.496031746031743, 25.297619047619047, 24.107142857142858, 24.6031746031746, 23.015873015873016, 25.595238095238095, 24.305555555555554, 24.801587301587304, 27.380952380952383, 24.305555555555554, 24.305555555555554, 27.18253968253968, 22.71825396825397, 23.908730158730158, 26.28968253968254, 25.694444444444443, 24.404761904761905, 25.396825396825395, 27.281746031746028, 24.801587301587304, 23.214285714285715, 24.404761904761905, 24.00793650793651, 24.900793650793652, 25.0, 23.809523809523807, 25.992063492063494, 24.107142857142858, 24.404761904761905, 25.198412698412696, 24.900793650793652, 26.58730158730159, 25.793650793650798, 24.702380952380953, 23.71031746031746, 26.686507936507937, 23.41269841269841, 25.496031746031743, 25.396825396825395, 26.58730158730159, 25.496031746031743, 25.793650793650798, 25.892857142857146, 26.091269841269842, 24.503968253968253, 25.0, 24.900793650793652, 25.793650793650798, 24.206349206349206, 22.71825396825397, 26.785714285714285, 26.58730158730159, 26.091269841269842, 26.884920634920633, 26.785714285714285, 24.6031746031746, 24.404761904761905, 25.214285714285715, 26.28968253968254, 24.107142857142858, 23.313492063492063, 25.198412698412696, 25.297619047619047, 24.702380952380953, 25.396825396825395, 26.817460317460316, 26.404761904761905, 25.694444444444443, 25.198412698412696, 24.404761904761905, 23.61111111111111, 26.091269841269842, 25.297619047619047, 25.892857142857146, 26.091269841269842, 26.488095238095237, 26.091269841269842, 25.595238095238095, 26.884920634920633, 24.801587301587304, 23.61111111111111, 23.313492063492063, 25.198412698412696, 23.809523809523807, 25.496031746031743, 24.900793650793652, 24.6031746031746, 25.198412698412696, 23.61111111111111, 25.892857142857146, 24.702380952380953, 24.900793650793652, 24.107142857142858, 25.702380952380953, 25.595238095238095, 24.801587301587304, 24.00793650793651, 25.0, 26.884920634920633, 22.916666666666664, 25.198412698412696, 24.801587301587304, 26.58730158730159, 26.190476190476193, 24.00793650793651, 23.71031746031746, 26.785714285714285, 24.404761904761905, 26.488095238095237, 24.206349206349206, 25.892857142857146, 24.702380952380953, 24.900793650793652, 25.694444444444443, 26.091269841269842, 24.107142857142858, 24.00793650793651, 24.00793650793651, 27.380952380952383, 24.900793650793652, 24.305555555555554, 25.396825396825395, 25.297619047619047, 25.595238095238095, 22.916666666666664, 25.198412698412696, 26.28968253968254, 24.900793650793652, 25.396825396825395, 23.809523809523807, 24.6031746031746, 25.396825396825395, 25.496031746031743, 24.702380952380953, 24.900793650793652, 25.496031746031743, 23.41269841269841, 25.892857142857146, 24.305555555555554, 23.511904761904763, 23.61111111111111, 25.0, 27.281746031746028, 26.091269841269842, 25.992063492063494, 23.809523809523807, 25.793650793650798, 24.900793650793652, 27.380952380952383, 24.00793650793651, 26.091269841269842, 24.305555555555554, 24.6031746031746, 24.107142857142858, 24.702380952380953, 23.809523809523807, 24.305555555555554, 25.694444444444443, 24.305555555555554, 25.297619047619047, 25.595238095238095, 23.511904761904763, 22.71825396825397, 26.38888888888889, 22.817460317460316, 25.595238095238095, 23.61111111111111, 25.496031746031743, 26.190476190476193, 24.00793650793651, 25.099206349206348, 26.190476190476193, 25.496031746031743, 25.595238095238095, 25.694444444444443, 24.00793650793651, 25.297619047619047, 26.488095238095237, 25.0, 24.6031746031746, 23.313492063492063, 26.28968253968254, 25.396825396825395, 25.992063492063494, 24.702380952380953, 24.206349206349206, 24.6031746031746, 24.503968253968253, 22.817460317460316, 23.61111111111111, 24.404761904761905, 25.198412698412696, 25.099206349206348, 24.00793650793651, 24.503968253968253, 25.496031746031743, 25.198412698412696, 24.503968253968253, 24.801587301587304, 24.900793650793652, 25.892857142857146, 25.793650793650798, 25.297619047619047, 24.6031746031746, 25.0, 26.091269841269842, 25.099206349206348, 25.099206349206348, 25.793650793650798, 25.396825396825395, 24.702380952380953, 26.785714285714285, 25.198412698412696, 25.0, 25.099206349206348, 24.702380952380953, 24.00793650793651, 25.595238095238095, 25.396825396825395, 24.801587301587304, 25.892857142857146, 26.091269841269842, 26.38888888888889, 24.404761904761905, 24.702380952380953, 27.083333333333332, 24.6031746031746, 23.41269841269841, 26.091269841269842, 23.71031746031746, 23.71031746031746, 24.702380952380953, 24.206349206349206, 22.22222222222222, 24.6031746031746, 25.297619047619047, 24.503968253968253, 24.6031746031746, 25.892857142857146, 25.0, 23.71031746031746, 24.702380952380953, 25.099206349206348, 24.503968253968253, 24.305555555555554, 26.488095238095237, 25.892857142857146, 25.793650793650798, 25.892857142857146, 25.595238095238095, 24.900793650793652, 26.190476190476193, 25.396825396825395, 24.00793650793651, 25.198412698412696, 25.198412698412696, 24.6031746031746, 23.908730158730158, 23.908730158730158, 24.107142857142858, 24.305555555555554, 25.496031746031743, 24.801587301587304, 24.702380952380953, 26.686507936507937, 25.297619047619047, 24.206349206349206, 27.579365079365083, 24.503968253968253, 22.61904761904762, 25.0, 25.793650793650798, 24.801587301587304, 25.694444444444443, 26.091269841269842, 24.107142857142858, 25.297619047619047, 24.305555555555554, 25.595238095238095, 25.198412698412696, 25.297619047619047, 24.305555555555554, 24.702380952380953, 25.099206349206348, 25.496031746031743, 25.595238095238095, 25.595238095238095, 24.503968253968253, 23.908730158730158, 23.61111111111111, 24.801587301587304, 24.107142857142858, 24.305555555555554, 23.313492063492063, 26.488095238095237, 24.801587301587304, 24.107142857142858, 25.595238095238095, 25.099206349206348, 23.313492063492063, 23.214285714285715, 24.801587301587304, 25.198412698412696, 26.38888888888889, 23.908730158730158, 23.71031746031746, 25.694444444444443, 25.595238095238095, 26.686507936507937, 23.71031746031746, 24.801587301587304, 26.488095238095237, 24.6031746031746, 25.992063492063494, 22.22222222222222, 26.488095238095237, 24.801587301587304, 25.0, 24.305555555555554, 24.00793650793651, 23.908730158730158, 23.214285714285715, 24.107142857142858, 24.00793650793651, 24.503968253968253, 25.892857142857146, 25.198412698412696, 24.00793650793651, 25.595238095238095, 23.511904761904763, 26.686507936507937, 25.892857142857146, 25.0, 24.900793650793652, 23.61111111111111, 25.198412698412696, 25.0, 26.488095238095237, 26.984126984126984, 24.6031746031746, 24.900793650793652, 25.793650793650798, 27.976190476190478, 24.702380952380953, 23.809523809523807, 25.0, 25.0, 25.297619047619047, 25.793650793650798, 23.115079365079367, 25.099206349206348, 25.496031746031743, 25.793650793650798, 25.892857142857146, 26.28968253968254, 26.28968253968254, 26.984126984126984, 25.297619047619047, 24.801587301587304, 25.099206349206348, 27.18253968253968, 25.992063492063494, 24.00793650793651, 26.686507936507937, 23.511904761904763, 23.809523809523807, 25.793650793650798, 26.488095238095237, 24.503968253968253, 25.793650793650798, 25.595238095238095, 25.595238095238095, 24.702380952380953, 26.190476190476193, 24.702380952380953, 25.198412698412696, 26.28968253968254, 26.686507936507937, 24.801587301587304, 24.6031746031746, 24.702380952380953, 24.404761904761905, 24.404761904761905, 24.900793650793652, 25.892857142857146, 23.511904761904763, 24.900793650793652, 25.694444444444443, 25.595238095238095, 23.115079365079367, 25.892857142857146, 24.900793650793652, 25.694444444444443, 25.595238095238095, 28.174603174603174, 25.595238095238095, 23.71031746031746, 25.694444444444443, 26.38888888888889, 24.305555555555554, 24.503968253968253, 25.396825396825395, 23.511904761904763, 26.091269841269842, 24.801587301587304, 26.190476190476193, 25.297619047619047, 24.00793650793651, 27.083333333333332, 24.305555555555554, 24.900793650793652, 23.908730158730158, 26.28968253968254, 24.702380952380953, 24.801587301587304, 25.297619047619047, 24.503968253968253, 22.916666666666664, 25.396825396825395, 25.992063492063494, 24.6031746031746, 23.908730158730158, 25.892857142857146, 23.511904761904763, 23.214285714285715, 27.18253968253968, 26.190476190476193, 25.396825396825395, 25.595238095238095, 24.900793650793652, 25.793650793650798, 25.892857142857146, 23.313492063492063, 23.41269841269841, 25.992063492063494, 25.793650793650798, 26.686507936507937, 26.091269841269842, 23.71031746031746, 24.305555555555554, 26.884920634920633, 26.785714285714285, 26.190476190476193, 25.793650793650798, 25.099206349206348, 23.214285714285715, 25.0, 23.809523809523807, 25.198412698412696, 26.984126984126984, 26.091269841269842, 23.71031746031746, 24.107142857142858, 26.38888888888889, 25.099206349206348, 25.595238095238095, 24.00793650793651, 26.190476190476193, 24.404761904761905, 25.496031746031743, 24.00793650793651, 23.809523809523807, 24.00793650793651, 25.0, 23.809523809523807, 25.297619047619047, 25.297619047619047, 26.28968253968254, 24.404761904761905, 27.380952380952383, 24.305555555555554, 25.992063492063494, 24.801587301587304, 25.595238095238095, 22.817460317460316, 23.908730158730158, 23.61111111111111, 24.503968253968253, 25.099206349206348, 28.174603174603174, 24.801587301587304, 24.900793650793652, 26.38888888888889, 26.091269841269842, 27.083333333333332, 24.00793650793651, 25.892857142857146, 25.595238095238095, 25.801587301587304, 25.900793650793652, 26.984126984126984, 25.793650793650798, 26.58730158730159, 26.686507936507937, 26.900793650793652, 26.488095238095237, 25.801587301587304, 26.61111111111111, 25.107142857142858]


# ヒストグラムを描画
plt.hist(data, bins=range(21, 29), edgecolor='black', align='left')

# x軸とy軸のラベルを設定
plt.xlabel('Error Rate of sifted key')
plt.ylabel('Frequency')

# グラフのタイトルを設定
plt.title('Error Rate of sifted key vs  Frequency of Error Rate (1000 times)')

# x軸の範囲を設定
plt.xlim(21, 28)

# グリッドを追加
plt.grid(axis='y')

# グラフをPNGファイルに保存
plt.savefig('eavesdropping.png', format='png', bbox_inches="tight", dpi=300)

# グラフを表示
plt.show()