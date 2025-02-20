from enum import Enum

class Airline(Enum):
    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, airline_name: str = "", website: str = ""):
        self._airline_name_ = airline_name
        self._website_ = website

    def __str__(self):
        return self.value

    @property
    def airline_name(self):
        return self._airline_name_
    
    @property
    def website(self):
        return self._website_
    
    @staticmethod
    def serialize(airline_enum: Enum):
        return {
            "airline_name": airline_enum.airline_name,
            "website": airline_enum.website
        }
    
    #static method to search by starting chars of airline
    @staticmethod
    def search_by(search: str):
        for airline in Airline:
            if search.lower() in airline.airline_name.lower():
                return Airline.serialize(airline)
        return {"name": search, "website": ""}


    AIRLINE_0 = "Finnair", "https://www.finnair.com"
    AIRLINE_1 = "Thai Lion Air", "https://www.lionairthai.com"
    AIRLINE_2 = "Wizz Air", "https://wizzair.com"
    AIRLINE_3 = "Loganair", "https://www.loganair.co.uk"
    AIRLINE_4 = "Aer Lingus Regional ", "https://www.aerlingus.com"
    AIRLINE_5 = "Air Vanuatu", "https://www.airvanuatu.com"
    AIRLINE_6 = "REX Regional Express Airlines", "https://www.rex.com.au"
    AIRLINE_7 = "Virgin Australia", "https://help.virginatlantic.com"
    AIRLINE_8 = "Qatar Airways", "https://www.qatarairways.com"
    AIRLINE_9 = "Air Moldova", "https://www.airmoldova.md"
    AIRLINE_10 = "Atlantic Airways", "https://www.atlanticairways.com"
    AIRLINE_11 = "Etihad Airways", "https://www.etihad.com"
    AIRLINE_12 = "Air Transat", "https://www.airtransat.com"
    AIRLINE_13 = "Sunwing Airlines", "https://www.sunwing.ca"
    AIRLINE_14 = "WestJet", "https://www.westjet.com"
    AIRLINE_15 = "Aerolineas Argentinas", "https://www.aerolineas.com.ar"
    AIRLINE_16 = "Air Corsica", "https://www.aircorsica.com"
    AIRLINE_17 = "Air Europa", "https://www.aireuropa.com"
    AIRLINE_18 = "Air France", "https://wwws.airfrance.us"
    AIRLINE_19 = "Air India", "https://www.airindia.in"
    AIRLINE_20 = "Air Mauritius", "https://www.airmauritius.com"
    AIRLINE_21 = "Air Tahiti", "https://www.airtahiti.com"
    AIRLINE_22 = "Avianca Airlines", "https://ayuda.avianca.com"
    AIRLINE_23 = "Georgian Airways", "https://georgian-airways.com"
    AIRLINE_24 = "GOL Airlines", "https://www.voegol.com.br"
    AIRLINE_25 = "IndiGo Airlines", "https://www.goindigo.in"
    AIRLINE_26 = "Kenya Airways", "https://www.kenya-airways.com"
    AIRLINE_27 = "KLM Royal Dutch Airlines", "https://www.klm.hr"
    AIRLINE_28 = "LATAM Airlines", "https://www.latamairlines.com"
    AIRLINE_29 = "SpiceJet", "https://corporate.spicejet.com"
    AIRLINE_30 = "Transavia", "https://www.transavia.com"
    AIRLINE_31 = "Aurigny", "https://www.aurigny.com"
    AIRLINE_32 = "Emirates", "https://www.emirates.com"
    AIRLINE_33 = "Royal Brunei Airlines", "https://www.flyroyalbrunei.com"
    AIRLINE_34 = "Air Austral", "https://www.air-austral.com"
    AIRLINE_35 = "Air China", "https://www.airchina.us"
    AIRLINE_36 = "Air Tahiti Nui", "https://us.airtahitinui.com"
    AIRLINE_37 = "Armenia Aircompany", "https://armenianairlines.am"
    AIRLINE_38 = "Asiana Airlines", "https://flyasiana.com"
    AIRLINE_39 = "Azores Airlines", "https://www.azoresairlines.pt"
    AIRLINE_40 = "Azul", "https://www.voeazul.com.br"
    AIRLINE_41 = "Carpatair", "https://www.carpatair.com"
    AIRLINE_42 = "China Southern", "https://www.csair.com"
    AIRLINE_43 = "Condor", "https://www.condor.com"
    AIRLINE_44 = "Corsair International", "https://www.flycorsair.com"
    AIRLINE_45 = "Croatia Airlines", "https://www.croatiaairlines.com"
    AIRLINE_46 = "Hainan Airlines", "https://www.hainanairlines.com"
    AIRLINE_47 = "Helvetic Airways", "https://www.helvetic.com"
    AIRLINE_48 = "Icelandair", "https://www.icelandair.com"
    AIRLINE_49 = "Jet Time", "https://jettime.com"
    AIRLINE_50 = "Korean Air", "https://www.koreanair.com"
    AIRLINE_51 = "MIAT Mongolian Airlines", "https://www.miat.com"
    AIRLINE_52 = "Pegasus Airlines", "https://www.flypgs.com"
    AIRLINE_53 = "Plus Ultra", "https://www.plusultra.com"
    AIRLINE_54 = "Ryanair", "https://www.ryanair.com"
    AIRLINE_55 = "Spring Airlines", "https://en.ch.com"
    AIRLINE_56 = "TAP Portugal", "https://www.flytap.com"
    AIRLINE_57 = "TAROM", "https://www.tarom.ro"
    AIRLINE_58 = "TUIfly", "https://www.tui.com"
    AIRLINE_59 = "VivaAerobus", "https://blog.vivaaerobus.com"
    AIRLINE_60 = "Vueling", "https://www.vueling.com"
    AIRLINE_61 = "Air Baltic", "https://www.airbaltic.com"
    AIRLINE_62 = "Air Canada", "https://www.aircanada.com"
    AIRLINE_63 = "Air New Zealand", "https://www.airnewzealand.com"
    AIRLINE_64 = "Air Serbia", "https://www.airserbia.com"
    AIRLINE_65 = "Austrian Airlines", "https://www.austrian.com"
    AIRLINE_66 = "Azerbaijan Airlines", "https://www.azal.az"
    AIRLINE_67 = "Brussels Airlines", "https://www.brusselsairlines.com"
    AIRLINE_68 = "Bulgaria Air", "https://www.air.bg"
    AIRLINE_69 = "Edelweiss", "https://www.flyedelweiss.com"
    AIRLINE_70 = "Egypt Air", "https://www.egyptair.com"
    AIRLINE_71 = "Ethiopian Airlines", "https://www.ethiopianairlines.com"
    AIRLINE_72 = "Fiji Airways", "https://www.fijiairways.com"
    AIRLINE_73 = "Lufthansa", "https://www.lufthansa.com"
    AIRLINE_74 = "Luxair", "https://www.luxair.lu"
    AIRLINE_75 = "Norwegian", "https://www.norwegian.com"
    AIRLINE_76 = "Olympic Air", "https://www.olympicair.com"
    AIRLINE_77 = "S7 Airlines", "https://www.s7.ru"
    AIRLINE_78 = "SAS Scandinavian Airlines", "https://www.flysas.com"
    AIRLINE_79 = "SunExpress", "https://www.sunexpress.com"
    AIRLINE_80 = "Swiss International Air Lines", "https://www.swiss.com"
    AIRLINE_81 = "Turkish Airlines", "https://www.turkishairlines.com"
    AIRLINE_82 = "Aer Lingus", "https://www.aerlingus.com"
    AIRLINE_83 = "Aeroflot", "https://www.aeroflot.ru"
    AIRLINE_84 = "Aeroméxico", "https://aeromexico.com"
    AIRLINE_85 = "ANA", "https://www.ana.co.jp"
    AIRLINE_86 = "Belavia", "https://en.belavia.by"
    AIRLINE_87 = "BH Air", "http://www.bhairlines.com"
    AIRLINE_88 = "Volaris", "https://cms.volaris.com"
    AIRLINE_89 = "Czech Airlines", "https://www.smartwings.com"
    AIRLINE_90 = "Wingo", "https://www.wingo.com"
    AIRLINE_91 = "Air Asia", "https://support.airasia.com"
    AIRLINE_92 = "Alaska Airlines", "https://www.alaskaair.com"
    AIRLINE_93 = "Allegiant Air", "https://www.allegiantair.com"
    AIRLINE_94 = "American Airlines", "https://www.aa.com"
    AIRLINE_95 = "Bahamasair", "https://bahamasair.com"
    AIRLINE_96 = "Bangkok Airways", "https://www.bangkokair.com"
    AIRLINE_97 = "Cambodia Angkor Air", "https://www.aircambodia.com"
    AIRLINE_98 = "Caribbean Airlines", "https://www.caribbean-airlines.com"
    AIRLINE_99 = "Cathay Pacific", "https://www.cathaypacific.com"
    AIRLINE_100 = "Cebu Pacific", "https://www.cebupacificair.com"
    AIRLINE_101 = "China Airlines", "https://www.china-airlines.com"
    AIRLINE_102 = "Delta Air Lines", "https://www.delta.com"
    AIRLINE_103 = "Garuda Indonesia", "https://www.garuda-indonesia.com"
    AIRLINE_104 = "Hawaiian Airlines", "https://hawaiianair.custhelp.com"
    AIRLINE_105 = "HK Express", "https://www.hkexpress.com"
    AIRLINE_106 = "Hong Kong Airlines", "http://www.hkairlines.com"
    AIRLINE_107 = "Japan Airlines", "https://www.jal.co.jp"
    AIRLINE_108 = "JetBlue Airways", "https://www.jetblue.com"
    AIRLINE_109 = "Jetstar", "https://www.jetstar.com"
    AIRLINE_110 = "Lao Airlines", "https://laoairlines.com"
    AIRLINE_111 = "NokAir", "https://content.nokair.com"
    AIRLINE_112 = "Oman Air", "https://www.omanair.com"
    AIRLINE_113 = "Peach", "http://www.flypeach.com"
    AIRLINE_114 = "Philippines Airlines", "https://www.philippineairlines.com"
    AIRLINE_115 = "Porter Airlines", "https://www.flyporter.com"
    AIRLINE_116 = "Qantas", "https://www.qantas.com"
    AIRLINE_117 = "Royal Air Maroc", "https://www.royalairmaroc.com"
    AIRLINE_118 = "Royal Jordanian Airlines", "https://www.rj.com"
    AIRLINE_119 = "Saudia Airlines", "https://www.saudia.com"
    AIRLINE_120 = "Scoot Airlines", "https://www.flyscoot.com"
    AIRLINE_121 = "Singapore Airlines", "https://www.singaporeair.com"
    AIRLINE_122 = "South African Airways", "https://www.flysaa.com"
    AIRLINE_123 = "Sri Lankan Airlines", "https://www.srilankan.com"
    AIRLINE_124 = "United Airlines", "https://www.united.com"
    AIRLINE_125 = "Vietnam Airlines", "https://www.vietnamairlines.com"
    AIRLINE_126 = "Virgin Atlantic Airways", "https://help.virginatlantic.com"
    AIRLINE_127 = "Xiamen Airlines", "https://www.xiamenair.com"
    AIRLINE_128 = "Copa Airlines", "https://www.copaair.com"
    AIRLINE_129 = "Aegean Airlines", "https://en.aegeanair.com"
    AIRLINE_130 = "Air Astana", "https://airastana.com"
    AIRLINE_131 = "British Airways", "https://www.britishairways.com"
    AIRLINE_132 = "easyJet", "https://www.easyjet.com"
    AIRLINE_133 = "El Al", "https://www.elal.com"
    AIRLINE_134 = "Iberia", "https://www.iberia.com"
    AIRLINE_135 = "Jet2.com", "https://www.jet2.com"
    AIRLINE_136 = "SmartWings", "https://www.smartwings.com"
    AIRLINE_137 = "Thai Airways", "https://www.thaiairways.com"
    AIRLINE_138 = "Kuwait Airways", "https://www.kuwaitairways.com"
    AIRLINE_139 = "Malaysia Airlines", "https://www.malaysiaairlines.com"
    AIRLINE_140 = "Norse Atlantic Airways", "https://flynorse.com"
    AIRLINE_141 = "Spirit Airlines", "https://customersupport.spirit.com"
    AIRLINE_142 = "Frontier Airlines", "https://www.flyfrontier.com"
    AIRLINE_143 = "Cayman Airways", "https://www.caymanairways.com"
    AIRLINE_144 = "Southwest Airlines", "https://www.southwest.com"
    AIRLINE_145 = "Sun Country Airlines", "https://suncountry.com"
    AIRLINE_146 = "Pobeda", "https://www.flypobeda.ru"
    AIRLINE_147 = "ZIPAIR", "https://www.zipair.net"
