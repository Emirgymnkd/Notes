#python eğitimi, openpyxl, pandas pratikleri, 2d plaxis input modeli kodlama çabalarından sonra outputa geçiş yapıyoruz. ne kadar devam ettirebilirim bilmiyorum(kaynak çok kısıtlı çünkü)
#ama ne bulduysam koymaya çalışacağım.

#PLAXIS Geotechnical Analysis Youtube Kanalı Output Video Notları

"""Output command line uses the same structure as in Input. But most actions are not translated into commands."""
"""With the Output GUI we usually:
Change the plot we are looking at such as deformations, stresses , forces."""

#help -> command reference bol bol kullanacağız.

"""Result Types"""
#for soils: ResultTypes.Soil
#plates: ResultTypes.Plate
#embedded beams: ResultTypes.EmbeddedBeam

#vertical displacement uy: ResultTypes.Soil.Uy
#excess pore pressures: ResultTypes.Soil.PExcess
#vertical effective stresses: ResultTypes.Soil.SiggyE
#bending moment (2d): ResultTypes.Plate.M2D
#active pore pressure in interface: ResultTypes.Interface.PActive

#bütün komutlara ulaaşbilmek için ""echo"" komutunu kullan. örn: echo ResultTypes.Soil

"""Phase"""
#accessible as Phase_x[n] for the nth step of Phase_X

#Phase_x.Reached command contains general results of the phase:

#Phase_x.Reached.SumMstage
#Phase_x.Reached.SumMsf
#Phase_x.Reached.Time

#Phase_x.InputSettings contains general settings of the phase:

#Phase_x.InputSettings.IgnoreUndrainedBehaviour
#Phase_x.InputSettings.UseUpdatedMesh
#Phase_x.InputSettings.UseUpdatedWaterPressures

#full details in: echo Phase_x

#object reference dan da aratıp bulabilrsin.

"""Cross-Section Plot"  """

#linecrosssectionplot crates a cross_section in a Plot object in 2D:                            #KESİT ALMAK İÇİN KULLLANILIR.

#linecrossectionplot <plot> <cords> <cords>
#plot = current plot of soil model for ex: deformations plot
#cords = set of two coordinates indicating first/second point of cross-section
#usually combined with getcrossectionresults command 

"for 3d:"
#crossectionplot creates a surface cross-section in a new Plot object in 3D:
#crossectionplot <plot> <coords> <coords> <coords>

"in plaxis:"
#linecrossectionplot Plot_1 (0 12) (100 12)
"in python:"
#g_o.linecrosssectionplot(g_o.Plots[0], 0, 12, 100, 12)

"kesit alıp sonucuna bakalım:"
#plot = g_o.Linecrosssectionplot (0, 5, 10, 5 )
#plot.ResultType = ResultType.Soil.Ux
#plot.Refresh()

"""relevant commands"""
#getsingleresult (gsre): displays the result at the specified coordinate or a specific node/stress point with or without result smoothing.
#getresults (gres): generates a table with the calculation results.
#addcurvepoint (acp): preselection of stress points or nodes for calculation results, with an indcation of a preferred direction.
#getcurveresults (gcres): displays results for curve points that have been previously selected for several different phases.
#getcrosssectionresults (gcsres): generates a table with the calculation results of a cross section.

"details"
#getsingleresult : <phase or step> <resulttype> <location> <boolean> 
#example: getsingleresult Phase_6 ResultTypes.Soil.Utot (50 20)

#getresults : <phase or step> <resulttype> <"node" "stresspoint">
#example : getresults Phase_6 ResultTypes.Soil.Utot "node"
#for structure:
#getresults Plate_1 Phases[-1] ResultTypes.PlateM2D "node"

#curve point selection:
#addcurvepoint <"node" or "stresspoint"> <clustername or structurename> <location>
#example: addcurvepoint "node" (50 15)
#addcurvepoint "stresspoint" Soil_3_1 (50 15)

#echo curvepoints --> list of selected curve points
#echo CurvePoints.Nodes[-1]

#get curve results:
#getcurveresults <point> <phase or step> <resulttype>
#getcurveresultspath <point> <phase/step range:start - end> <resulttype>

#example: getcurveresults CN_1 Phase_1 ResultTypes.Soil.Uy
#example: getcurveresultspath CN_1 Phase_1 Phase_1 ResultTypes.Soil.Uy

#get cross section results
#getcrosssectionresults <plot> <phase or step> <resulttype> <boolean> ((boolean is optional))
#example: getcrsossectionresults Plots[-1] Phase_6 ResultTypes.Soil.Uy True


