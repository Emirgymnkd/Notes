#PLAXIS 2D programında Sedat Hoca'nın yüksek lisans öğrencilerine verdiği derse katıldım ve ilk kez bir iksa modeli oluşturmuştum. Şimdi de onu oluşturan kodu yazıyorum:
from plxscripting.easy import *
import math


s_i, g_i = new_server("localhost", 10000 ,password="hDuviP7EnXxwYCUN")
s_o, g_o = new_server("localhost", 10001, password="hDuviP7EnXxwYCUN")
s_i.new()



g_i.setproperties("Title","GeoProje-Abdullah Filiz")
g_i.setproperties("Company","GeoProje Mühendislik")
g_i.setproperties("ModelType", "Plane Strain")

g_i.gotosoil()
g_i.SoilContour.initializerectangular(-44, -35, 16, 1)
bh_1 = g_i.borehole(0)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 0, 1)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 1, 0)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 2, -2.5)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 3, -6)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 4, -13)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 5, -17)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 6, -22)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 7, -27)
g_i.soillayer(0)
g_i.setsoillayerlevel(bh_1, 8, -28)


Dolgu =g_i.soilmat(
    "Identification", "Dolgu",
    "SoilModel", "HS-Small",
    "DrainageType", "Drained",
    "gammaUnsat", 18,
    "gammaSat", 19,
    "E50ref", 12000,
    "G0Ref", 38600,
    "gamma07", 0.00003,
    "cRef", 1,
    "phi", 32,
    "psi", 3,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8
)


KilliKumluÇakil = g_i.soilmat(
    "SoilModel", "HS-Small",
    "DrainageType", "Drained",
    "Identification", "KilliKumluÇakil",
    "gammaUnsat", 21,
    "gammaSat", 22,
    "E50Ref", 50000,
    "G0Ref", 112000,
    "gamma07", 0.00035,
    "cRef", 15,
    "phi", 34,
    "psi", 4,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8
)
KilliKumluÇakil2 = g_i.soilmat(
    "SoilModel", "Hs-Small",
    "DrainageType", "Drained",
    "Identification", "KilliKumluÇakil2",
    "gammaUnsat", 20,
    "gammaSat", 21,
    "E50Ref", 25000,
    "G0Ref", 101200,
    "gamma07",0.00024,
    "cRef", 10,
    "phi", 34,
    "psi", 4,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8
)
KumluKilÜst =g_i.soilmat(
    "SoilModel", "Hs-Small",
    "DrainageType", "Undrained A",
    "Identification", "KumluKilÜst",
    "gammaUnsat", 19,
    "gammaSat", 20,
    "E50Ref", 10000,
    "G0Ref", 64000, 
    "gamma07", 0.00026,
    "cRef", 20,
    "phi", 28,
    "psi", 0,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8,
) 
KumluKilAlt =g_i.soilmat(
    "SoilModel", "Hs-Small",
    "Identification", "KumluKilAlt",
    "DrainageType", "Undrained A",
    "gammaUnsat", 20,
    "gammaSat", 21,
    "E50Ref", 40000,
    "G0Ref", 152000,
    "gamma07", 0.00032,
    "cRef", 10,
    "phi", 28,
    "psi", 0,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8,
)
KumluKilOrta = g_i.soilmat(
    "SoilModel", "HS-Small",
    "DrainageType", "Undrained A",
    "Identification", "KumluKilOrta",
    "gammaUnsat", 19,
    "gammaSat", 20,
    "E50Ref", 22000,
    "G0Ref", 113000,
    "gamma07", 0.00028,
    "cRef", 15,
    "phi", 28,
    "psi", 0,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8,
)

SiltliKil = g_i.soilmat(
    "SoilModel", "Hs-Small",
    "DrainageType", "Undrained A",
    "Identification", "SiltliKil",
    "gammaUnsat", 18,
    "gammaSat", 19,
    "E50Ref", 8000,
    "G0Ref", 38000,
    "gamma07", 0.00012,
    "cRef", 2,
    "phi", 26,
    "psi", 0,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8,
)
SiltliKumluKil = g_i.soilmat(
    "SoilModel", "HS-Small",
    "DrainageType", "Undrained A",
    "Identification","SiltliKumluKil",
    "gammaUnsat", 19,
    "gammaSat", 20,
    "E50Ref", 30000,
    "G0Ref", 123000,
    "gamma07", 0.00033,
    "cRef", 10,
    "phi", 28,
    "psi", 0,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8,
)

SiltliKumluÇakil = g_i.soilmat(
    "SoilModel", "HS-Small",
    "Identification", "SiltliKumluÇakil",
    "DrainageType", "Drained",
    "gammaUnsat", 19,
    "gammaSat", 20,
    "E50Ref", 15000,
    "G0Ref", 39600,
    "gamma07", 0.00033,
    "cRef", 1,
    "phi", 30,
    "psi", 0,
    "InterfaceStrengthDetermination", "Manual",
    "Rinter", 0.8,
)

g_i.Soillayer_1.Soil.Material.set(Dolgu)
g_i.Soillayer_2.Soil.Material.set(SiltliKil)
g_i.Soillayer_3.Soil.Material.set(SiltliKumluÇakil)
g_i.Soillayer_4.Soil.Material.set(KumluKilÜst)
g_i.Soillayer_5.Soil.Material.set(KilliKumluÇakil)
g_i.Soillayer_6.Soil.Material.set(KumluKilOrta)
g_i.Soillayer_7.Soil.Material.set(KilliKumluÇakil2)
g_i.Soillayer_8.Soil.Material.set(SiltliKumluKil)
g_i.Soillayer_9.Soil.Material.set(KumluKilAlt)

kazik_malzeme = g_i.platemat(
    "MaterialType", "Elastic",
    "Identification", "Diyafram Duvari",
    "Isotropic", False,
     "w", 5,
     "EA1", 24000000,
     "EA2", 24000000,
     "EI", 1280000
)
ankraj_body =g_i.geogridmat (
    "Identification", "Ankraj Kökü 1",
    "MaterialType", "Elastic",
    "EA1", 600000
)
ankraj_free = g_i.anchormat(
        "MaterialType", "Elastoplastic",
        "Identification", "Ankraj 1",
        "Lspacing", 1,
        "EA",168000
        #"F_max_tens", 960,
        #"F_max_comp",  960
)

ankraj_free = g_i.anchormat(
    "MaterialType", "Elastoplastic",
    "Identification", "Ankraj 2",
    "Lspacing", 2,
    "EA", 168000
    # "F_max_tens", 1200,
    # "F_max_comp", 1200
)

g_i.gotostructures()
Plate_1 = g_i.plate( 0, 1, 0, -22, "Material", kazik_malzeme)

g_i.neginterface( 0, -22,  0, 1)
g_i.posinterface( 0, -22,  0, 1)

g_i.n2nanchor(0, -1.8, -13.16, -6.588, "Material",  ankraj_free)
g_i.n2nanchor(0, -4.8, -11.27, -8.9, "Material",  ankraj_free)
g_i.n2nanchor(0, -7.8, -9.4, -11.2, "Material",  ankraj_free)
g_i.n2nanchor(0, -10.8, -7.518, -13.54, "Material", ankraj_free)

geogrid1 = g_i.geogrid((-13.16, -6.588), (-22.56, -10.01), "Material", ankraj_body)
geogrid2 = g_i.geogrid((-11.27, -8.9), (-20.67, -12.32), "Material", ankraj_body)
geogrid3 = g_i.geogrid((-9.4, -11.20), (-18.8, -14.64), "Material", ankraj_body)
geogrid4 = g_i.geogrid((-7.518, -13.54), (-16.92, -16.96), "Material", ankraj_body)

g_i.line(0, -3, 16, -3)
g_i.line(0, -6, 16, -6)
g_i.line(0, -9, 16, -9)
g_i.line(0, -12, 16, -12)
g_i.line(0, -14, 16, -14)

g_i.lineload(-26, 1, -5, 1, "qy_start", -15)
g_i.lineload(-5, 1, 0, 1, "qy_start", -25)

# polygon_1 = g_i.polygon((-44, 0), (16, 0), (16, 1), (-44, 1)) 
# polygon_2 = g_i.polygon((-44, -2), (16, -2), (16, 0), (-44, 0))   
# polygon_3 = g_i.polygon((-44, -6), (16, -6), (16, -3), (-44, -3)) 
# polygon_4 = g_i.polygon((-44, -13), (16, -13), (16, -6), (-44, -6)) 
# polygon_5 = g_i.polygon((-44, -17),(16, -17), (16, -13), (-44, -13)) 
# polygon_6 = g_i.polygon((-44, -22), (16, -22), (16, -17), (-44, -17)) 
# polygon_7 = g_i.polygon((-44, -27), (16, -27), (16, -22), (-44,-22)) 
# polygon_8 = g_i.polygon((-44, -28),(16, -28), (16, -27), (-44, -27)) BUNLAR ÇALIŞMADI!!!!!!

soils = g_i.soillayers[:]
for soil in soils:
    soil.CoarsenessFactor = 1

g_i.gotomesh()
g_i.mesh(0.04002)

# g_i.coarsen(polygon_1, Coarseness=1)
# g_i.coarsen(polygon_2)
# g_i.coarsen(polygon_3)
# g_i.coarsen(polygon_3)
# g_i.coarsen(polygon_4)
# g_i.coarsen(polygon_5)
# g_i.coarsen(polygon_6)
# g_i.coarsen(polygon_7)
# g_i.coarsen(polygon_8)

g_i.gotostages()

phase0 = g_i.InitialPhase
phase1 =g_i.phase(phase0)
phase1.Identification = "Perde+Yükler"
g_i.NegativeInterface_1.activate(phase1)
g_i.PositiveInterface_1.activate(phase1)
g_i.LineLoad_1_1.activate(phase1)
g_i.LineLoad_2_1.activate(phase1)
g_i.Plate_1.activate(phase1)
g_i.gotoflow()
waterlevel0 = g_i.waterlevel((-44, 0), (19,0))
g_i.setglobalwaterlevel(waterlevel0,phase1)

phase2 =g_i.phase(phase1)
phase2.Identification = "K1"
# g_i.setproperties(phase2, "PorePresCalcType", "steadystategroundwaterflow")bu ve alttakiler çalışıyor ama kx ve ky değerlerini giremdiğimden direkt başta çöküyor.
g_i.BoreHolePolygon_1_2.deactivate(phase2)
g_i.BoreHolePolygon_2_2.deactivate(phase2)
g_i.BoreHolePolygon_3_1.deactivate(phase2)
g_i.gotoflow()
waterlevel = g_i.waterlevel((-44, 0), (0, -3), (18, -3))
g_i.setglobalwaterlevel(waterlevel, phase2)

phase3 = g_i.phase(phase2)
phase3.Identification = "K2+A1"
# g_i.setproperties(phase3, "PorePesCalcType", "steadystategroundwaterflow")
g_i.BoreHolePolygon_3_3.deactivate(phase3)
g_i.NodeToNodeAnchor_1_1.AdjustPrestress.set(phase2, True)
g_i.NodeToNodeAnchor_1_1.PrestressForce.set(phase2, 650)
g_i.NodeToNodeAnchor_1_1.activate(phase2)
g_i.geogrid_1_1.activate(phase2)
waterlevel2 = g_i.waterlevel((-44, 0),(0.04480, -6.30), (18, -6))
g_i.setglobalwaterlevel(waterlevel2 , phase3)

phase4 = g_i.phase(phase3)
phase4.Identification = "K3+A2"
# g_i.setproperties(phase4, "PorePresCalcType", "steadystategroundwaterflow")
g_i.BoreHolePolygon_4_1.deactivate(phase4)
g_i.NodeToNodeAnchor_2_1.activate(phase3)
g_i.NodeToNodeAnchor_2_1.AdjustPrestress.set(phase3, True)
g_i.NodeToNodeAnchor_2_1.PrestressForce.set(phase3, 650)
g_i.geogrid_2_1.activate(phase3)
waterlevel3 = g_i.waterlevel((-44, 0), (0.07062, -9.30), (18, -9.30))
g_i.setglobalwaterlevel(waterlevel3,phase4)

phase5 = g_i.phase(phase4)
phase5.Identification = "K4+A3"
# g_i.setproperties(phase5, "PorePresCalcType", "steadystategroundwaterflow")
g_i.BoreHolePolygon_4_3.deactivate(phase5)
g_i.NodeToNodeAnchor_3_1.activate(phase5)
g_i.NodeToNodeAnchor_3_1.AdjustPrestress.set(phase5, True)
g_i.NodeToNodeAnchor_3_1.PrestressForce.set(phase5, 650)
g_i.geogrid_3_1.activate(phase5)
g_i.geogrid_3_2.activate(phase5)
waterlevel4 = g_i.waterlevel((-44, 0), (0, -12.30), (18, -12.30))
g_i.setglobalwaterlevel(waterlevel4, phase5)

phase6 = g_i.phase(phase5)
phase6.Identification = "K5+A4"
# g_i.setproperties(phase6, "PorePresCalcType", "steadystategroundwaterflow")
g_i.BoreHolePolygon_4_4.deactivate(phase6)
g_i.BoreHolePolygon_5_1.deactivate(phase6)
g_i.NodeToNodeAnchor_4_1.activate(phase6)
g_i.geogrid_4_1.activate(phase6)
g_i.NodeToNodeAnchor_4_1.AdjustPrestress.set(phase6, True)
g_i.NodeToNodeAnchor_4_1.PrestressForce.set(phase6, 650)
waterlevel5 = g_i.waterlevel((-44, 0), (0, -13.80), (18, -13.80))
g_i.setglobalwaterlevel(waterlevel5,phase6)

g_i.calculate()
g_i.view(phase6)