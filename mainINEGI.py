import utils.imports as inp
import utils.visuals as visu
import utils.processing as proc
import pandas as pd

data = inp.read_natalidad_dataset("data\conjunto_de_datos_natalidad_2022.csv")
print("archivo txt cargado")
data_edades_padres = data[["edad_madn", "edad_padn", "ent_regis"]]
# quitar datos donde edad >=99
idx_filtered = data_edades_padres[data_edades_padres["edad_madn"] == 99].index
data_edades_padres.drop(idx_filtered, inplace=True)
idx_filtered = data_edades_padres[data_edades_padres["edad_padn"] == 99].index
data_edades_padres.drop(idx_filtered, inplace=True)


# implementar plotly 2d histogram
# visu.save_heatmap_edades(data_edades_padres)
visu.save_heatmap_edades_logaritmico(data_edades_padres)
print("grafica de padres completa")