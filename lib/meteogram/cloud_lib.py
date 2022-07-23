import Ngl
import math
import numpy

# function to create the plot resource for the relative humidity plot of the meteogram
def get_cloud_resource(count_xdata):
  cloud_res = Ngl.Resources()
  cloud_res.vpXF            = 0.15   # The left side of the box
  cloud_res.vpYF            = 1.05   # The top side of the plot box
  cloud_res.vpWidthF        = 0.75   # The Width of the plot box
  cloud_res.vpHeightF       = 0.10   # The height of the plot box
  
  cloud_res.tiXAxisString      = ""             # X axes label.
  cloud_res.tiYAxisFontHeightF = 0.015          # Y axes font height.
  cloud_res.tiYAxisString      = "clouds [%]"   # Y axis label.

  cloud_res.tmXBMode           = "Explicit"     # Define own tick mark labels.
  cloud_res.tmXMajorGrid       = True
  cloud_res.tmXMajorGridLineDashPattern = 2
  cloud_res.tmYMajorGrid = True
  cloud_res.tmYLMaxTicks = 6
  cloud_res.tmXTOn             = False          # turn off the top tickmarks

  cloud_res.trXMaxF         = count_xdata   # max value on x-axis
  cloud_res.trYMaxF         = 100
  cloud_res.trYMinF         = 0.0
  cloud_res.tmYLMajorThicknessF = 0.1

  cloud_res.xyLineThicknesses  = 3
  cloud_res.xyLineColor        =  "blue"

  cloud_res.nglDraw         = False     # Don't draw individual plot.
  cloud_res.nglFrame        = False     # Don't advance frame.
  cloud_res.nglMaximize     = False     # Do not maximize plot in frame
  
  return cloud_res





# id, ts_hour, id_tsloc, ix, iy, t, q, u, v, psfc, glw, gsw, hfx, lh, tsk, tslb(1), rainc, rainnc, clw
# id:		grid ID
# ts_hour:	forecast time in hours
# id_tsloc:	time series ID
# ix,iy:		grid location (nearest grid to the station)
# t:		2 m Temperature (K)
# q:		2 m vapor mixing ratio (kg/kg)
# u:		10 m U wind (earth-relative)
# v:		10 m V wind (earth-relative)
# psfc:		surface pressure (Pa)
# glw:		downward longwave radiation flux at the ground (W/m^2, downward is positive)
# gsw:		net shortwave radiation flux at the ground (W/m^2, downward is positive)
# hfx:		surface sensible heat flux (W/m^2, upward is positive)
# lh:		surface latent heat flux (W/m^2, upward is positive)
# tsk:		skin temperature (K)
# tslb(1):	top soil layer temperature (K)
# rainc:		rainfall from a cumulus scheme (mm)
# rainnc:		rainfall from an explicit scheme (mm)
# clw:		total column-integrated water vapor and cloud variables
# Example:
#  2     0.033333    7  153  207     -39.49153       0.00104      -4.57959       7.21139   99064.35938     168.17384      12.06811     -41.77642       0.00001     259.18286     271.35104       0.00000       0.00000       0.00000


# If solar_diagnostics is activated (see README.namelist) and tslist is present, then time series variables relevant to solar forecasting.
# These additional variables from the time series output are:

# cldfrac2d:     2-D MAX CLOUD FRACTION (%)
# wvp:           WATER VAPOR PATH (kg m-2)
# lwp:           LIQUID CLOUD WATER PATH (kg m-2)
# iwp:           ICE CLOUD WATER PATH (kg m-2)
# swp:           SNOW CLOUD WATER PATH (kg m-2)
# wp_sum:        SUM OF LWP+IWP+SWP (kg m-2)
# lwp_tot:       LIQUID CLOUD WATER PATH RES + UNRES (kg m-2)
# iwp_tot:       ICE CLOUD WATER PATH RES + UNRES (kg m-2)
# wp_tot_sum:    SUM OF LWP+IWP+SWP RES + UNRES (kg m-2)
# re_qc:         MASS-WEIGHTED LIQUID CLOUD EFFECTIVE RADIUS (m)
# re_qi:         MASS-WEIGHTED ICE EFFECTIVE RADIUS (m)
# re_qs:         MASS-WEIGHTED SNOW EFFECTIVE RADIUS (m)
# re_qc_tot:     MASS-WEIGHTED LIQUID CLOUD EFFECTIVE RADIUS RES + UNRES (m)
# re_qi_tot:     MASS-WEIGHTED ICE EFFECTIVE RADIUS RES + UNRES (m)
# tau_qc:        MASS-WEIGHTED LIQUID CLOUD OPTICAL THICKNESS ()
# tau_qi:        MASS-WEIGHTED ICE OPTICAL THICKNESS ()
# tau_qs:        MASS-WEIGHTED SNOW OPTICAL THICKNESS ()
# tau_qc_tot:    MASS-WEIGHTED LIQUID CLOUD OPTICAL THICKNESS RES + UNRES ()
# tau_qi_tot:    MASS-WEIGHTED ICE OPTICAL THICKNESS RES + UNRES ()
# cbaseht:       CLOUD BASE HEIGHT (m)
# ctopht:        CLOUD TOP HEIGHT (m)
# cbaseht_tot:   CLOUD BASE HEIGHT RES + UNRES (m)
# ctopht_tot:    CLOUD TOP HEIGHT RES + UNRES (m)
# clrnidx:       CLEARNESS INDEX ()
# sza:           SOLAR ZENITH ANGLE (deg)


