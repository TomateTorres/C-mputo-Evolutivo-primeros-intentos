#%%
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#%%
# Ackley Elitismo
elitismoAckley1 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_10_semilla_1729572032.csv")
elitismoAckley2 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_11_semilla_1729572034.csv")
elitismoAckley3 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_12_semilla_1729572035.csv")
elitismoAckley4 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_13_semilla_1729572036.csv")
elitismoAckley5 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_14_semilla_1729572038.csv")
elitismoAckley6 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_15_semilla_1729572039.csv")
elitismoAckley7 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_16_semilla_1729572040.csv")
elitismoAckley8 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_17_semilla_1729572041.csv")
elitismoAckley9 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_18_semilla_1729572043.csv")
elitismoAckley10 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_19_semilla_1729572044.csv")
elitismoAckley11 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_1_semilla_1729572004.csv")
elitismoAckley12 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_20_semilla_1729572045.csv")
elitismoAckley13 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_21_semilla_1729572047.csv")
elitismoAckley14 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_23_semilla_1729572049.csv")
elitismoAckley15 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_24_semilla_1729572050.csv")
elitismoAckley16 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_25_semilla_1729572052.csv")
elitismoAckley17 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_26_semilla_1729572053.csv")
elitismoAckley18 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_27_semilla_1729572054.csv")
elitismoAckley19 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_28_semilla_1729572055.csv")
elitismoAckley20 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_29_semilla_1729572057.csv")
elitismoAckley21 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_2_semilla_1729572022.csv")
elitismoAckley22 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_30_semilla_1729572058.csv")
elitismoAckley23 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_4_semilla_1729572025.csv")
elitismoAckley24 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_5_semilla_1729572026.csv")
elitismoAckley25 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_6_semilla_1729572027.csv")
elitismoAckley26 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_7_semilla_1729572029.csv")
elitismoAckley27 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_8_semilla_1729572030.csv")
elitismoAckley28 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_9_semilla_1729572031.csv")
elitismoAckley29 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_22_semilla_1729572048.csv")
elitismoAckley30 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_elitismo_3_semilla_1729572024.csv")
#%%
# Ackley Generacional 
generacionalAckley1 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_1_semilla_1729572700.csv")
generacionalAckley2 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_2_semilla_1729572711.csv")
generacionalAckley3 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_3_semilla_1729572712.csv")
generacionalAckley4 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_4_semilla_1729572713.csv")
generacionalAckley5 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_5_semilla_1729572715.csv")
generacionalAckley6 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_6_semilla_1729572716.csv")
generacionalAckley7 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_7_semilla_1729572717.csv")
generacionalAckley8 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_8_semilla_1729572718.csv")
generacionalAckley9 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_9_semilla_1729572720.csv")
generacionalAckley10 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_10_semilla_1729572721.csv")
generacionalAckley11 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_11_semilla_1729572722.csv")
generacionalAckley12 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_12_semilla_1729572723.csv")
generacionalAckley13 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_13_semilla_1729572725.csv")
generacionalAckley14 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_14_semilla_1729572726.csv")
generacionalAckley15 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_15_semilla_1729572727.csv")
generacionalAckley16 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_16_semilla_1729572729.csv")
generacionalAckley17 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_17_semilla_1729572730.csv")
generacionalAckley18 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_18_semilla_1729572731.csv")
generacionalAckley19 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_19_semilla_1729572732.csv")
generacionalAckley20 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_20_semilla_1729572734.csv")
generacionalAckley21 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_21_semilla_1729572735.csv")
generacionalAckley22 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_22_semilla_1729572736.csv")
generacionalAckley23 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_23_semilla_1729572738.csv")
generacionalAckley24 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_24_semilla_1729572739.csv")
generacionalAckley25 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_25_semilla_1729572740.csv")
generacionalAckley26 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_26_semilla_1729572741.csv")
generacionalAckley27 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_27_semilla_1729572743.csv")
generacionalAckley28 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_28_semilla_1729572744.csv")
generacionalAckley29 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_29_semilla_1729572745.csv")
generacionalAckley30 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_generacional_30_semilla_1729572747.csv")
#%% Ackley Peores
peoresAckley1 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_1_semilla_1729573134.csv")
peoresAckley2 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_2_semilla_1729573147.csv")
peoresAckley3 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_3_semilla_1729573148.csv")
peoresAckley4 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_4_semilla_1729573149.csv")
peoresAckley5 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_5_semilla_1729573150.csv")
peoresAckley6 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_6_semilla_1729573152.csv")
peoresAckley7 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_7_semilla_1729573153.csv")
peoresAckley8 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_8_semilla_1729573154.csv")
peoresAckley9 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_9_semilla_1729573156.csv")
peoresAckley10 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_10_semilla_1729573157.csv")
peoresAckley11 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_11_semilla_1729573158.csv")
peoresAckley12 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_12_semilla_1729573160.csv")
peoresAckley13 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_13_semilla_1729573161.csv")
peoresAckley14 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_14_semilla_1729573162.csv")
peoresAckley15 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_15_semilla_1729573163.csv")
peoresAckley16 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_16_semilla_1729573165.csv")
peoresAckley17 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_17_semilla_1729573166.csv")
peoresAckley18 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_18_semilla_1729573167.csv")
peoresAckley19 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_19_semilla_1729573169.csv")
peoresAckley20 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_20_semilla_1729573170.csv")
peoresAckley21 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_21_semilla_1729573171.csv")
peoresAckley22 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_22_semilla_1729573172.csv")
peoresAckley23 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_23_semilla_1729573174.csv")
peoresAckley24 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_24_semilla_1729573175.csv")
peoresAckley45 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_25_semilla_1729573176.csv")
peoresAckley26 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_26_semilla_1729573178.csv")
peoresAckley27 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_27_semilla_1729573179.csv")
peoresAckley28 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_28_semilla_1729573180.csv")
peoresAckley29 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_29_semilla_1729573181.csv")
peoresAckley30 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Ackley/Ackley_resultados_peores_30_semilla_1729573183.csv")

#%% 
# Ackley lineal y geometrico

base = "https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/main/Tarea%205/Ejecuciones_Ackley/"

geometricoAckley1 = pd.read_csv(base + "Ackley_resultados_geometrico_1_semilla_1729910682.csv")
geometricoAckley2 = pd.read_csv(base + "Ackley_resultados_geometrico_2_semilla_1729910683.csv")
geometricoAckley3 = pd.read_csv(base + "Ackley_resultados_geometrico_3_semilla_1729910684.csv")
geometricoAckley4 = pd.read_csv(base + "Ackley_resultados_geometrico_4_semilla_1729910685.csv")
geometricoAckley5 = pd.read_csv(base + "Ackley_resultados_geometrico_5_semilla_1729910686.csv")
geometricoAckley6 = pd.read_csv(base + "Ackley_resultados_geometrico_6_semilla_1729910687.csv")
geometricoAckley7 = pd.read_csv(base + "Ackley_resultados_geometrico_7_semilla_1729910688.csv")
geometricoAckley8 = pd.read_csv(base + "Ackley_resultados_geometrico_8_semilla_1729910689.csv")
geometricoAckley9 = pd.read_csv(base + "Ackley_resultados_geometrico_9_semilla_1729910690.csv")
geometricoAckley10 = pd.read_csv(base + "Ackley_resultados_geometrico_10_semilla_1729910691.csv")
geometricoAckley11 = pd.read_csv(base + "Ackley_resultados_geometrico_11_semilla_1729910692.csv")
geometricoAckley12 = pd.read_csv(base + "Ackley_resultados_geometrico_12_semilla_1729910693.csv")
geometricoAckley13 = pd.read_csv(base + "Ackley_resultados_geometrico_13_semilla_1729910694.csv")
geometricoAckley14 = pd.read_csv(base + "Ackley_resultados_geometrico_14_semilla_1729910695.csv")
geometricoAckley15 = pd.read_csv(base + "Ackley_resultados_geometrico_15_semilla_1729910696.csv")
geometricoAckley16 = pd.read_csv(base + "Ackley_resultados_geometrico_16_semilla_1729910697.csv")
geometricoAckley17 = pd.read_csv(base + "Ackley_resultados_geometrico_17_semilla_1729910699.csv")
geometricoAckley18 = pd.read_csv(base + "Ackley_resultados_geometrico_18_semilla_1729910700.csv")
geometricoAckley19 = pd.read_csv(base + "Ackley_resultados_geometrico_19_semilla_1729910701.csv")
geometricoAckley20 = pd.read_csv(base + "Ackley_resultados_geometrico_20_semilla_1729910702.csv")
geometricoAckley21 = pd.read_csv(base + "Ackley_resultados_geometrico_21_semilla_1729910703.csv")
geometricoAckley22 = pd.read_csv(base + "Ackley_resultados_geometrico_22_semilla_1729910704.csv")
geometricoAckley23 = pd.read_csv(base + "Ackley_resultados_geometrico_23_semilla_1729910705.csv")
geometricoAckley24 = pd.read_csv(base + "Ackley_resultados_geometrico_24_semilla_1729910706.csv")
geometricoAckley25 = pd.read_csv(base + "Ackley_resultados_geometrico_25_semilla_1729910707.csv")
geometricoAckley26 = pd.read_csv(base + "Ackley_resultados_geometrico_26_semilla_1729910708.csv")
geometricoAckley27 = pd.read_csv(base + "Ackley_resultados_geometrico_27_semilla_1729910709.csv")
geometricoAckley28 = pd.read_csv(base + "Ackley_resultados_geometrico_28_semilla_1729910710.csv")
geometricoAckley29 = pd.read_csv(base + "Ackley_resultados_geometrico_29_semilla_1729910711.csv")
geometricoAckley30 = pd.read_csv(base + "Ackley_resultados_geometrico_30_semilla_1729910712.csv")

linealAckley1 = pd.read_csv(base + "Ackley_resultados_lineal_1_semilla_1729910669.csv")
linealAckley2 = pd.read_csv(base + "Ackley_resultados_lineal_2_semilla_1729910670.csv")
linealAckley3 = pd.read_csv(base + "Ackley_resultados_lineal_3_semilla_1729910671.csv")
linealAckley4 = pd.read_csv(base + "Ackley_resultados_lineal_4_semilla_1729910672.csv")
linealAckley5 = pd.read_csv(base + "Ackley_resultados_lineal_5_semilla_1729910673.csv")
linealAckley6 = pd.read_csv(base + "Ackley_resultados_lineal_6_semilla_1729910674.csv")
linealAckley7 = pd.read_csv(base + "Ackley_resultados_lineal_7_semilla_1729910676.csv")
linealAckley8 = pd.read_csv(base + "Ackley_resultados_lineal_8_semilla_1729910677.csv")
linealAckley9 = pd.read_csv(base + "Ackley_resultados_lineal_9_semilla_1729910678.csv")
linealAckley10 = pd.read_csv(base + "Ackley_resultados_lineal_10_semilla_1729910679.csv")
linealAckley11 = pd.read_csv(base + "Ackley_resultados_lineal_11_semilla_1729910680.csv")
linealAckley12 = pd.read_csv(base + "Ackley_resultados_lineal_12_semilla_1729910681.csv")
linealAckley13 = pd.read_csv(base + "Ackley_resultados_lineal_13_semilla_1729910682.csv")
linealAckley14 = pd.read_csv(base + "Ackley_resultados_lineal_14_semilla_1729910683.csv")
linealAckley15 = pd.read_csv(base + "Ackley_resultados_lineal_15_semilla_1729910684.csv")
linealAckley16 = pd.read_csv(base + "Ackley_resultados_lineal_16_semilla_1729910685.csv")
linealAckley17 = pd.read_csv(base + "Ackley_resultados_lineal_17_semilla_1729910686.csv")
linealAckley18 = pd.read_csv(base + "Ackley_resultados_lineal_18_semilla_1729910687.csv")
linealAckley19 = pd.read_csv(base + "Ackley_resultados_lineal_19_semilla_1729910688.csv")
linealAckley20 = pd.read_csv(base + "Ackley_resultados_lineal_20_semilla_1729910689.csv")
linealAckley21 = pd.read_csv(base + "Ackley_resultados_lineal_21_semilla_1729910690.csv")
linealAckley22 = pd.read_csv(base + "Ackley_resultados_lineal_22_semilla_1729910691.csv")
linealAckley23 = pd.read_csv(base + "Ackley_resultados_lineal_23_semilla_1729910692.csv")
linealAckley24 = pd.read_csv(base + "Ackley_resultados_lineal_24_semilla_1729910693.csv")
linealAckley25 = pd.read_csv(base + "Ackley_resultados_lineal_25_semilla_1729910694.csv")
linealAckley26 = pd.read_csv(base + "Ackley_resultados_lineal_26_semilla_1729910695.csv")
linealAckley27 = pd.read_csv(base + "Ackley_resultados_lineal_27_semilla_1729910696.csv")
linealAckley28 = pd.read_csv(base + "Ackley_resultados_lineal_28_semilla_1729910697.csv")
linealAckley29 = pd.read_csv(base + "Ackley_resultados_lineal_29_semilla_1729910698.csv")
linealAckley30 = pd.read_csv(base + "Ackley_resultados_lineal_30_semilla_1729910699.csv")


# %%
# Griewank elitismo
elitismoGriewank1 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_1_semilla_1729572137.csv")
elitismoGriewank2 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_2_semilla_1729572148.csv")
elitismoGriewank3 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_3_semilla_1729572149.csv")
elitismoGriewank4 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_4_semilla_1729572150.csv")
elitismoGriewank5 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_5_semilla_1729572152.csv")
elitismoGriewank6 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_6_semilla_1729572153.csv")
elitismoGriewank7 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_7_semilla_1729572154.csv")
elitismoGriewank8 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_8_semilla_1729572156.csv")
elitismoGriewank9 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_9_semilla_1729572157.csv")
elitismoGriewank10 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_10_semilla_1729572158.csv")
elitismoGriewank11 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_11_semilla_1729572159.csv")
elitismoGriewank12 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_12_semilla_1729572161.csv")
elitismoGriewank13 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_13_semilla_1729572162.csv")
elitismoGriewank14 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_14_semilla_1729572163.csv")
elitismoGriewank15 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_15_semilla_1729572164.csv")
elitismoGriewank16 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_16_semilla_1729572166.csv")
elitismoGriewank17 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_17_semilla_1729572167.csv")
elitismoGriewank18 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_18_semilla_1729572168.csv")
elitismoGriewank19 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_19_semilla_1729572170.csv")
elitismoGriewank20 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_20_semilla_1729572171.csv")
elitismoGriewank21 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_21_semilla_1729572172.csv")
elitismoGriewank22 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_22_semilla_1729572173.csv")
elitismoGriewank23 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_23_semilla_1729572175.csv")
elitismoGriewank24 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_24_semilla_1729572176.csv")
elitismoGriewank25 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_25_semilla_1729572177.csv")
elitismoGriewank26 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_26_semilla_1729572179.csv")
elitismoGriewank27 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_27_semilla_1729572180.csv")
elitismoGriewank28 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_28_semilla_1729572181.csv")
elitismoGriewank29 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_29_semilla_1729572182.csv")
elitismoGriewank30 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_elitismo_30_semilla_1729572184.csv")

#%%
# Griewank generacional
generacionalGriewank1 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_1_semilla_1729572857.csv")
generacionalGriewank2 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_2_semilla_1729572868.csv")
generacionalGriewank3 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_3_semilla_1729572869.csv")
generacionalGriewank4 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_4_semilla_1729572871.csv")
generacionalGriewank5 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_5_semilla_1729572872.csv")
generacionalGriewank6 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_6_semilla_1729572873.csv")
generacionalGriewank7 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_7_semilla_1729572874.csv")
generacionalGriewank8 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_8_semilla_1729572876.csv")
generacionalGriewank9 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_9_semilla_1729572877.csv")
generacionalGriewank10 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_10_semilla_1729572878.csv")
generacionalGriewank11 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_11_semilla_1729572879.csv")
generacionalGriewank12 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_12_semilla_1729572881.csv")
generacionalGriewank13 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_13_semilla_1729572882.csv")
generacionalGriewank14 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_14_semilla_1729572883.csv")
generacionalGriewank15 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_15_semilla_1729572885.csv")
generacionalGriewank16 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_16_semilla_1729572886.csv")
generacionalGriewank17 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_17_semilla_1729572887.csv")
generacionalGriewank18 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_18_semilla_1729572888.csv")
generacionalGriewank19 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_19_semilla_1729572890.csv")
generacionalGriewank20 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_20_semilla_1729572891.csv")
generacionalGriewank21 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_21_semilla_1729572892.csv")
generacionalGriewank22 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_22_semilla_1729572894.csv")
generacionalGriewank23 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_23_semilla_1729572895.csv")
generacionalGriewank24 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_24_semilla_1729572896.csv")
generacionalGriewank25 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_25_semilla_1729572898.csv")
generacionalGriewank26 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_26_semilla_1729572899.csv")
generacionalGriewank27 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_27_semilla_1729572900.csv")
generacionalGriewank28 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_28_semilla_1729572901.csv")
generacionalGriewank29 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_29_semilla_1729572903.csv")
generacionalGriewank30 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_generacional_30_semilla_1729572904.csv")

#%%

# Griewank peores
peoresGriewank1 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_1_semilla_1729573193.csv")
peoresGriewank2 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_2_semilla_1729573205.csv")
peoresGriewank3 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_3_semilla_1729573207.csv")
peoresGriewank4 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_4_semilla_1729573208.csv")
peoresGriewank5 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_5_semilla_1729573209.csv")
peoresGriewank6 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_6_semilla_1729573211.csv")
peoresGriewank7 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_7_semilla_1729573212.csv")
peoresGriewank8 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_8_semilla_1729573213.csv")
peoresGriewank9 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_9_semilla_1729573215.csv")
peoresGriewank10 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_10_semilla_1729573216.csv")
peoresGriewank11 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_11_semilla_1729573217.csv")
peoresGriewank12 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_12_semilla_1729573218.csv")
peoresGriewank13 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_13_semilla_1729573220.csv")
peoresGriewank14 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_14_semilla_1729573221.csv")
peoresGriewank15 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_15_semilla_1729573222.csv")
peoresGriewank16 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_16_semilla_1729573224.csv")
peoresGriewank17 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_17_semilla_1729573225.csv")
peoresGriewank18 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_18_semilla_1729573226.csv")
peoresGriewank19 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_19_semilla_1729573227.csv")
peoresGriewank20 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_20_semilla_1729573229.csv")
peoresGriewank21 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_21_semilla_1729573230.csv")
peoresGriewank22 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_22_semilla_1729573231.csv")
peoresGriewank23 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_23_semilla_1729573233.csv")
peoresGriewank24 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_24_semilla_1729573234.csv")
peoresGriewank25 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_25_semilla_1729573235.csv")
peoresGriewank26 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_26_semilla_1729573236.csv")
peoresGriewank27 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_27_semilla_1729573238.csv")
peoresGriewank28 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_28_semilla_1729573239.csv")
peoresGriewank29 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_29_semilla_1729573240.csv")
peoresGriewank30 = pd.read_csv("https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Griewank/Griewank_resultados_peores_30_semilla_1729573242.csv")

#%% 
# Griewank lineal 
base_5 = "https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/main/Tarea%205/Ejecuciones_Griewank/"

linealGriewank1 = pd.read_csv(base_5 + "Griewank_resultados_lineal_1_semilla_1729911270.csv")
linealGriewank2 = pd.read_csv(base_5 + "Griewank_resultados_lineal_2_semilla_1729911271.csv")
linealGriewank3 = pd.read_csv(base_5 + "Griewank_resultados_lineal_3_semilla_1729911272.csv")
linealGriewank4 = pd.read_csv(base_5 + "Griewank_resultados_lineal_4_semilla_1729911273.csv")
linealGriewank5 = pd.read_csv(base_5 + "Griewank_resultados_lineal_5_semilla_1729911274.csv")
linealGriewank6 = pd.read_csv(base_5 + "Griewank_resultados_lineal_6_semilla_1729911275.csv")
linealGriewank7 = pd.read_csv(base_5 + "Griewank_resultados_lineal_7_semilla_1729911276.csv")
linealGriewank8 = pd.read_csv(base_5 + "Griewank_resultados_lineal_8_semilla_1729911277.csv")
linealGriewank9 = pd.read_csv(base_5 + "Griewank_resultados_lineal_9_semilla_1729911278.csv")
linealGriewank10 = pd.read_csv(base_5 + "Griewank_resultados_lineal_10_semilla_1729911279.csv")
linealGriewank11 = pd.read_csv(base_5 + "Griewank_resultados_lineal_11_semilla_1729911280.csv")
linealGriewank12 = pd.read_csv(base_5 + "Griewank_resultados_lineal_12_semilla_1729911281.csv")
linealGriewank13 = pd.read_csv(base_5 + "Griewank_resultados_lineal_13_semilla_1729911282.csv")
linealGriewank14 = pd.read_csv(base_5 + "Griewank_resultados_lineal_14_semilla_1729911283.csv")
linealGriewank15 = pd.read_csv(base_5 + "Griewank_resultados_lineal_15_semilla_1729911284.csv")
linealGriewank16 = pd.read_csv(base_5 + "Griewank_resultados_lineal_16_semilla_1729911285.csv")
linealGriewank17 = pd.read_csv(base_5 + "Griewank_resultados_lineal_17_semilla_1729911286.csv")
linealGriewank18 = pd.read_csv(base_5 + "Griewank_resultados_lineal_18_semilla_1729911287.csv")
linealGriewank19 = pd.read_csv(base_5 + "Griewank_resultados_lineal_19_semilla_1729911288.csv")
linealGriewank20 = pd.read_csv(base_5 + "Griewank_resultados_lineal_20_semilla_1729911289.csv")
linealGriewank21 = pd.read_csv(base_5 + "Griewank_resultados_lineal_21_semilla_1729911290.csv")
linealGriewank22 = pd.read_csv(base_5 + "Griewank_resultados_lineal_22_semilla_1729911291.csv")
linealGriewank23 = pd.read_csv(base_5 + "Griewank_resultados_lineal_23_semilla_1729911292.csv")
linealGriewank24 = pd.read_csv(base_5 + "Griewank_resultados_lineal_24_semilla_1729911293.csv")
linealGriewank25 = pd.read_csv(base_5 + "Griewank_resultados_lineal_25_semilla_1729911294.csv")
linealGriewank26 = pd.read_csv(base_5 + "Griewank_resultados_lineal_26_semilla_1729911295.csv")
linealGriewank27 = pd.read_csv(base_5 + "Griewank_resultados_lineal_27_semilla_1729911296.csv")
linealGriewank28 = pd.read_csv(base_5 + "Griewank_resultados_lineal_28_semilla_1729911297.csv")
linealGriewank29 = pd.read_csv(base_5 + "Griewank_resultados_lineal_29_semilla_1729911298.csv")
linealGriewank30 = pd.read_csv(base_5 + "Griewank_resultados_lineal_30_semilla_1729911299.csv")

#%%
# y geometrico
geometricoGriewank1 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_1_semilla_1729911277.csv")
geometricoGriewank2 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_2_semilla_1729911278.csv")
geometricoGriewank3 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_3_semilla_1729911279.csv")
geometricoGriewank4 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_4_semilla_1729911280.csv")
geometricoGriewank5 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_5_semilla_1729911281.csv")
geometricoGriewank6 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_6_semilla_1729911282.csv")
geometricoGriewank7 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_7_semilla_1729911283.csv")
geometricoGriewank8 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_8_semilla_1729911284.csv")
geometricoGriewank9 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_9_semilla_1729911285.csv")
geometricoGriewank10 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_10_semilla_1729911286.csv")
geometricoGriewank11 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_11_semilla_1729911287.csv")
geometricoGriewank12 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_12_semilla_1729911288.csv")
geometricoGriewank13 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_13_semilla_1729911289.csv")
geometricoGriewank14 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_14_semilla_1729911290.csv")
geometricoGriewank15 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_15_semilla_1729911291.csv")
geometricoGriewank16 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_16_semilla_1729911292.csv")
geometricoGriewank17 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_17_semilla_1729911293.csv")
geometricoGriewank18 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_18_semilla_1729911294.csv")
geometricoGriewank19 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_19_semilla_1729911295.csv")
geometricoGriewank20 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_20_semilla_1729911296.csv")
geometricoGriewank21 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_21_semilla_1729911297.csv")
geometricoGriewank22 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_22_semilla_1729911298.csv")
geometricoGriewank23 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_23_semilla_1729911299.csv")
geometricoGriewank24 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_24_semilla_1729911300.csv")
geometricoGriewank25 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_25_semilla_1729911301.csv")
geometricoGriewank26 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_26_semilla_1729911302.csv")
geometricoGriewank27 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_27_semilla_1729911303.csv")
geometricoGriewank28 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_28_semilla_1729911304.csv")
geometricoGriewank29 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_29_semilla_1729911305.csv")
geometricoGriewank30 = pd.read_csv(base_5 + "Griewank_resultados_geometrico_30_semilla_1729911306.csv")

#%% Rasreigin
# URL base
base_url = "https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Rastrigin/Rastrigin_resultados_"

# Rastrigin elitismo
elitismoRastrigin10 = pd.read_csv(base_url + "elitismo_10_semilla_1729572404.csv")
elitismoRastrigin11 = pd.read_csv(base_url + "elitismo_11_semilla_1729572406.csv")
elitismoRastrigin12 = pd.read_csv(base_url + "elitismo_12_semilla_1729572407.csv")
elitismoRastrigin13 = pd.read_csv(base_url + "elitismo_13_semilla_1729572408.csv")
elitismoRastrigin14 = pd.read_csv(base_url + "elitismo_14_semilla_1729572409.csv")
elitismoRastrigin15 = pd.read_csv(base_url + "elitismo_15_semilla_1729572411.csv")
elitismoRastrigin16 = pd.read_csv(base_url + "elitismo_16_semilla_1729572412.csv")
elitismoRastrigin17 = pd.read_csv(base_url + "elitismo_17_semilla_1729572413.csv")
elitismoRastrigin18 = pd.read_csv(base_url + "elitismo_18_semilla_1729572415.csv")
elitismoRastrigin19 = pd.read_csv(base_url + "elitismo_19_semilla_1729572416.csv")
elitismoRastrigin1 = pd.read_csv(base_url + "elitismo_1_semilla_1729572393.csv")
elitismoRastrigin20 = pd.read_csv(base_url + "elitismo_20_semilla_1729572417.csv")
elitismoRastrigin21 = pd.read_csv(base_url + "elitismo_21_semilla_1729572418.csv")
elitismoRastrigin22 = pd.read_csv(base_url + "elitismo_22_semilla_1729572420.csv")
elitismoRastrigin23 = pd.read_csv(base_url + "elitismo_23_semilla_1729572421.csv")
elitismoRastrigin24 = pd.read_csv(base_url + "elitismo_24_semilla_1729572422.csv")
elitismoRastrigin25 = pd.read_csv(base_url + "elitismo_25_semilla_1729572424.csv")
elitismoRastrigin26 = pd.read_csv(base_url + "elitismo_26_semilla_1729572425.csv")
elitismoRastrigin27 = pd.read_csv(base_url + "elitismo_27_semilla_1729572426.csv")
elitismoRastrigin28 = pd.read_csv(base_url + "elitismo_28_semilla_1729572427.csv")
elitismoRastrigin29 = pd.read_csv(base_url + "elitismo_29_semilla_1729572429.csv")
elitismoRastrigin2 = pd.read_csv(base_url + "elitismo_2_semilla_1729572394.csv")
elitismoRastrigin30 = pd.read_csv(base_url + "elitismo_30_semilla_1729572430.csv")
elitismoRastrigin3 = pd.read_csv(base_url + "elitismo_3_semilla_1729572395.csv")
elitismoRastrigin4 = pd.read_csv(base_url + "elitismo_4_semilla_1729572397.csv")
elitismoRastrigin5 = pd.read_csv(base_url + "elitismo_5_semilla_1729572398.csv")
elitismoRastrigin6 = pd.read_csv(base_url + "elitismo_6_semilla_1729572399.csv")
elitismoRastrigin7 = pd.read_csv(base_url + "elitismo_7_semilla_1729572400.csv")
elitismoRastrigin8 = pd.read_csv(base_url + "elitismo_8_semilla_1729572402.csv")
elitismoRastrigin9 = pd.read_csv(base_url + "elitismo_9_semilla_1729572403.csv")

#%% Ratrigin remplazo generacional
generacionalRastrigin10 = pd.read_csv(base_url + "generacional_10_semilla_1729572936.csv")
generacionalRastrigin11 = pd.read_csv(base_url + "generacional_11_semilla_1729572938.csv")
generacionalRastrigin12 = pd.read_csv(base_url + "generacional_12_semilla_1729572939.csv")
generacionalRastrigin13 = pd.read_csv(base_url + "generacional_13_semilla_1729572940.csv")
generacionalRastrigin14 = pd.read_csv(base_url + "generacional_14_semilla_1729572941.csv")
generacionalRastrigin15 = pd.read_csv(base_url + "generacional_15_semilla_1729572943.csv")
generacionalRastrigin16 = pd.read_csv(base_url + "generacional_16_semilla_1729572944.csv")
generacionalRastrigin17 = pd.read_csv(base_url + "generacional_17_semilla_1729572945.csv")
generacionalRastrigin18 = pd.read_csv(base_url + "generacional_18_semilla_1729572947.csv")
generacionalRastrigin19 = pd.read_csv(base_url + "generacional_19_semilla_1729572948.csv")
generacionalRastrigin1 = pd.read_csv(base_url + "generacional_1_semilla_1729572915.csv")
generacionalRastrigin20 = pd.read_csv(base_url + "generacional_20_semilla_1729572949.csv")
generacionalRastrigin21 = pd.read_csv(base_url + "generacional_21_semilla_1729572950.csv")
generacionalRastrigin22 = pd.read_csv(base_url + "generacional_22_semilla_1729572952.csv")
generacionalRastrigin23 = pd.read_csv(base_url + "generacional_23_semilla_1729572953.csv")
generacionalRastrigin24 = pd.read_csv(base_url + "generacional_24_semilla_1729572954.csv")
generacionalRastrigin25 = pd.read_csv(base_url + "generacional_25_semilla_1729572956.csv")
generacionalRastrigin26 = pd.read_csv(base_url + "generacional_26_semilla_1729572957.csv")
generacionalRastrigin27 = pd.read_csv(base_url + "generacional_27_semilla_1729572958.csv")
generacionalRastrigin28 = pd.read_csv(base_url + "generacional_28_semilla_1729572959.csv")
generacionalRastrigin29 = pd.read_csv(base_url + "generacional_29_semilla_1729572961.csv")
generacionalRastrigin2 = pd.read_csv(base_url + "generacional_2_semilla_1729572926.csv")
generacionalRastrigin30 = pd.read_csv(base_url + "generacional_30_semilla_1729572962.csv")
generacionalRastrigin3 = pd.read_csv(base_url + "generacional_3_semilla_1729572927.csv")
generacionalRastrigin4 = pd.read_csv(base_url + "generacional_4_semilla_1729572929.csv")
generacionalRastrigin5 = pd.read_csv(base_url + "generacional_5_semilla_1729572930.csv")
generacionalRastrigin6 = pd.read_csv(base_url + "generacional_6_semilla_1729572931.csv")
generacionalRastrigin7 = pd.read_csv(base_url + "generacional_7_semilla_1729572932.csv")
generacionalRastrigin8 = pd.read_csv(base_url + "generacional_8_semilla_1729572934.csv")
generacionalRastrigin9 = pd.read_csv(base_url + "generacional_9_semilla_1729572935.csv")

#%% Rastrigin remplazo peores
peoresRastrigin10 = pd.read_csv(base_url + "peores_10_semilla_1729573276.csv")
peoresRastrigin11 = pd.read_csv(base_url + "peores_11_semilla_1729573277.csv")
peoresRastrigin12 = pd.read_csv(base_url + "peores_12_semilla_1729573279.csv")
peoresRastrigin13 = pd.read_csv(base_url + "peores_13_semilla_1729573280.csv")
peoresRastrigin14 = pd.read_csv(base_url + "peores_14_semilla_1729573281.csv")
peoresRastrigin15 = pd.read_csv(base_url + "peores_15_semilla_1729573283.csv")
peoresRastrigin16 = pd.read_csv(base_url + "peores_16_semilla_1729573284.csv")
peoresRastrigin17 = pd.read_csv(base_url + "peores_17_semilla_1729573285.csv")
peoresRastrigin18 = pd.read_csv(base_url + "peores_18_semilla_1729573286.csv")
peoresRastrigin19 = pd.read_csv(base_url + "peores_19_semilla_1729573288.csv")
peoresRastrigin1 = pd.read_csv(base_url + "peores_1_semilla_1729573253.csv")
peoresRastrigin20 = pd.read_csv(base_url + "peores_20_semilla_1729573289.csv")
peoresRastrigin21 = pd.read_csv(base_url + "peores_21_semilla_1729573290.csv")
peoresRastrigin22 = pd.read_csv(base_url + "peores_22_semilla_1729573292.csv")
peoresRastrigin23 = pd.read_csv(base_url + "peores_23_semilla_1729573293.csv")
peoresRastrigin24 = pd.read_csv(base_url + "peores_24_semilla_1729573294.csv")
peoresRastrigin25 = pd.read_csv(base_url + "peores_25_semilla_1729573295.csv")
peoresRastrigin26 = pd.read_csv(base_url + "peores_26_semilla_1729573297.csv")
peoresRastrigin27 = pd.read_csv(base_url + "peores_27_semilla_1729573298.csv")
peoresRastrigin28 = pd.read_csv(base_url + "peores_28_semilla_1729573299.csv")
peoresRastrigin29 = pd.read_csv(base_url + "peores_29_semilla_1729573301.csv")
peoresRastrigin2 = pd.read_csv(base_url + "peores_2_semilla_1729573266.csv")
peoresRastrigin30 = pd.read_csv(base_url + "peores_30_semilla_1729573302.csv")
peoresRastrigin3 = pd.read_csv(base_url + "peores_3_semilla_1729573267.csv")
peoresRastrigin4 = pd.read_csv(base_url + "peores_4_semilla_1729573268.csv")
peoresRastrigin5 = pd.read_csv(base_url + "peores_5_semilla_1729573270.csv")
peoresRastrigin6 = pd.read_csv(base_url + "peores_6_semilla_1729573271.csv")
peoresRastrigin7 = pd.read_csv(base_url + "peores_7_semilla_1729573272.csv")
peoresRastrigin8 = pd.read_csv(base_url + "peores_8_semilla_1729573274.csv")
peoresRastrigin9 = pd.read_csv(base_url + "peores_9_semilla_1729573275.csv")

#%% Rastrigin Geometrico

base_6 = "https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/main/Tarea%205/Ejecuciones_Rastrigin/"

geometricoRastrigin1 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_1_semilla_1729911618.csv")
geometricoRastrigin2 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_2_semilla_1729911619.csv")
geometricoRastrigin3 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_3_semilla_1729911620.csv")
geometricoRastrigin4 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_4_semilla_1729911621.csv")
geometricoRastrigin5 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_5_semilla_1729911622.csv")
geometricoRastrigin6 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_6_semilla_1729911623.csv")
geometricoRastrigin7 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_7_semilla_1729911624.csv")
geometricoRastrigin8 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_8_semilla_1729911625.csv")
geometricoRastrigin9 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_9_semilla_1729911626.csv")
geometricoRastrigin10 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_10_semilla_1729911627.csv")
geometricoRastrigin11 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_11_semilla_1729911628.csv")
geometricoRastrigin12 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_12_semilla_1729911629.csv")
geometricoRastrigin13 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_13_semilla_1729911630.csv")
geometricoRastrigin14 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_14_semilla_1729911631.csv")
geometricoRastrigin15 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_15_semilla_1729911632.csv")
geometricoRastrigin16 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_16_semilla_1729911633.csv")
geometricoRastrigin17 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_17_semilla_1729911634.csv")
geometricoRastrigin18 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_18_semilla_1729911635.csv")
geometricoRastrigin19 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_19_semilla_1729911636.csv")
geometricoRastrigin20 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_20_semilla_1729911637.csv")
geometricoRastrigin21 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_21_semilla_1729911638.csv")
geometricoRastrigin22 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_22_semilla_1729911639.csv")
geometricoRastrigin23 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_23_semilla_1729911640.csv")
geometricoRastrigin24 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_24_semilla_1729911641.csv")
geometricoRastrigin25 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_25_semilla_1729911642.csv")
geometricoRastrigin26 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_26_semilla_1729911643.csv")
geometricoRastrigin27 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_27_semilla_1729911644.csv")
geometricoRastrigin28 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_28_semilla_1729911645.csv")
geometricoRastrigin29 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_29_semilla_1729911646.csv")
geometricoRastrigin30 = pd.read_csv(base_6 + "Rastrigin_resultados_geometrico_30_semilla_1729911647.csv")
#%% Rastrigin Lineal
linealRastrigin1 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_1_semilla_1729911617.csv")
linealRastrigin2 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_2_semilla_1729911618.csv")
linealRastrigin3 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_3_semilla_1729911619.csv")
linealRastrigin4 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_4_semilla_1729911620.csv")
linealRastrigin5 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_5_semilla_1729911621.csv")
linealRastrigin6 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_6_semilla_1729911622.csv")
linealRastrigin7 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_7_semilla_1729911623.csv")
linealRastrigin8 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_8_semilla_1729911624.csv")
linealRastrigin9 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_9_semilla_1729911625.csv")
linealRastrigin10 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_10_semilla_1729911626.csv")
linealRastrigin11 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_11_semilla_1729911627.csv")
linealRastrigin12 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_12_semilla_1729911628.csv")
linealRastrigin13 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_13_semilla_1729911630.csv")
linealRastrigin14 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_14_semilla_1729911631.csv")
linealRastrigin15 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_15_semilla_1729911632.csv")
linealRastrigin16 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_16_semilla_1729911633.csv")
linealRastrigin17 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_17_semilla_1729911634.csv")
linealRastrigin18 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_18_semilla_1729911635.csv")
linealRastrigin19 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_19_semilla_1729911636.csv")
linealRastrigin20 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_20_semilla_1729911637.csv")
linealRastrigin21 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_21_semilla_1729911638.csv")
linealRastrigin22 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_22_semilla_1729911639.csv")
linealRastrigin23 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_23_semilla_1729911640.csv")
linealRastrigin24 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_24_semilla_1729911641.csv")
linealRastrigin25 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_25_semilla_1729911642.csv")
linealRastrigin26 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_26_semilla_1729911643.csv")
linealRastrigin27 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_27_semilla_1729911644.csv")
linealRastrigin28 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_28_semilla_1729911645.csv")
linealRastrigin29 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_29_semilla_1729911646.csv")
linealRastrigin30 = pd.read_csv(base_6 + "Rastrigin_resultados_lineal_30_semilla_1729911647.csv")


# URL base
base2 = "https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Rosenbrock/Rosenbrock_resultados_"

#  Rosenbrock remplazo elitista
elitismoRosenbrock10 = pd.read_csv(base2 + "elitismo_10_semilla_1729571599.csv")
elitismoRosenbrock11 = pd.read_csv(base2 + "elitismo_11_semilla_1729571601.csv")
elitismoRosenbrock12 = pd.read_csv(base2 + "elitismo_12_semilla_1729571602.csv")
elitismoRosenbrock13 = pd.read_csv(base2 + "elitismo_13_semilla_1729571603.csv")
elitismoRosenbrock14 = pd.read_csv(base2 + "elitismo_14_semilla_1729571604.csv")
elitismoRosenbrock15 = pd.read_csv(base2 + "elitismo_15_semilla_1729571606.csv")
elitismoRosenbrock16 = pd.read_csv(base2 + "elitismo_16_semilla_1729571607.csv")
elitismoRosenbrock17 = pd.read_csv(base2 + "elitismo_17_semilla_1729571608.csv")
elitismoRosenbrock18 = pd.read_csv(base2 + "elitismo_18_semilla_1729571610.csv")
elitismoRosenbrock19 = pd.read_csv(base2 + "elitismo_19_semilla_1729571611.csv")
elitismoRosenbrock1 = pd.read_csv(base2 + "elitismo_1_semilla_1729571588.csv")
elitismoRosenbrock20 = pd.read_csv(base2 + "elitismo_20_semilla_1729571612.csv")
elitismoRosenbrock21 = pd.read_csv(base2 + "elitismo_21_semilla_1729571613.csv")
elitismoRosenbrock22 = pd.read_csv(base2 + "elitismo_22_semilla_1729571615.csv")
elitismoRosenbrock23 = pd.read_csv(base2 + "elitismo_23_semilla_1729571616.csv")
elitismoRosenbrock24 = pd.read_csv(base2 + "elitismo_24_semilla_1729571617.csv")
elitismoRosenbrock25 = pd.read_csv(base2 + "elitismo_25_semilla_1729571618.csv")
elitismoRosenbrock26 = pd.read_csv(base2 + "elitismo_26_semilla_1729571620.csv")
elitismoRosenbrock27 = pd.read_csv(base2 + "elitismo_27_semilla_1729571621.csv")
elitismoRosenbrock28 = pd.read_csv(base2 + "elitismo_28_semilla_1729571622.csv")
elitismoRosenbrock29 = pd.read_csv(base2 + "elitismo_29_semilla_1729571624.csv")
elitismoRosenbrock2 = pd.read_csv(base2 + "elitismo_2_semilla_1729571589.csv")
elitismoRosenbrock30 = pd.read_csv(base2 + "elitismo_30_semilla_1729571625.csv")
elitismoRosenbrock3 = pd.read_csv(base2 + "elitismo_3_semilla_1729571591.csv")
elitismoRosenbrock4 = pd.read_csv(base2 + "elitismo_4_semilla_1729571592.csv")
elitismoRosenbrock5 = pd.read_csv(base2 + "elitismo_5_semilla_1729571593.csv")
elitismoRosenbrock6 = pd.read_csv(base2 + "elitismo_6_semilla_1729571594.csv")
elitismoRosenbrock7 = pd.read_csv(base2 + "elitismo_7_semilla_1729571596.csv")
elitismoRosenbrock8 = pd.read_csv(base2 + "elitismo_8_semilla_1729571597.csv")
elitismoRosenbrock9 = pd.read_csv(base2 + "elitismo_9_semilla_1729571598.csv")
#%%

# Rosenbrock remplazo generacional
generacionalRosenbrock10 = pd.read_csv(base2 + "generacional_10_semilla_1729572985.csv")
generacionalRosenbrock11 = pd.read_csv(base2 + "generacional_11_semilla_1729572986.csv")
generacionalRosenbrock12 = pd.read_csv(base2 + "generacional_12_semilla_1729572988.csv")
generacionalRosenbrock13 = pd.read_csv(base2 + "generacional_13_semilla_1729572989.csv")
generacionalRosenbrock14 = pd.read_csv(base2 + "generacional_14_semilla_1729572990.csv")
generacionalRosenbrock15 = pd.read_csv(base2 + "generacional_15_semilla_1729572992.csv")
generacionalRosenbrock16 = pd.read_csv(base2 + "generacional_16_semilla_1729572993.csv")
generacionalRosenbrock17 = pd.read_csv(base2 + "generacional_17_semilla_1729572994.csv")
generacionalRosenbrock18 = pd.read_csv(base2 + "generacional_18_semilla_1729572995.csv")
generacionalRosenbrock19 = pd.read_csv(base2 + "generacional_19_semilla_1729572997.csv")
generacionalRosenbrock1 = pd.read_csv(base2 + "generacional_1_semilla_1729572974.csv")
generacionalRosenbrock20 = pd.read_csv(base2 + "generacional_20_semilla_1729572998.csv")
generacionalRosenbrock21 = pd.read_csv(base2 + "generacional_21_semilla_1729572999.csv")
generacionalRosenbrock22 = pd.read_csv(base2 + "generacional_22_semilla_1729573001.csv")
generacionalRosenbrock23 = pd.read_csv(base2 + "generacional_23_semilla_1729573002.csv")
generacionalRosenbrock24 = pd.read_csv(base2 + "generacional_24_semilla_1729573003.csv")
generacionalRosenbrock25 = pd.read_csv(base2 + "generacional_25_semilla_1729573004.csv")
generacionalRosenbrock26 = pd.read_csv(base2 + "generacional_26_semilla_1729573006.csv")
generacionalRosenbrock27 = pd.read_csv(base2 + "generacional_27_semilla_1729573007.csv")
generacionalRosenbrock28 = pd.read_csv(base2 + "generacional_28_semilla_1729573008.csv")
generacionalRosenbrock29 = pd.read_csv(base2 + "generacional_29_semilla_1729573010.csv")
generacionalRosenbrock2 = pd.read_csv(base2 + "generacional_2_semilla_1729572975.csv")
generacionalRosenbrock30 = pd.read_csv(base2 + "generacional_30_semilla_1729573011.csv")
generacionalRosenbrock3 = pd.read_csv(base2 + "generacional_3_semilla_1729572976.csv")
generacionalRosenbrock4 = pd.read_csv(base2 + "generacional_4_semilla_1729572978.csv")
generacionalRosenbrock5 = pd.read_csv(base2 + "generacional_5_semilla_1729572979.csv")
generacionalRosenbrock6 = pd.read_csv(base2 + "generacional_6_semilla_1729572980.csv")
generacionalRosenbrock7 = pd.read_csv(base2 + "generacional_7_semilla_1729572981.csv")
generacionalRosenbrock8 = pd.read_csv(base2 + "generacional_8_semilla_1729572983.csv")
generacionalRosenbrock9 = pd.read_csv(base2 + "generacional_9_semilla_1729572984.csv")

#%%

# Rosenbrock remplazo peores
peoresRosenbrock10 = pd.read_csv(base2 + "peores_10_semilla_1729573392.csv")
peoresRosenbrock11 = pd.read_csv(base2 + "peores_11_semilla_1729573393.csv")
peoresRosenbrock12 = pd.read_csv(base2 + "peores_12_semilla_1729573394.csv")
peoresRosenbrock13 = pd.read_csv(base2 + "peores_13_semilla_1729573396.csv")
peoresRosenbrock14 = pd.read_csv(base2 + "peores_14_semilla_1729573397.csv")
peoresRosenbrock15 = pd.read_csv(base2 + "peores_15_semilla_1729573398.csv")
peoresRosenbrock16 = pd.read_csv(base2 + "peores_16_semilla_1729573400.csv")
peoresRosenbrock17 = pd.read_csv(base2 + "peores_17_semilla_1729573401.csv")
peoresRosenbrock18 = pd.read_csv(base2 + "peores_18_semilla_1729573402.csv")
peoresRosenbrock19 = pd.read_csv(base2 + "peores_19_semilla_1729573403.csv")
peoresRosenbrock1 = pd.read_csv(base2 + "peores_1_semilla_1729573381.csv")
peoresRosenbrock20 = pd.read_csv(base2 + "peores_20_semilla_1729573405.csv")
peoresRosenbrock21 = pd.read_csv(base2 + "peores_21_semilla_1729573406.csv")
peoresRosenbrock22 = pd.read_csv(base2 + "peores_22_semilla_1729573407.csv")
peoresRosenbrock23 = pd.read_csv(base2 + "peores_23_semilla_1729573409.csv")
peoresRosenbrock24 = pd.read_csv(base2 + "peores_24_semilla_1729573410.csv")
peoresRosenbrock25 = pd.read_csv(base2 + "peores_25_semilla_1729573411.csv")
peoresRosenbrock26 = pd.read_csv(base2 + "peores_26_semilla_1729573412.csv")
peoresRosenbrock27 = pd.read_csv(base2 + "peores_27_semilla_1729573414.csv")
peoresRosenbrock28 = pd.read_csv(base2 + "peores_28_semilla_1729573415.csv")
peoresRosenbrock29 = pd.read_csv(base2 + "peores_29_semilla_1729573416.csv")
peoresRosenbrock2 = pd.read_csv(base2 + "peores_2_semilla_1729573382.csv")
peoresRosenbrock30 = pd.read_csv(base2 + "peores_30_semilla_1729573418.csv")
peoresRosenbrock3 = pd.read_csv(base2 + "peores_3_semilla_1729573383.csv")
peoresRosenbrock4 = pd.read_csv(base2 + "peores_4_semilla_1729573384.csv")
peoresRosenbrock5 = pd.read_csv(base2 + "peores_5_semilla_1729573386.csv")
peoresRosenbrock6 = pd.read_csv(base2 + "peores_6_semilla_1729573387.csv")
peoresRosenbrock7 = pd.read_csv(base2 + "peores_7_semilla_1729573388.csv")
peoresRosenbrock8 = pd.read_csv(base2 + "peores_8_semilla_1729573389.csv")
peoresRosenbrock9 = pd.read_csv(base2 + "peores_9_semilla_1729573391.csv")
# Lineales y geometricos
# 
geometricoRosenbrock1 = pd.read_csv(base2 + "geometrico_1_semilla_1729912203.csv")
geometricoRosenbrock2 = pd.read_csv(base2 + "geometrico_2_semilla_1729912204.csv")
geometricoRosenbrock3 = pd.read_csv(base2 + "geometrico_3_semilla_1729912205.csv")
geometricoRosenbrock4 = pd.read_csv(base2 + "geometrico_4_semilla_1729912206.csv")
geometricoRosenbrock5 = pd.read_csv(base2 + "geometrico_5_semilla_1729912207.csv")
geometricoRosenbrock6 = pd.read_csv(base2 + "geometrico_6_semilla_1729912208.csv")
geometricoRosenbrock7 = pd.read_csv(base2 + "geometrico_7_semilla_1729912209.csv")
geometricoRosenbrock8 = pd.read_csv(base2 + "geometrico_8_semilla_1729912210.csv")
geometricoRosenbrock9 = pd.read_csv(base2 + "geometrico_9_semilla_1729912211.csv")
geometricoRosenbrock10 = pd.read_csv(base2 + "geometrico_10_semilla_1729912212.csv")
geometricoRosenbrock11 = pd.read_csv(base2 + "geometrico_11_semilla_1729912213.csv")
geometricoRosenbrock12 = pd.read_csv(base2 + "geometrico_12_semilla_1729912214.csv")
geometricoRosenbrock13 = pd.read_csv(base2 + "geometrico_13_semilla_1729912215.csv")
geometricoRosenbrock14 = pd.read_csv(base2 + "geometrico_14_semilla_1729912216.csv")
geometricoRosenbrock15 = pd.read_csv(base2 + "geometrico_15_semilla_1729912218.csv")
geometricoRosenbrock16 = pd.read_csv(base2 + "geometrico_16_semilla_1729912219.csv")
geometricoRosenbrock17 = pd.read_csv(base2 + "geometrico_17_semilla_1729912220.csv")
geometricoRosenbrock18 = pd.read_csv(base2 + "geometrico_18_semilla_1729912221.csv")
geometricoRosenbrock19 = pd.read_csv(base2 + "geometrico_19_semilla_1729912222.csv")
geometricoRosenbrock20 = pd.read_csv(base2 + "geometrico_20_semilla_1729912223.csv")
geometricoRosenbrock21 = pd.read_csv(base2 + "geometrico_21_semilla_1729912224.csv")
geometricoRosenbrock22 = pd.read_csv(base2 + "geometrico_22_semilla_1729912225.csv")
geometricoRosenbrock23 = pd.read_csv(base2 + "geometrico_23_semilla_1729912226.csv")
geometricoRosenbrock24 = pd.read_csv(base2 + "geometrico_24_semilla_1729912227.csv")
geometricoRosenbrock25 = pd.read_csv(base2 + "geometrico_25_semilla_1729912228.csv")
geometricoRosenbrock26 = pd.read_csv(base2 + "geometrico_26_semilla_1729912229.csv")
geometricoRosenbrock27 = pd.read_csv(base2 + "geometrico_27_semilla_1729912230.csv")
geometricoRosenbrock28 = pd.read_csv(base2 + "geometrico_28_semilla_1729912231.csv")
geometricoRosenbrock29 = pd.read_csv(base2 + "geometrico_29_semilla_1729912232.csv")
geometricoRosenbrock30 = pd.read_csv(base2 + "geometrico_30_semilla_1729912233.csv")

# Archivos Lineales
linealRosenbrock1 = pd.read_csv(base2 + "lineal_1_semilla_1729912203.csv")
linealRosenbrock2 = pd.read_csv(base2 + "lineal_2_semilla_1729912204.csv")
linealRosenbrock3 = pd.read_csv(base2 + "lineal_3_semilla_1729912205.csv")
linealRosenbrock4 = pd.read_csv(base2 + "lineal_4_semilla_1729912206.csv")
linealRosenbrock5 = pd.read_csv(base2 + "lineal_5_semilla_1729912207.csv")
linealRosenbrock6 = pd.read_csv(base2 + "lineal_6_semilla_1729912208.csv")
linealRosenbrock7 = pd.read_csv(base2 + "lineal_7_semilla_1729912209.csv")
linealRosenbrock8 = pd.read_csv(base2 + "lineal_8_semilla_1729912210.csv")
linealRosenbrock9 = pd.read_csv(base2 + "lineal_9_semilla_1729912211.csv")
linealRosenbrock10 = pd.read_csv(base2 + "lineal_10_semilla_1729912212.csv")
linealRosenbrock11 = pd.read_csv(base2 + "lineal_11_semilla_1729912213.csv")
linealRosenbrock12 = pd.read_csv(base2 + "lineal_12_semilla_1729912214.csv")
linealRosenbrock13 = pd.read_csv(base2 + "lineal_13_semilla_1729912215.csv")
linealRosenbrock14 = pd.read_csv(base2 + "lineal_14_semilla_1729912216.csv")
linealRosenbrock15 = pd.read_csv(base2 + "lineal_15_semilla_1729912217.csv")
linealRosenbrock16 = pd.read_csv(base2 + "lineal_16_semilla_1729912218.csv")
linealRosenbrock17 = pd.read_csv(base2 + "lineal_17_semilla_1729912219.csv")
linealRosenbrock18 = pd.read_csv(base2 + "lineal_18_semilla_1729912220.csv")
linealRosenbrock19 = pd.read_csv(base2 + "lineal_19_semilla_1729912221.csv")
linealRosenbrock20 = pd.read_csv(base2 + "lineal_20_semilla_1729912222.csv")
linealRosenbrock21 = pd.read_csv(base2 + "lineal_21_semilla_1729912223.csv")
linealRosenbrock22 = pd.read_csv(base2 + "lineal_22_semilla_1729912224.csv")
linealRosenbrock23 = pd.read_csv(base2 + "lineal_23_semilla_1729912225.csv")
linealRosenbrock24 = pd.read_csv(base2 + "lineal_24_semilla_1729912226.csv")
linealRosenbrock25 = pd.read_csv(base2 + "lineal_25_semilla_1729912227.csv")
linealRosenbrock26 = pd.read_csv(base2 + "lineal_26_semilla_1729912228.csv")
linealRosenbrock27 = pd.read_csv(base2 + "lineal_27_semilla_1729912229.csv")
linealRosenbrock28 = pd.read_csv(base2 + "lineal_28_semilla_1729912230.csv")
linealRosenbrock29 = pd.read_csv(base2 + "lineal_29_semilla_1729912231.csv")
linealRosenbrock30 = pd.read_csv(base2 + "lineal_30_semilla_1729912232.csv")


#%%

# URL base
base3 = "https://raw.githubusercontent.com/TomateTorres/C-mputo-Evolutivo-primeros-intentos/refs/heads/main/Tarea%205/Ejecuciones_Sphere/Sphere_resultados_"

# Sphere elitismo
elitismoSphere1 = pd.read_csv(base3 + "elitismo_1_semilla_1729572449.csv")
elitismoSphere2 = pd.read_csv(base3 + "elitismo_2_semilla_1729572461.csv")
elitismoSphere3 = pd.read_csv(base3 + "elitismo_3_semilla_1729572462.csv")
elitismoSphere4 = pd.read_csv(base3 + "elitismo_4_semilla_1729572463.csv")
elitismoSphere5 = pd.read_csv(base3 + "elitismo_5_semilla_1729572465.csv")
elitismoSphere6 = pd.read_csv(base3 + "elitismo_6_semilla_1729572466.csv")
elitismoSphere7 = pd.read_csv(base3 + "elitismo_7_semilla_1729572467.csv")
elitismoSphere8 = pd.read_csv(base3 + "elitismo_8_semilla_1729572468.csv")
elitismoSphere9 = pd.read_csv(base3 + "elitismo_9_semilla_1729572470.csv")
elitismoSphere10 = pd.read_csv(base3 + "elitismo_10_semilla_1729572471.csv")
elitismoSphere11 = pd.read_csv(base3 + "elitismo_11_semilla_1729572472.csv")
elitismoSphere12 = pd.read_csv(base3 + "elitismo_12_semilla_1729572474.csv")
elitismoSphere13 = pd.read_csv(base3 + "elitismo_13_semilla_1729572475.csv")
elitismoSphere14 = pd.read_csv(base3 + "elitismo_14_semilla_1729572476.csv")
elitismoSphere15 = pd.read_csv(base3 + "elitismo_15_semilla_1729572477.csv")
elitismoSphere16 = pd.read_csv(base3 + "elitismo_16_semilla_1729572479.csv")
elitismoSphere17 = pd.read_csv(base3 + "elitismo_17_semilla_1729572480.csv")
elitismoSphere18 = pd.read_csv(base3 + "elitismo_18_semilla_1729572481.csv")
elitismoSphere19 = pd.read_csv(base3 + "elitismo_19_semilla_1729572483.csv")
elitismoSphere20 = pd.read_csv(base3 + "elitismo_20_semilla_1729572484.csv")
elitismoSphere21 = pd.read_csv(base3 + "elitismo_21_semilla_1729572485.csv")
elitismoSphere22 = pd.read_csv(base3 + "elitismo_22_semilla_1729572486.csv")
elitismoSphere23 = pd.read_csv(base3 + "elitismo_23_semilla_1729572488.csv")
elitismoSphere24 = pd.read_csv(base3 + "elitismo_24_semilla_1729572489.csv")
elitismoSphere25 = pd.read_csv(base3 + "elitismo_25_semilla_1729572490.csv")
elitismoSphere26 = pd.read_csv(base3 + "elitismo_26_semilla_1729572491.csv")
elitismoSphere27 = pd.read_csv(base3 + "elitismo_27_semilla_1729572493.csv")
elitismoSphere28 = pd.read_csv(base3 + "elitismo_28_semilla_1729572494.csv")
elitismoSphere29 = pd.read_csv(base3 + "elitismo_29_semilla_1729572495.csv")
elitismoSphere30 = pd.read_csv(base3 + "elitismo_30_semilla_1729572497.csv")

# Sphere remplazo generacional
generacionalSphere1 = pd.read_csv(base3 + "generacional_1_semilla_1729573019.csv")
generacionalSphere2 = pd.read_csv(base3 + "generacional_2_semilla_1729573029.csv")
generacionalSphere3 = pd.read_csv(base3 + "generacional_3_semilla_1729573031.csv")
generacionalSphere4 = pd.read_csv(base3 + "generacional_4_semilla_1729573032.csv")
generacionalSphere5 = pd.read_csv(base3 + "generacional_5_semilla_1729573033.csv")
generacionalSphere6 = pd.read_csv(base3 + "generacional_6_semilla_1729573035.csv")
generacionalSphere7 = pd.read_csv(base3 + "generacional_7_semilla_1729573036.csv")
generacionalSphere8 = pd.read_csv(base3 + "generacional_8_semilla_1729573037.csv")
generacionalSphere9 = pd.read_csv(base3 + "generacional_9_semilla_1729573038.csv")
generacionalSphere10 = pd.read_csv(base3 + "generacional_10_semilla_1729573040.csv")
generacionalSphere11 = pd.read_csv(base3 + "generacional_11_semilla_1729573041.csv")
generacionalSphere12 = pd.read_csv(base3 + "generacional_12_semilla_1729573042.csv")
generacionalSphere13 = pd.read_csv(base3 + "generacional_13_semilla_1729573043.csv")
generacionalSphere14 = pd.read_csv(base3 + "generacional_14_semilla_1729573045.csv")
generacionalSphere15 = pd.read_csv(base3 + "generacional_15_semilla_1729573046.csv")
generacionalSphere16 = pd.read_csv(base3 + "generacional_16_semilla_1729573047.csv")
generacionalSphere17 = pd.read_csv(base3 + "generacional_17_semilla_1729573049.csv")
generacionalSphere18 = pd.read_csv(base3 + "generacional_18_semilla_1729573050.csv")
generacionalSphere19 = pd.read_csv(base3 + "generacional_19_semilla_1729573051.csv")
generacionalSphere20 = pd.read_csv(base3 + "generacional_20_semilla_1729573052.csv")
generacionalSphere21 = pd.read_csv(base3 + "generacional_21_semilla_1729573054.csv")
generacionalSphere22 = pd.read_csv(base3 + "generacional_22_semilla_1729573055.csv")
generacionalSphere23 = pd.read_csv(base3 + "generacional_23_semilla_1729573056.csv")
generacionalSphere24 = pd.read_csv(base3 + "generacional_24_semilla_1729573057.csv")
generacionalSphere25 = pd.read_csv(base3 + "generacional_25_semilla_1729573059.csv")
generacionalSphere26 = pd.read_csv(base3 + "generacional_26_semilla_1729573060.csv")
generacionalSphere27 = pd.read_csv(base3 + "generacional_27_semilla_1729573061.csv")
generacionalSphere28 = pd.read_csv(base3 + "generacional_28_semilla_1729573062.csv")
generacionalSphere29 = pd.read_csv(base3 + "generacional_29_semilla_1729573064.csv")
generacionalSphere30 = pd.read_csv(base3 + "generacional_30_semilla_1729573065.csv")

# Sphere remplazo peores
peoresSphere1 = pd.read_csv(base3 + "peores_1_semilla_1729573471.csv")
peoresSphere2 = pd.read_csv(base3 + "peores_2_semilla_1729573483.csv")
peoresSphere3 = pd.read_csv(base3 + "peores_3_semilla_1729573484.csv")
peoresSphere4 = pd.read_csv(base3 + "peores_4_semilla_1729573485.csv")
peoresSphere5 = pd.read_csv(base3 + "peores_5_semilla_1729573486.csv")
peoresSphere6 = pd.read_csv(base3 + "peores_6_semilla_1729573488.csv")
peoresSphere7 = pd.read_csv(base3 + "peores_7_semilla_1729573489.csv")
peoresSphere8 = pd.read_csv(base3 + "peores_8_semilla_1729573490.csv")
peoresSphere9 = pd.read_csv(base3 + "peores_9_semilla_1729573492.csv")
peoresSphere10 = pd.read_csv(base3 + "peores_10_semilla_1729573493.csv")
peoresSphere11 = pd.read_csv(base3 + "peores_11_semilla_1729573494.csv")
peoresSphere12 = pd.read_csv(base3 + "peores_12_semilla_1729573495.csv")
peoresSphere13 = pd.read_csv(base3 + "peores_13_semilla_1729573497.csv")
peoresSphere14 = pd.read_csv(base3 + "peores_14_semilla_1729573498.csv")
peoresSphere15 = pd.read_csv(base3 + "peores_15_semilla_1729573499.csv")
peoresSphere16 = pd.read_csv(base3 + "peores_16_semilla_1729573500.csv")
peoresSphere17 = pd.read_csv(base3 + "peores_17_semilla_1729573502.csv")
peoresSphere18 = pd.read_csv(base3 + "peores_18_semilla_1729573503.csv")
peoresSphere19 = pd.read_csv(base3 + "peores_19_semilla_1729573504.csv")
peoresSphere20 = pd.read_csv(base3 + "peores_20_semilla_1729573505.csv")
peoresSphere21 = pd.read_csv(base3 + "peores_21_semilla_1729573507.csv")
peoresSphere22 = pd.read_csv(base3 + "peores_22_semilla_1729573508.csv")
peoresSphere23 = pd.read_csv(base3 + "peores_23_semilla_1729573509.csv")
peoresSphere24 = pd.read_csv(base3 + "peores_24_semilla_1729573511.csv")
peoresSphere25 = pd.read_csv(base3 + "peores_25_semilla_1729573512.csv")
peoresSphere26 = pd.read_csv(base3 + "peores_26_semilla_1729573513.csv")
peoresSphere27 = pd.read_csv(base3 + "peores_27_semilla_1729573514.csv")
peoresSphere28 = pd.read_csv(base3 + "peores_28_semilla_1729573516.csv")
peoresSphere29 = pd.read_csv(base3 + "peores_29_semilla_1729573517.csv")
peoresSphere30 = pd.read_csv(base3 + "peores_30_semilla_1729573518.csv")


# Sphere Geométricos
geometricoSphere1 = pd.read_csv(base3 + "geometrico_1_semilla_1729912546.csv")
geometricoSphere2 = pd.read_csv(base3 + "geometrico_2_semilla_1729912547.csv")
geometricoSphere3 = pd.read_csv(base3 + "geometrico_3_semilla_1729912548.csv")
geometricoSphere4 = pd.read_csv(base3 + "geometrico_4_semilla_1729912549.csv")
geometricoSphere5 = pd.read_csv(base3 + "geometrico_5_semilla_1729912550.csv")
geometricoSphere6 = pd.read_csv(base3 + "geometrico_6_semilla_1729912551.csv")
geometricoSphere7 = pd.read_csv(base3 + "geometrico_7_semilla_1729912552.csv")
geometricoSphere8 = pd.read_csv(base3 + "geometrico_8_semilla_1729912553.csv")
geometricoSphere9 = pd.read_csv(base3 + "geometrico_9_semilla_1729912554.csv")
geometricoSphere10 = pd.read_csv(base3 + "geometrico_10_semilla_1729912555.csv")
geometricoSphere11 = pd.read_csv(base3 + "geometrico_11_semilla_1729912556.csv")
geometricoSphere12 = pd.read_csv(base3 + "geometrico_12_semilla_1729912557.csv")
geometricoSphere13 = pd.read_csv(base3 + "geometrico_13_semilla_1729912558.csv")
geometricoSphere14 = pd.read_csv(base3 + "geometrico_14_semilla_1729912559.csv")
geometricoSphere15 = pd.read_csv(base3 + "geometrico_15_semilla_1729912560.csv")
geometricoSphere16 = pd.read_csv(base3 + "geometrico_16_semilla_1729912561.csv")
geometricoSphere17 = pd.read_csv(base3 + "geometrico_17_semilla_1729912563.csv")
geometricoSphere18 = pd.read_csv(base3 + "geometrico_18_semilla_1729912564.csv")
geometricoSphere19 = pd.read_csv(base3 + "geometrico_19_semilla_1729912565.csv")
geometricoSphere20 = pd.read_csv(base3 + "geometrico_20_semilla_1729912566.csv")
geometricoSphere21 = pd.read_csv(base3 + "geometrico_21_semilla_1729912567.csv")
geometricoSphere22 = pd.read_csv(base3 + "geometrico_22_semilla_1729912568.csv")
geometricoSphere23 = pd.read_csv(base3 + "geometrico_23_semilla_1729912569.csv")
geometricoSphere24 = pd.read_csv(base3 + "geometrico_24_semilla_1729912570.csv")
geometricoSphere25 = pd.read_csv(base3 + "geometrico_25_semilla_1729912571.csv")
geometricoSphere26 = pd.read_csv(base3 + "geometrico_26_semilla_1729912572.csv")
geometricoSphere27 = pd.read_csv(base3 + "geometrico_27_semilla_1729912573.csv")
geometricoSphere28 = pd.read_csv(base3 + "geometrico_28_semilla_1729912574.csv")
geometricoSphere29 = pd.read_csv(base3 + "geometrico_29_semilla_1729912575.csv")
geometricoSphere30 = pd.read_csv(base3 + "geometrico_30_semilla_1729912576.csv")

# Sphere Lineales
linealSphere1 = pd.read_csv(base3 + "lineal_1_semilla_1729912546.csv")
linealSphere2 = pd.read_csv(base3 + "lineal_2_semilla_1729912547.csv")
linealSphere3 = pd.read_csv(base3 + "lineal_3_semilla_1729912548.csv")
linealSphere4 = pd.read_csv(base3 + "lineal_4_semilla_1729912549.csv")
linealSphere5 = pd.read_csv(base3 + "lineal_5_semilla_1729912550.csv")
linealSphere6 = pd.read_csv(base3 + "lineal_6_semilla_1729912551.csv")
linealSphere7 = pd.read_csv(base3 + "lineal_7_semilla_1729912552.csv")
linealSphere8 = pd.read_csv(base3 + "lineal_8_semilla_1729912553.csv")
linealSphere9 = pd.read_csv(base3 + "lineal_9_semilla_1729912554.csv")
linealSphere10 = pd.read_csv(base3 + "lineal_10_semilla_1729912555.csv")
linealSphere11 = pd.read_csv(base3 + "lineal_11_semilla_1729912556.csv")
linealSphere12 = pd.read_csv(base3 + "lineal_12_semilla_1729912557.csv")
linealSphere13 = pd.read_csv(base3 + "lineal_13_semilla_1729912558.csv")
linealSphere14 = pd.read_csv(base3 + "lineal_14_semilla_1729912559.csv")
linealSphere15 = pd.read_csv(base3 + "lineal_15_semilla_1729912560.csv")
linealSphere16 = pd.read_csv(base3 + "lineal_16_semilla_1729912561.csv")
linealSphere17 = pd.read_csv(base3 + "lineal_17_semilla_1729912562.csv")
linealSphere18 = pd.read_csv(base3 + "lineal_18_semilla_1729912563.csv")
linealSphere19 = pd.read_csv(base3 + "lineal_19_semilla_1729912564.csv")
linealSphere20 = pd.read_csv(base3 + "lineal_20_semilla_1729912565.csv")
linealSphere21 = pd.read_csv(base3 + "lineal_21_semilla_1729912566.csv")
linealSphere22 = pd.read_csv(base3 + "lineal_22_semilla_1729912567.csv")
linealSphere23 = pd.read_csv(base3 + "lineal_23_semilla_1729912568.csv")
linealSphere24 = pd.read_csv(base3 + "lineal_24_semilla_1729912569.csv")
linealSphere25 = pd.read_csv(base3 + "lineal_25_semilla_1729912570.csv")
linealSphere26 = pd.read_csv(base3 + "lineal_26_semilla_1729912571.csv")
linealSphere27 = pd.read_csv(base3 + "lineal_27_semilla_1729912572.csv")
linealSphere28 = pd.read_csv(base3 + "lineal_28_semilla_1729912573.csv")
linealSphere29 = pd.read_csv(base3 + "lineal_29_semilla_1729912574.csv")
linealSphere30 = pd.read_csv(base3 + "lineal_30_semilla_1729912575.csv")


#%%
# Ahora sumamos las 30 ejecuciones para el promedio
# Ackley Elitismo
Ackley_Elitismo =  [elitismoAckley1, elitismoAckley2, elitismoAckley3, elitismoAckley4, elitismoAckley5, elitismoAckley6, elitismoAckley7, elitismoAckley8, elitismoAckley9, elitismoAckley10,
                    elitismoAckley11, elitismoAckley12, elitismoAckley13, elitismoAckley14, elitismoAckley15, elitismoAckley16, elitismoAckley17, elitismoAckley18, elitismoAckley19, elitismoAckley20,
                    elitismoAckley21, elitismoAckley22, elitismoAckley23, elitismoAckley24, elitismoAckley25, elitismoAckley26, elitismoAckley27, elitismoAckley28, elitismoAckley29, elitismoAckley30,
                    
                    ]
Ackley_E = pd.DataFrame(sum(Ackley_Elitismo))/30

# Ackley Generacional
Ackley_Generacional =  [generacionalAckley1, generacionalAckley2, generacionalAckley3, generacionalAckley4, generacionalAckley5, generacionalAckley6, generacionalAckley7, generacionalAckley8, generacionalAckley9, generacionalAckley10,
                    generacionalAckley11, generacionalAckley12, generacionalAckley13, generacionalAckley14, generacionalAckley15, generacionalAckley16, generacionalAckley17, generacionalAckley18, generacionalAckley19, generacionalAckley20,
                    generacionalAckley21, generacionalAckley22, generacionalAckley23, generacionalAckley24, generacionalAckley25, generacionalAckley26, generacionalAckley27, generacionalAckley28, generacionalAckley29, generacionalAckley30,
                    
                    ]
Ackley_G = pd.DataFrame(sum(Ackley_Generacional))/30

#Ackley peores
Ackley_Peores =  [peoresAckley1, peoresAckley2, peoresAckley3, peoresAckley4, peoresAckley5, peoresAckley6, peoresAckley7, peoresAckley8, peoresAckley9, peoresAckley10,
                    peoresAckley11, peoresAckley12, peoresAckley13, peoresAckley14, peoresAckley15, peoresAckley16, peoresAckley17, peoresAckley18, peoresAckley19, peoresAckley20,
                    peoresAckley21, peoresAckley22, peoresAckley23, peoresAckley24, peoresAckley45, peoresAckley26, peoresAckley27, peoresAckley28, peoresAckley29, peoresAckley30,
                    
                    ]
Ackley_P = pd.DataFrame(sum(Ackley_Peores))/30

# Ackley Lineal
Ackley_lineal =  [linealAckley1, linealAckley2, linealAckley3, linealAckley4, linealAckley5, linealAckley6, linealAckley7, linealAckley8, linealAckley9, linealAckley10,
                    linealAckley11, linealAckley12, linealAckley13, linealAckley14, linealAckley15, linealAckley16, linealAckley17, linealAckley18, linealAckley19, linealAckley20,
                    linealAckley21, linealAckley22, linealAckley23, linealAckley24, linealAckley25, linealAckley26, linealAckley27, linealAckley28, linealAckley29, linealAckley30,
                    
                    ]
Ackley_L = pd.DataFrame(sum(Ackley_lineal))/30

Ackley_geometrico =  [geometricoAckley1, geometricoAckley2, geometricoAckley3, geometricoAckley4, geometricoAckley5, geometricoAckley6, geometricoAckley7, geometricoAckley8, geometricoAckley9, geometricoAckley10,
                    geometricoAckley11, geometricoAckley12, geometricoAckley13, geometricoAckley14, geometricoAckley15, geometricoAckley16, geometricoAckley17, geometricoAckley18, geometricoAckley19, geometricoAckley20,
                    geometricoAckley21, geometricoAckley22, geometricoAckley23, geometricoAckley24, geometricoAckley25, geometricoAckley26, geometricoAckley27, geometricoAckley28, geometricoAckley29, geometricoAckley30,
                    
                    ]
Ackley_GM = pd.DataFrame(sum(Ackley_geometrico))/30




#%% 
#Graficamos 
# Crear la figura y el eje
plt.figure(figsize=(20, 10))

# Graficar la primera columna de cada DataFrame
plt.plot(Ackley_E['MejorEval'], label='Remplazo elitista')
plt.plot(Ackley_G['MejorEval'], label='Remplazo Generacional')
plt.plot(Ackley_P['MejorEval'], label='Remplazo Peores')
plt.plot(Ackley_L['MejorEval'], label='Enfriamiento Lineal')
plt.plot(Ackley_GM['MejorEval'], label='Enfriamiento Geometrico')

# Agregar título y etiquetas
plt.title('Rendimiento promedio de diferentes esquemas en función Ackley')
plt.xlabel('Iteraciones')
plt.ylabel('Valores')
plt.legend()

# Mostrar el gráfico
plt.show()


#%%
# Ahora sumamos las 30 ejecuciones para el promedio
# Griewank Elitismo
Griewank_Elitismo =  [elitismoGriewank1, elitismoGriewank2, elitismoGriewank3, elitismoGriewank4, elitismoGriewank5, elitismoGriewank6, elitismoGriewank7, elitismoGriewank8, elitismoGriewank9, elitismoGriewank10,
                    elitismoGriewank11, elitismoGriewank12, elitismoGriewank13, elitismoGriewank14, elitismoGriewank15, elitismoGriewank16, elitismoGriewank17, elitismoGriewank18, elitismoGriewank19, elitismoGriewank20,
                    elitismoGriewank21, elitismoGriewank22, elitismoGriewank23, elitismoGriewank24, elitismoGriewank25, elitismoGriewank26, elitismoGriewank27, elitismoGriewank28, elitismoGriewank29, elitismoGriewank30,
                    
                    ]
Griewank_E = pd.DataFrame(sum(Griewank_Elitismo))/30

# Griewank Generacional
Griewank_Generacional =  [generacionalGriewank1, generacionalGriewank2, generacionalGriewank3, generacionalGriewank4, generacionalGriewank5, generacionalGriewank6, generacionalGriewank7, generacionalGriewank8, generacionalGriewank9, generacionalGriewank10,
                    generacionalGriewank11, generacionalGriewank12, generacionalGriewank13, generacionalGriewank14, generacionalGriewank15, generacionalGriewank16, generacionalGriewank17, generacionalGriewank18, generacionalGriewank19, generacionalGriewank20,
                    generacionalGriewank21, generacionalGriewank22, generacionalGriewank23, generacionalGriewank24, generacionalGriewank25, generacionalGriewank26, generacionalGriewank27, generacionalGriewank28, generacionalGriewank29, generacionalGriewank30,
                    
                    ]
Griewank_G = pd.DataFrame(sum(Griewank_Generacional))/30

# Griewank peores
Griewank_Peores =  [peoresGriewank1, peoresGriewank2, peoresGriewank3, peoresGriewank4, peoresGriewank5, peoresGriewank6, peoresGriewank7, peoresGriewank8, peoresGriewank9, peoresGriewank10,
                    peoresGriewank11, peoresGriewank12, peoresGriewank13, peoresGriewank14, peoresGriewank15, peoresGriewank16, peoresGriewank17, peoresGriewank18, peoresGriewank19, peoresGriewank20,
                    peoresGriewank21, peoresGriewank22, peoresGriewank23, peoresGriewank24, peoresGriewank25, peoresGriewank26, peoresGriewank27, peoresGriewank28, peoresGriewank29, peoresGriewank30,
                    
                    ]
Griewank_P = pd.DataFrame(sum(Griewank_Peores))/30

# Griewank Lineal
Griewank_lineal =  [linealGriewank1, linealGriewank2, linealGriewank3, linealGriewank4, linealGriewank5, linealGriewank6, linealGriewank7, linealGriewank8, linealGriewank9, linealGriewank10,
                    linealGriewank11, linealGriewank12, linealGriewank13, linealGriewank14, linealGriewank15, linealGriewank16, linealGriewank17, linealGriewank18, linealGriewank19, linealGriewank20,
                    linealGriewank21, linealGriewank22, linealGriewank23, linealGriewank24, linealGriewank25, linealGriewank26, linealGriewank27, linealGriewank28, linealGriewank29, linealGriewank30,
                    
                    ]
Griewank_L = pd.DataFrame(sum(Griewank_lineal))/30

Griewank_geometrico =  [geometricoGriewank1, geometricoGriewank2, geometricoGriewank3, geometricoGriewank4, geometricoGriewank5, geometricoGriewank6, geometricoGriewank7, geometricoGriewank8, geometricoGriewank9, geometricoGriewank10,
                    geometricoGriewank11, geometricoGriewank12, geometricoGriewank13, geometricoGriewank14, geometricoGriewank15, geometricoGriewank16, geometricoGriewank17, geometricoGriewank18, geometricoGriewank19, geometricoGriewank20,
                    geometricoGriewank21, geometricoGriewank22, geometricoGriewank23, geometricoGriewank24, geometricoGriewank25, geometricoGriewank26, geometricoGriewank27, geometricoGriewank28, geometricoGriewank29, geometricoGriewank30,
                    
                    ]
Griewank_GM = pd.DataFrame(sum(Griewank_geometrico))/30

#%% 
#Graficamos 
# Crear la figura y el eje
plt.figure(figsize=(20, 10))

# Graficar la primera columna de cada DataFrame
plt.plot(Griewank_E['MejorEval'], label='Remplazo elitista')
plt.plot(Griewank_G['MejorEval'], label='Remplazo Generacional')
plt.plot(Griewank_P['MejorEval'], label='Remplazo Peores')
plt.plot(Griewank_L['MejorEval'], label='Enfriamiento Lineal')
plt.plot(Griewank_GM['MejorEval'], label='Enfriamiento Geometrico')

# Agregar título y etiquetas
plt.title('Rendimiento promedio de diferentes esquemas en función Griewank')
plt.xlabel('Iteraciones')
plt.ylabel('Valores')
plt.legend()

# Mostrar el gráfico
plt.show()

#%%
# Ahora sumamos las 30 ejecuciones para el promedio
# Rastrigin Elitismo
Rastrigin_Elitismo =  [elitismoRastrigin1, elitismoRastrigin2, elitismoRastrigin3, elitismoRastrigin4, elitismoRastrigin5, elitismoRastrigin6, elitismoRastrigin7, elitismoRastrigin8, elitismoRastrigin9, elitismoRastrigin10,
                    elitismoRastrigin11, elitismoRastrigin12, elitismoRastrigin13, elitismoRastrigin14, elitismoRastrigin15, elitismoRastrigin16, elitismoRastrigin17, elitismoRastrigin18, elitismoRastrigin19, elitismoRastrigin20,
                    elitismoRastrigin21, elitismoRastrigin22, elitismoRastrigin23, elitismoRastrigin24, elitismoRastrigin25, elitismoRastrigin26, elitismoRastrigin27, elitismoRastrigin28, elitismoRastrigin29, elitismoRastrigin30,
                    
                    ]
Rastrigin_E = pd.DataFrame(sum(Rastrigin_Elitismo))/30

# Rastrigin Generacional
Rastrigin_Generacional =  [generacionalRastrigin1, generacionalRastrigin2, generacionalRastrigin3, generacionalRastrigin4, generacionalRastrigin5, generacionalRastrigin6, generacionalRastrigin7, generacionalRastrigin8, generacionalRastrigin9, generacionalRastrigin10,
                    generacionalRastrigin11, generacionalRastrigin12, generacionalRastrigin13, generacionalRastrigin14, generacionalRastrigin15, generacionalRastrigin16, generacionalRastrigin17, generacionalRastrigin18, generacionalRastrigin19, generacionalRastrigin20,
                    generacionalRastrigin21, generacionalRastrigin22, generacionalRastrigin23, generacionalRastrigin24, generacionalRastrigin25, generacionalRastrigin26, generacionalRastrigin27, generacionalRastrigin28, generacionalRastrigin29, generacionalRastrigin30,
                    
                    ]
Rastrigin_G = pd.DataFrame(sum(Rastrigin_Generacional))/30

# Rastrigin peores
Rastrigin_Peores =  [peoresRastrigin1, peoresRastrigin2, peoresRastrigin3, peoresRastrigin4, peoresRastrigin5, peoresRastrigin6, peoresRastrigin7, peoresRastrigin8, peoresRastrigin9, peoresRastrigin10,
                    peoresRastrigin11, peoresRastrigin12, peoresRastrigin13, peoresRastrigin14, peoresRastrigin15, peoresRastrigin16, peoresRastrigin17, peoresRastrigin18, peoresRastrigin19, peoresRastrigin20,
                    peoresRastrigin21, peoresRastrigin22, peoresRastrigin23, peoresRastrigin24, peoresRastrigin25, peoresRastrigin26, peoresRastrigin27, peoresRastrigin28, peoresRastrigin29, peoresRastrigin30,
                    
                    ]
Rastrigin_P = pd.DataFrame(sum(Rastrigin_Peores))/30

# Rastrigin Lineal
Rastrigin_lineal =  [linealRastrigin1, linealRastrigin2, linealRastrigin3, linealRastrigin4, linealRastrigin5, linealRastrigin6, linealRastrigin7, linealRastrigin8, linealRastrigin9, linealRastrigin10,
                    linealRastrigin11, linealRastrigin12, linealRastrigin13, linealRastrigin14, linealRastrigin15, linealRastrigin16, linealRastrigin17, linealRastrigin18, linealRastrigin19, linealRastrigin20,
                    linealRastrigin21, linealRastrigin22, linealRastrigin23, linealRastrigin24, linealRastrigin25, linealRastrigin26, linealRastrigin27, linealRastrigin28, linealRastrigin29, linealRastrigin30,
                    
                    ]
Rastrigin_L = pd.DataFrame(sum(Rastrigin_lineal))/30

Rastrigin_geometrico =  [geometricoRastrigin1, geometricoRastrigin2, geometricoRastrigin3, geometricoRastrigin4, geometricoRastrigin5, geometricoRastrigin6, geometricoRastrigin7, geometricoRastrigin8, geometricoRastrigin9, geometricoRastrigin10,
                    geometricoRastrigin11, geometricoRastrigin12, geometricoRastrigin13, geometricoRastrigin14, geometricoRastrigin15, geometricoRastrigin16, geometricoRastrigin17, geometricoRastrigin18, geometricoRastrigin19, geometricoRastrigin20,
                    geometricoRastrigin21, geometricoRastrigin22, geometricoRastrigin23, geometricoRastrigin24, geometricoRastrigin25, geometricoRastrigin26, geometricoRastrigin27, geometricoRastrigin28, geometricoRastrigin29, geometricoRastrigin30,
                    
                    ]
Rastrigin_GM = pd.DataFrame(sum(Rastrigin_geometrico))/30

#%% 
#Graficamos 
# Crear la figura y el eje
plt.figure(figsize=(20, 10))

# Graficar la primera columna de cada DataFrame
plt.plot(Rastrigin_E['MejorEval'], label='Remplazo elitista')
plt.plot(Rastrigin_G['MejorEval'], label='Remplazo Generacional')
plt.plot(Rastrigin_P['MejorEval'], label='Remplazo Peores')

plt.plot(Rastrigin_L['MejorEval'], label='Enfriamiento Lineal')
plt.plot(Rastrigin_GM['MejorEval'], label='Enfriamiento Geometrico')


# Agregar título y etiquetas
plt.title('Rendimiento promedio de diferentes esquemas en función Rastrigin')
plt.xlabel('Iteraciones')
plt.ylabel('Valores')
plt.legend()

# Mostrar el gráfico
plt.show()

#%%
# Ahora sumamos las 30 ejecuciones para el promedio
# Rosenbrock Elitismo
Rosenbrock_Elitismo =  [elitismoRosenbrock1, elitismoRosenbrock2, elitismoRosenbrock3, elitismoRosenbrock4, elitismoRosenbrock5, elitismoRosenbrock6, elitismoRosenbrock7, elitismoRosenbrock8, elitismoRosenbrock9, elitismoRosenbrock10,
                    elitismoRosenbrock11, elitismoRosenbrock12, elitismoRosenbrock13, elitismoRosenbrock14, elitismoRosenbrock15, elitismoRosenbrock16, elitismoRosenbrock17, elitismoRosenbrock18, elitismoRosenbrock19, elitismoRosenbrock20,
                    elitismoRosenbrock21, elitismoRosenbrock22, elitismoRosenbrock23, elitismoRosenbrock24, elitismoRosenbrock25, elitismoRosenbrock26, elitismoRosenbrock27, elitismoRosenbrock28, elitismoRosenbrock29, elitismoRosenbrock30,
                    
                    ]
Rosenbrock_E = pd.DataFrame(sum(Rosenbrock_Elitismo))/30

# Rosenbrock Generacional
Rosenbrock_Generacional =  [generacionalRosenbrock1, generacionalRosenbrock2, generacionalRosenbrock3, generacionalRosenbrock4, generacionalRosenbrock5, generacionalRosenbrock6, generacionalRosenbrock7, generacionalRosenbrock8, generacionalRosenbrock9, generacionalRosenbrock10,
                    generacionalRosenbrock11, generacionalRosenbrock12, generacionalRosenbrock13, generacionalRosenbrock14, generacionalRosenbrock15, generacionalRosenbrock16, generacionalRosenbrock17, generacionalRosenbrock18, generacionalRosenbrock19, generacionalRosenbrock20,
                    generacionalRosenbrock21, generacionalRosenbrock22, generacionalRosenbrock23, generacionalRosenbrock24, generacionalRosenbrock25, generacionalRosenbrock26, generacionalRosenbrock27, generacionalRosenbrock28, generacionalRosenbrock29, generacionalRosenbrock30,
                    
                    ]
Rosenbrock_G = pd.DataFrame(sum(Rosenbrock_Generacional))/30

# Rosenbrock peores
Rosenbrock_Peores =  [peoresRosenbrock1, peoresRosenbrock2, peoresRosenbrock3, peoresRosenbrock4, peoresRosenbrock5, peoresRosenbrock6, peoresRosenbrock7, peoresRosenbrock8, peoresRosenbrock9, peoresRosenbrock10,
                    peoresRosenbrock11, peoresRosenbrock12, peoresRosenbrock13, peoresRosenbrock14, peoresRosenbrock15, peoresRosenbrock16, peoresRosenbrock17, peoresRosenbrock18, peoresRosenbrock19, peoresRosenbrock20,
                    peoresRosenbrock21, peoresRosenbrock22, peoresRosenbrock23, peoresRosenbrock24, peoresRosenbrock25, peoresRosenbrock26, peoresRosenbrock27, peoresRosenbrock28, peoresRosenbrock29, peoresRosenbrock30,
                    
                    ]
Rosenbrock_P = pd.DataFrame(sum(Rosenbrock_Peores))/30

# Rosenbrock Lineal
Rosenbrock_lineal =  [linealRosenbrock1, linealRosenbrock2, linealRosenbrock3, linealRosenbrock4, linealRosenbrock5, linealRosenbrock6, linealRosenbrock7, linealRosenbrock8, linealRosenbrock9, linealRosenbrock10,
                    linealRosenbrock11, linealRosenbrock12, linealRosenbrock13, linealRosenbrock14, linealRosenbrock15, linealRosenbrock16, linealRosenbrock17, linealRosenbrock18, linealRosenbrock19, linealRosenbrock20,
                    linealRosenbrock21, linealRosenbrock22, linealRosenbrock23, linealRosenbrock24, linealRosenbrock25, linealRosenbrock26, linealRosenbrock27, linealRosenbrock28, linealRosenbrock29, linealRosenbrock30,
                    
                    ]
Rosenbrock_L = pd.DataFrame(sum(Rosenbrock_lineal))/30

Rosenbrock_geometrico =  [geometricoRosenbrock1, geometricoRosenbrock2, geometricoRosenbrock3, geometricoRosenbrock4, geometricoRosenbrock5, geometricoRosenbrock6, geometricoRosenbrock7, geometricoRosenbrock8, geometricoRosenbrock9, geometricoRosenbrock10,
                    geometricoRosenbrock11, geometricoRosenbrock12, geometricoRosenbrock13, geometricoRosenbrock14, geometricoRosenbrock15, geometricoRosenbrock16, geometricoRosenbrock17, geometricoRosenbrock18, geometricoRosenbrock19, geometricoRosenbrock20,
                    geometricoRosenbrock21, geometricoRosenbrock22, geometricoRosenbrock23, geometricoRosenbrock24, geometricoRosenbrock25, geometricoRosenbrock26, geometricoRosenbrock27, geometricoRosenbrock28, geometricoRosenbrock29, geometricoRosenbrock30,
                    
                    ]
Rosenbrock_GM = pd.DataFrame(sum(Rosenbrock_geometrico))/30


#%% 
#Graficamos 
# Crear la figura y el eje
plt.figure(figsize=(20, 10))

# Graficar la primera columna de cada DataFrame
plt.plot(Rosenbrock_E['MejorEval'], label='Remplazo elitista')
plt.plot(Rosenbrock_G['MejorEval'], label='Remplazo Generacional')
plt.plot(Rosenbrock_P['MejorEval'], label='Remplazo Peores')
plt.plot(Rosenbrock_L['MejorEval'], label='Enfriamiento Lineal')
plt.plot(Rosenbrock_GM['MejorEval'], label='Enfriamiento Geometrico')

# Agregar título y etiquetas
plt.title('Rendimiento promedio de diferentes esquemas en función Rosenbrock')
plt.xlabel('Iteraciones')
plt.ylabel('Valores')
plt.legend()

# Mostrar el gráfico
plt.show()

# %%
#%%
# Ahora sumamos las 30 ejecuciones para el promedio
# Sphere Elitismo
Sphere_Elitismo =  [elitismoSphere1, elitismoSphere2, elitismoSphere3, elitismoSphere4, elitismoSphere5, elitismoSphere6, elitismoSphere7, elitismoSphere8, elitismoSphere9, elitismoSphere10,
                    elitismoSphere11, elitismoSphere12, elitismoSphere13, elitismoSphere14, elitismoSphere15, elitismoSphere16, elitismoSphere17, elitismoSphere18, elitismoSphere19, elitismoSphere20,
                    elitismoSphere21, elitismoSphere22, elitismoSphere23, elitismoSphere24, elitismoSphere25, elitismoSphere26, elitismoSphere27, elitismoSphere28, elitismoSphere29, elitismoSphere30,
                    
                    ]
Sphere_E = pd.DataFrame(sum(Sphere_Elitismo))/30

# Sphere Generacional
Sphere_Generacional =  [generacionalSphere1, generacionalSphere2, generacionalSphere3, generacionalSphere4, generacionalSphere5, generacionalSphere6, generacionalSphere7, generacionalSphere8, generacionalSphere9, generacionalSphere10,
                    generacionalSphere11, generacionalSphere12, generacionalSphere13, generacionalSphere14, generacionalSphere15, generacionalSphere16, generacionalSphere17, generacionalSphere18, generacionalSphere19, generacionalSphere20,
                    generacionalSphere21, generacionalSphere22, generacionalSphere23, generacionalSphere24, generacionalSphere25, generacionalSphere26, generacionalSphere27, generacionalSphere28, generacionalSphere29, generacionalSphere30,
                    
                    ]
Sphere_G = pd.DataFrame(sum(Sphere_Generacional))/30

# Sphere peores
Sphere_Peores =  [peoresSphere1, peoresSphere2, peoresSphere3, peoresSphere4, peoresSphere5, peoresSphere6, peoresSphere7, peoresSphere8, peoresSphere9, peoresSphere10,
                    peoresSphere11, peoresSphere12, peoresSphere13, peoresSphere14, peoresSphere15, peoresSphere16, peoresSphere17, peoresSphere18, peoresSphere19, peoresSphere20,
                    peoresSphere21, peoresSphere22, peoresSphere23, peoresSphere24, peoresSphere25, peoresSphere26, peoresSphere27, peoresSphere28, peoresSphere29, peoresSphere30,
                    
                    ]
Sphere_P = pd.DataFrame(sum(Sphere_Peores))/30

# Sphere Lineal
Sphere_lineal =  [linealSphere1, linealSphere2, linealSphere3, linealSphere4, linealSphere5, linealSphere6, linealSphere7, linealSphere8, linealSphere9, linealSphere10,
                    linealSphere11, linealSphere12, linealSphere13, linealSphere14, linealSphere15, linealSphere16, linealSphere17, linealSphere18, linealSphere19, linealSphere20,
                    linealSphere21, linealSphere22, linealSphere23, linealSphere24, linealSphere25, linealSphere26, linealSphere27, linealSphere28, linealSphere29, linealSphere30,
                    
                    ]
Sphere_L = pd.DataFrame(sum(Sphere_lineal))/30

Sphere_geometrico =  [geometricoSphere1, geometricoSphere2, geometricoSphere3, geometricoSphere4, geometricoSphere5, geometricoSphere6, geometricoSphere7, geometricoSphere8, geometricoSphere9, geometricoSphere10,
                    geometricoSphere11, geometricoSphere12, geometricoSphere13, geometricoSphere14, geometricoSphere15, geometricoSphere16, geometricoSphere17, geometricoSphere18, geometricoSphere19, geometricoSphere20,
                    geometricoSphere21, geometricoSphere22, geometricoSphere23, geometricoSphere24, geometricoSphere25, geometricoSphere26, geometricoSphere27, geometricoSphere28, geometricoSphere29, geometricoSphere30,
                    
                    ]
Sphere_GM = pd.DataFrame(sum(Sphere_geometrico))/30

#%% 
#Graficamos 
# Crear la figura y el eje
plt.figure(figsize=(20, 10))

# Graficar la primera columna de cada DataFrame
plt.plot(Sphere_E['MejorEval'], label='Remplazo elitista')
plt.plot(Sphere_G['MejorEval'], label='Remplazo Generacional')
plt.plot(Sphere_P['MejorEval'], label='Remplazo Peores')
plt.plot(Sphere_L['MejorEval'], label='Enfriamiento Lineal')
plt.plot(Sphere_GM['MejorEval'], label='Enfriamiento Geometrico')

# Agregar título y etiquetas
plt.title('Rendimiento promedio de diferentes esquemas en función Sphere')
plt.xlabel('Iteraciones')
plt.ylabel('Valores')
plt.legend()

# Mostrar el gráfico
plt.show()

# %%
# Veamos de todas
fig, axes = plt.subplots(5, 5, figsize=(25, 20))
# Graficar cada DataFrame para cada función y esquema
# Función Sphere
axes[0, 0].plot(Sphere_E['MejorEval'], label='Mejor', marker='o')
axes[0, 0].plot(Sphere_E['PromedioEval'], label='Promedio', marker='*')
axes[0, 0].set_title('Sphere - Elitista')
axes[0, 0].legend(loc='upper right')

axes[0, 1].plot(Sphere_G['MejorEval'], label='Mejor', marker='o')
axes[0, 1].plot(Sphere_G['PromedioEval'], label='Promedio', marker='*')
axes[0, 1].set_title('Sphere - Generacional')
axes[0, 1].legend(loc='upper right')

axes[0, 2].plot(Sphere_P['MejorEval'], label='Mejor', marker='o')
axes[0, 2].plot(Sphere_P['PromedioEval'], label='Promedio', marker='*')
axes[0, 2].set_title('Sphere - Peores')
axes[0, 2].legend(loc='upper right')

axes[0, 3].plot(Sphere_L['MejorEval'], label='Mejor', marker='o')
axes[0, 3].plot(Sphere_L['SolActiva'], label='Activa', marker='*')
axes[0, 3].set_title('Sphere - Enfriamiento Lineal')
axes[0, 3].legend(loc='upper right')

axes[0, 4].plot(Sphere_GM['MejorEval'], label='Mejor', marker='o')
axes[0, 4].plot(Sphere_GM['SolActiva'], label='Activa', marker='*')
axes[0, 4].set_title('Sphere - Geométrico')
axes[0, 4].legend(loc='upper right')

# Función Ackley
axes[1, 0].plot(Ackley_E['MejorEval'], label='Mejor', marker='o')
axes[1, 0].plot(Ackley_E['PromedioEval'], label='Promedio', marker='*')
axes[1, 0].set_title('Ackley - Elitista')
axes[1, 0].legend(loc='upper right')

axes[1, 1].plot(Ackley_G['MejorEval'], label='Mejor', marker='o')
axes[1, 1].plot(Ackley_G['PromedioEval'], label='Promedio', marker='*')
axes[1, 1].set_title('Ackley - Generacional')
axes[1, 1].legend(loc='upper right')

axes[1, 2].plot(Ackley_P['MejorEval'], label='Mejor', marker='o')
axes[1, 2].plot(Ackley_P['PromedioEval'], label='Promedio', marker='*')
axes[1, 2].set_title('Ackley - Peores')
axes[1, 2].legend(loc='upper right')

axes[1, 3].plot(Ackley_L['MejorEval'], label='Mejor', marker='o')
axes[1, 3].plot(Ackley_L['SolActiva'], label='Activa', marker='*')
axes[1, 3].set_title('Ackley - Enfriamiento Lineal')
axes[1, 3].legend(loc='upper right')

axes[1, 4].plot(Ackley_GM['MejorEval'], label='Mejor', marker='o')
axes[1, 4].plot(Ackley_GM['SolActiva'], label='Activa', marker='*')
axes[1, 4].set_title('Ackley - Geométrico')
axes[1, 4].legend(loc='upper right')

# Función Griewank
axes[2, 0].plot(Griewank_E['MejorEval'], label='Mejor', marker='o')
axes[2, 0].plot(Griewank_E['PromedioEval'], label='Promedio', marker='*')
axes[2, 0].set_title('Griewank - Elitista')
axes[2, 0].legend(loc='upper right')

axes[2, 1].plot(Griewank_G['MejorEval'], label='Mejor', marker='o')
axes[2, 1].plot(Griewank_G['PromedioEval'], label='Promedio', marker='*')
axes[2, 1].set_title('Griewank - Generacional')
axes[2, 1].legend(loc='upper right')

axes[2, 2].plot(Griewank_P['MejorEval'], label='Mejor', marker='o')
axes[2, 2].plot(Griewank_P['PromedioEval'], label='Promedio', marker='*')
axes[2, 2].set_title('Griewank - Peores')
axes[2, 2].legend(loc='upper right')

axes[2, 3].plot(Griewank_L['MejorEval'], label='Mejor', marker='o')
axes[2, 3].plot(Griewank_L['SolActiva'], label='Activa', marker='*')
axes[2, 3].set_title('Griewank - Enfriamiento Lineal')
axes[2, 3].legend(loc='upper right')

axes[2, 4].plot(Griewank_GM['MejorEval'], label='Mejor', marker='o')
axes[2, 4].plot(Griewank_GM['SolActiva'], label='Activa', marker='*')
axes[2, 4].set_title('Griewank - Geométrico')
axes[2, 4].legend(loc='upper right')

# Función Rastrigin
axes[3, 0].plot(Rastrigin_E['MejorEval'], label='Mejor', marker='o')
axes[3, 0].plot(Rastrigin_E['PromedioEval'], label='Promedio', marker='*')
axes[3, 0].set_title('Rastrigin - Elitista')
axes[3, 0].legend(loc='upper right')

axes[3, 1].plot(Rastrigin_G['MejorEval'], label='Mejor', marker='o')
axes[3, 1].plot(Rastrigin_G['PromedioEval'], label='Promedio', marker='*')
axes[3, 1].set_title('Rastrigin - Generacional')
axes[3, 1].legend(loc='upper right')

axes[3, 2].plot(Rastrigin_P['MejorEval'], label='Mejor', marker='o')
axes[3, 2].plot(Rastrigin_P['PromedioEval'], label='Promedio', marker='*')
axes[3, 2].set_title('Rastrigin - Peores')
axes[3, 2].legend(loc='upper right')

axes[3, 3].plot(Rastrigin_L['MejorEval'], label='Mejor', marker='o')
axes[3, 3].plot(Rastrigin_L['SolActiva'], label='Activa', marker='*')
axes[3, 3].set_title('Rastrigin - Enfriamiento Lineal')
axes[3, 3].legend(loc='upper right')

axes[3, 4].plot(Rastrigin_GM['MejorEval'], label='Mejor', marker='o')
axes[3, 4].plot(Rastrigin_GM['SolActiva'], label='Activa', marker='*')
axes[3, 4].set_title('Rastrigin - Geométrico')
axes[3, 4].legend(loc='upper right')

# Función Rosenbrock
axes[4, 0].plot(Rosenbrock_E['MejorEval'], label='Mejor', marker='o')
axes[4, 0].plot(Rosenbrock_E['PromedioEval'], label='Promedio', marker='*')
axes[4, 0].set_title('Rosenbrock - Elitista')
axes[4, 0].legend(loc='upper right')

axes[4, 1].plot(Rosenbrock_G['MejorEval'], label='Mejor', marker='o')
axes[4, 1].plot(Rosenbrock_G['PromedioEval'], label='Promedio', marker='*')
axes[4, 1].set_title('Rosenbrock - Generacional')
axes[4, 1].legend(loc='upper right')

axes[4, 2].plot(Rosenbrock_P['MejorEval'], label='Mejor', marker='o')
axes[4, 2].plot(Rosenbrock_P['PromedioEval'], label='Promedio', marker='*')
axes[4, 2].set_title('Rosenbrock - Peores')
axes[4, 2].legend(loc='upper right')

axes[4, 3].plot(Rosenbrock_L['MejorEval'], label='Mejor', marker='o')
axes[4, 3].plot(Rosenbrock_L['SolActiva'], label='Activa', marker='*')
axes[4, 3].set_title('Rosenbrock - Enfriamiento Lineal')
axes[4, 3].legend(loc='upper right')

axes[4, 4].plot(Rosenbrock_GM['MejorEval'], label='Mejor', marker='o')
axes[4, 4].plot(Rosenbrock_GM['SolActiva'], label='Activa', marker='*')
axes[4, 4].set_title('Rosenbrock - Geométrico')
axes[4, 4].legend(loc='upper right')

fig.suptitle('Comparación del Promedio por Función', fontsize=40)

#%%
import statistics
# %%
# Vamos a sacar medidas de tendencia central para las funciones
# Ackley Lineal, últimas ejecuciones (son los mejores valores a los que se llegaron)
# O sea a lo que convergieron esas 30 evaluaciones
mejorEval_AL = [df['MejorEval'].iloc[-1] for df in Ackley_lineal]
mejorEval_AG = [df['MejorEval'].iloc[-1] for df in Ackley_geometrico]
# Lo mismo con Griewank 
mejorEval_GL = [df['MejorEval'].iloc[-1] for df in Griewank_lineal]
mejorEval_GG = [df['MejorEval'].iloc[-1] for df in Griewank_geometrico]
# Rosenbrock
mejorEval_RL = [df['MejorEval'].iloc[-1] for df in Rosenbrock_lineal]
mejorEval_RG = [df['MejorEval'].iloc[-1] for df in Rosenbrock_geometrico]
# Rastrigin
mejorEval_NL = [df['MejorEval'].iloc[-1] for df in Rastrigin_lineal]
mejorEval_NG = [df['MejorEval'].iloc[-1] for df in Rastrigin_geometrico]
# Sphere
mejorEval_SL = [df['MejorEval'].iloc[-1] for df in Sphere_lineal]
mejorEval_SG = [df['MejorEval'].iloc[-1] for df in Sphere_geometrico]
# %%

funciones = {'Sphere Lineal': mejorEval_SL,
            'Sphere Geometrico': mejorEval_SG,
            'Ackley Lineal': mejorEval_AL,
            'Ackley Geometrico': mejorEval_AG,
            'Griewank Lineal': mejorEval_GL,
            'Griewank Geometrico': mejorEval_GG,
            'Rastrigin Lineal': mejorEval_NL,
            'Rastrigin Geometrico': mejorEval_NG,
            'Rosenbrock Lineal': mejorEval_RL,
            'Rosenbrock Geometrico': mejorEval_RG}
# Hacemos un diccionario para guardar la info
resultados = {}
# Calcular las medidas de tendencia central para cada función
for nombre, valores in funciones.items():
    resultados[nombre] = {
        'media': statistics.mean(valores),
        'mediana': statistics.median(valores),
        'moda': statistics.mode(valores),
        'minimo': min(valores),
        'max': max(valores),
        'STD': statistics.stdev(valores)
    }

# Convertir el diccionario en un DataFrame
Analisis = pd.DataFrame(resultados).T # Transponer para que las funciones sean fila

Analisis.to_csv('Tabla_SA.csv')

# %%
resultados
# %%
# Ahora hacemos el boxplot, priero convirtiendo el diccionario en dataframe
Datos_SA = pd.DataFrame(funciones)

# %%
plt.figure(figsize=(18, 10))
Datos_SA.boxplot()
plt.title('Boxplot de Funciones con diferentes esquemas de enfriamiento')
plt.ylabel('Evaluación')
plt.xticks(rotation=45)
# %%
# hacemos lo mismo ahora para AG

mejorEval_AE = [df['MejorEval'].iloc[-1] for df in Ackley_Elitismo]
mejorEval_AGen = [df['MejorEval'].iloc[-1] for df in Ackley_Generacional]
mejorEval_AP = [df['MejorEval'].iloc[-1] for df in Ackley_Peores]
# Lo mismo con Griewank 
mejorEval_GE = [df['MejorEval'].iloc[-1] for df in Griewank_Elitismo]
mejorEval_GGen = [df['MejorEval'].iloc[-1] for df in Griewank_Generacional]
mejorEval_GP = [df['MejorEval'].iloc[-1] for df in Griewank_Peores]
# Rosenbrock
mejorEval_RE = [df['MejorEval'].iloc[-1] for df in Rosenbrock_Elitismo]
mejorEval_RGen = [df['MejorEval'].iloc[-1] for df in Rosenbrock_Generacional]
mejorEval_RP = [df['MejorEval'].iloc[-1] for df in Rosenbrock_Peores]
# Rastrigin
mejorEval_NE = [df['MejorEval'].iloc[-1] for df in Rastrigin_Elitismo]
mejorEval_NGen = [df['MejorEval'].iloc[-1] for df in Rastrigin_Generacional]
mejorEval_NP = [df['MejorEval'].iloc[-1] for df in Rastrigin_Peores]
# Sphere
mejorEval_SE = [df['MejorEval'].iloc[-1] for df in Sphere_Elitismo]
mejorEval_SGen = [df['MejorEval'].iloc[-1] for df in Sphere_Generacional]
mejorEval_SP = [df['MejorEval'].iloc[-1] for df in Sphere_Peores]

# %%

funciones_2 = {'Sphere Elitismo': mejorEval_SE,
             'Sphere Generacional': mejorEval_SG,
             'Sphere Peores': mejorEval_SP,
            'Ackley Elitismo': mejorEval_AE,
            'Ackley Generacional': mejorEval_AG,
            'Ackley Peores': mejorEval_AP,
            'Griewank Elitismo': mejorEval_GE,
            'Griewank Generacional': mejorEval_GG,
            'Griewank Peores': mejorEval_GP,
            'Rastrigin Elitismo': mejorEval_NE,
            'Rastrigin Generacional': mejorEval_NG,
            'Rastrigin Peores': mejorEval_NP,
            'Rosenbrock Elitismo': mejorEval_RE,
            'Rosenbrock Generacional': mejorEval_RG,
            'Rosenbrock Peores': mejorEval_RP}

# %%
# Ahora hacemos el boxplot, priero convirtiendo el diccionario en dataframe
Datos_GA = pd.DataFrame(funciones_2)

# %%
plt.figure(figsize=(18, 10))
Datos_GA.boxplot()
plt.title('Boxplot de Funciones con diferentes esquemas de remplazo')
plt.ylabel('Evaluación')
plt.xticks(rotation=45)
# %%
