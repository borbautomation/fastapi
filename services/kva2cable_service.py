from typing import Optional
import math
import sympy

def get_s(voltage,amps,longitud):
    v_drop = 3*voltage/100
    #print(f"voltaje : {voltage}\n\nAmperaje : {amps}\n\nlong : {longitud}")
    cu_rho = 0.0172
    al_rho = 0.0282

    s_cu = math.sqrt(3)*cu_rho*amps*longitud/v_drop
    s_al = math.sqrt(3)*al_rho*amps*longitud/v_drop

    return {"cobre":{"seccion":s_cu,"awg":awg(s_cu)},"aluminio":{"seccion":s_al,"awg":awg(s_al)}}

def awg(s):
    from services.cable_dict import s_cable as cable_dict
    for key in cable_dict:
        if s in cable_dict[key]:
            return key
    return cable_dict

def get_gnd(amps):
    from services.cable_dict import gnd_dict_cu as cu_gnd_dict
    from services.cable_dict import gnd_dict_al as al_gnd_dict

    gnd = {}
    for key in cu_gnd_dict:
        if amps in cu_gnd_dict[key]:
            gnd["cobre"] = key
            break
    for key in al_gnd_dict:
        if amps in al_gnd_dict[key]:
            gnd["aluminio"] = key
            break
    return gnd




def get_kva2amp(kva:float = 11 ,voltaje:int = 220, longitud:Optional[float] = 1 , hilos:Optional[int] = 1) -> dict:
    amps_total = round(1000*kva/(math.sqrt(3)*voltaje)/0.91)
    amps_per_line = amps_total/hilos
    cable = get_s(voltaje,amps_per_line,longitud)
    gnd = get_gnd(amps_total)

    return {
            "input":
                {
                    "kva":kva,
                    "voltaje":voltaje,
                    "longitud":longitud,
                    "hilos":hilos
                },
            "output":
                {
                    "amps_total":amps_total,
                    "amps_per_line":amps_per_line,
                    "cable":cable,
                    "gnd":gnd
                    

                },

            }
    