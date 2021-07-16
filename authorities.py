from aenum import MultiValueEnum


class Authorities(MultiValueEnum):
    AIR_FORCE = 1, 'חיל האוויר'
    YAMAL_1014 = 2, 'ימ"ל 1014'
    YAMAL_1024 = 3, 'ימ"ל 1024'
    YAMAL_1044 = 4, 'ימ"ל 1044'
    YAMAL_1079 = 5, 'ימ"ל 1079'
    YAMAL_1600 = 6, 'ימ"ל 1600'
    NAVY = 7, 'חיל הים'
    CSC = 8, 'מצו"ב'
    INTELLIGENCE_CORPS = 9, 'חיל מודיעין'
    MEDICAL_CORPS = 10, 'חיל הרפואה'
    TECHNOLOGY_MAINTENANCE_CORPS = 11, 'חיל האחזקה'
    LOGISTICS_CORPS = 12, 'חיל הלוגיסטיקה'
    MANPOWER_DIRECTORATE = 13, 'אכ"א'
    OPERATIONS_DIRECTORATE = 14, 'אמ"ץ'
    C4I_CORPS = 15, 'חיל תקשוב'
    RAFAEL = 16, 'רפאל'
    ADWTI = 17, 'מפא"ת'
    IIBR = 18, 'המכון הביולוגי'
    PLANNING_DEPARTMENT = 19, 'אג"ת'

    @classmethod
    def from_string(cls, value: str):
        try:
            return Authorities(value)
        except:
            return None
