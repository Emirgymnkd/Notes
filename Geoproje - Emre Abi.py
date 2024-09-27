#emre abinin yolladığı örnek model kod bloğu.

from plxscripting.easy import *
import math

s_i, g_i = new_server('localhost', 10000, password='hDuviP7EnXxwYCUN')
s_o, g_o = new_server('localhost', 10001, password='hDuviP7EnXxwYCUN')
s_i.new()


g_i.setproperties(
    "Title","deneme",
    "Company","Geoproje Mühendislik",
    "ModelType","Plane strain"
)

g_i.gotosoil()
g_i.SoilContour.initializerectangular(-20,-30,20,0)
bh_1 = g_i.borehole(0)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 0, 30)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 1, 20)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 2, 5)

zemin1 = g_i.soilmat(
    "SoilModel","Hardening-Soil",
    "Identification","zemin-1",
    "gammaUnsat",18,
    "gammaSat",19,
    "E50ref",15000,
    "cRef",5,
    "phi",35,
    "psi",5,
    "GwUseDefaults",True
)
zemin2 = g_i.soilmat(
    "SoilModel","Hoek-Brown",
    "Identification","zemin-2",
    "gammaUnsat",19,
    "gammaSat",20,
    "Erm",500000,
    "mi",19,
    "nu",0.2,
    "GSI",20,
    "Disturbance", 1,
    "AbsSigmaCI",250000
)

zemin3 = g_i.soilmat(
    "SoilModel","Hoek-Brown",
    "Identification","zemin-2",
    "gammaUnsat",20,
    "gammaSat",21,
    "Erm",750000,
    "mi",19,
    "nu",0.2,
    "GSI",30,
    "Disturbance", 1,
    "AbsSigmaCI",350000
)
g_i.Soillayer_1.Soil.Material.set(zemin1)
g_i.Soillayer_2.Soil.Material.set(zemin2)
g_i.Soillayer_3.Soil.Material.set(zemin3)

kazik_malzeme = g_i.platemat(
    "MaterialType", "Elastic",
    "Identification","kazik",
    "Comments" , "65'lik Kazik",
    "EA1", 13826280.17,
    "EI",365100.2107,
    "StructNu",0.15
    )

ankraj_free = g_i.anchormat(
    "MaterialType","Elastic",
    "Identification","ankraj_free",
    "LSpacing",2,
    "EA", 114921.2563
)

ankraj_body = g_i.embeddedbeammat(
    "MaterialType","Elastic",
    "Identification","ankraj_body",
    "Gamma",25,
    "LSpacing",2,
    "E",20000000,
    "TSkinStartMax", 250,
    "TSkinEndMax", 250,
    "Diameter", 0.15
)
""
g_i.gotostructures()
Plate_1 = g_i.plate(5,30,5,20,
"Material",kazik_malzeme)
g_i.neginterface(5,30,5,19)
g_i.posinterface(5,30,5,19)[-1]
g_i.n2nanchor(5,29,-2.73,26.93,
"Material",ankraj_free)
g_i.n2nanchor(5,27,-1.76,25.19,
"Material",ankraj_free) 
g_i.n2nanchor(5,25,-0.8,23.45,
"Material",ankraj_free)
g_i.embeddedbeam(-2.73,26.93,-10.45,24.86,
    "Material",ankraj_body,
    "Connection", "Free")
g_i.embeddedbeam(-1.76,25.19,-9.49,23.12,
    "Material",ankraj_body,
    "Connection", "Free")
g_i.embeddedbeam(-0.80,23.45,-8.52,21.38,
    "Material",ankraj_body,
    "Connection", "Free")
g_i.line(5,28.50,20,28.50)
g_i.line(5,26.50,20,26.50)
g_i.line(5,24.50,20,24.50)
g_i.line(5,22,20,22)
g_i.lineload(4,30,1,30,
"qy_start",-50)

g_i.gotomesh()
g_i.mesh(0.04002)

g_i.gotostages()
phase0_s = g_i.InitialPhase
g_i.NegativeInterface_1.activate(phase0_s)
g_i.PositiveInterface_1.activate(phase0_s)
g_i.LineLoad_1_1.activate(phase0_s)
g_i.Plate_1.activate(phase0_s)
phase1_s = g_i.phase(phase0_s)
phase1_s.Identification = "Stage 1"
g_i.BoreHolePolygon_1_1.deactivate(phase1_s)
g_i.NodeToNodeAnchor_1_1.activate(phase1_s)
g_i.NodeToNodeAnchor_1_1.AdjustPrestress.set(phase1_s, True)
g_i.NodeToNodeAnchor_1_1.PrestressForce.set(phase1_s, 350)
g_i.EmbeddedBeam_1_1.activate(phase1_s)
phase2_s = g_i.phase(phase1_s)
phase2_s.Identification = "Stage 2"
g_i.BoreHolePolygon_1_2.deactivate(phase2_s)
g_i.NodeToNodeAnchor_2_1.activate(phase2_s)
g_i.NodeToNodeAnchor_2_1.AdjustPrestress.set(phase2_s, True)
g_i.NodeToNodeAnchor_2_1.PrestressForce.set(phase2_s, 350)
g_i.EmbeddedBeam_2_1.activate(phase2_s)
phase3_s = g_i.phase(phase2_s)
phase3_s.Identification = "Stage 3"
g_i.BoreHolePolygon_1_3.deactivate(phase3_s)
g_i.NodeToNodeAnchor_3_1.activate(phase3_s)
g_i.NodeToNodeAnchor_3_1.AdjustPrestress.set(phase3_s, True)
g_i.NodeToNodeAnchor_3_1.PrestressForce.set(phase3_s, 350)
g_i.EmbeddedBeam_3_1.activate(phase3_s)
phase4_s = g_i.phase(phase3_s)
phase4_s.DeformCalcType ="Safety"
g_i.calculate()

g_i.view(phase4_s)

