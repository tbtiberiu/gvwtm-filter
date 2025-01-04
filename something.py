# def gvwtm_filter(image, window_size=3):
#     # Dimensiunea imaginii
#     [L, C] = np.shape(img)
#     # Inițializare imagine filtrată
#     filtered_img = np.zeros_like(image)
#     pad = window_size // 2

#     # Parcurgerea fiecărui pixel (excluzând marginile)
#     for i in range(pad, rows - pad):
#         for j in range(pad, cols - pad):
#             # Extrage vecinătatea 3x3
#             neighborhood = image[i - pad:i + pad + 1, j - pad:j + pad + 1]

#             # Calcularea medianei vecinătății
#             median_val = np.median(neighborhood)

#             # Calculul ponderilor dinamice
#             weights = np.abs(neighborhood - median_val)
#             weights = 1 / (weights + 1)  # Evită împărțirea la zero

#             # Înlocuirea pixelului central cu media ponderată
#             filtered_img[i, j] = np.sum(neighborhood * weights) / np.sum(weights)

#     return filtered_img
