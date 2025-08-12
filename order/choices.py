from django.db import models

class NigerianStates(models.TextChoices):
    ABIA = "AB", "Abia"
    ADAMAWA = "AD", "Adamawa"
    AKWA_IBOM = "AK", "Akwa Ibom"
    ANAMBRA = "AN", "Anambra"
    BAUCHI = "BA", "Bauchi"
    BAYELSA = "BY", "Bayelsa"
    BENUE = "BE", "Benue"
    BORNO = "BO", "Borno"
    CROSS_RIVER = "CR", "Cross River"
    DELTA = "DE", "Delta"
    EBONYI = "EB", "Ebonyi"
    EDO = "ED", "Edo"
    EKITI = "EK", "Ekiti"
    ENUGU = "EN", "Enugu"
    FCT = "FC", "Federal Capital Territory"
    GOMBE = "GO", "Gombe"
    IMO = "IM", "Imo"
    JIGAWA = "JI", "Jigawa"
    KADUNA = "KD", "Kaduna"
    KANO = "KN", "Kano"
    KATSINA = "KT", "Katsina"
    KEBBI = "KE", "Kebbi"
    KOGI = "KG", "Kogi"
    KWARA = "KW", "Kwara"
    LAGOS = "LA", "Lagos"
    NASARAWA = "NA", "Nasarawa"
    NIGER = "NI", "Niger"
    OGUN = "OG", "Ogun"
    ONDO = "ON", "Ondo"
    OSUN = "OS", "Osun"
    OYO = "OY", "Oyo"
    PLATEAU = "PL", "Plateau"
    RIVERS = "RI", "Rivers"
    SOKOTO = "SO", "Sokoto"
    TARABA = "TA", "Taraba"
    YOBE = "YO", "Yobe"
    ZAMFARA = "ZA", "Zamfara"

DELIVERY_PRICES = {
    NigerianStates.ABIA: 2000,
    NigerianStates.ADAMAWA: 3500,
    NigerianStates.AKWA_IBOM: 2500,
    NigerianStates.ANAMBRA: 2200,
    NigerianStates.BAUCHI: 3500,
    NigerianStates.BAYELSA: 3000,
    NigerianStates.BENUE: 2800,
    NigerianStates.BORNO: 4000,
    NigerianStates.CROSS_RIVER: 2700,
    NigerianStates.DELTA: 2300,
    NigerianStates.EBONYI: 2100,
    NigerianStates.EDO: 2300,
    NigerianStates.EKITI: 2000,
    NigerianStates.ENUGU: 2100,
    NigerianStates.FCT: 2500,
    NigerianStates.GOMBE: 3500,
    NigerianStates.IMO: 2200,
    NigerianStates.JIGAWA: 3700,
    NigerianStates.KADUNA: 3000,
    NigerianStates.KANO: 3200,
    NigerianStates.KATSINA: 3400,
    NigerianStates.KEBBI: 3600,
    NigerianStates.KOGI: 2400,
    NigerianStates.KWARA: 2400,
    NigerianStates.LAGOS: 1500,
    NigerianStates.NASARAWA: 2600,
    NigerianStates.NIGER: 2700,
    NigerianStates.OGUN: 1800,
    NigerianStates.ONDO: 2000,
    NigerianStates.OSUN: 2000,
    NigerianStates.OYO: 1900,
    NigerianStates.PLATEAU: 2800,
    NigerianStates.RIVERS: 2500,
    NigerianStates.SOKOTO: 3800,
    NigerianStates.TARABA: 3600,
    NigerianStates.YOBE: 3900,
    NigerianStates.ZAMFARA: 3700,
}