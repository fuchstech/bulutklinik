data = """
id="oksuruk" value="oksuruk"
value="secilmedi" value="Seçilmedi" name="sikayetler[]"
value="kuru" value="Kuru" name="sikayetler[]"
value="balgamli" value="Balgamlı" name="sikayetler[]
value="kanli" value="Kanlı" name="sikayetler[]

value="nefesDarligi" id="nefesDarligi" name="sikayetler[]" 
value="akcigerHiriltisi" id="akciger-hiriltisi" name="sikayetler[]
value="gogusAgrisi" id="gogus-agrisi" name="sikayetler[]
value="gogus1" id="gogus1" name="sikayetler[]
value="gogus2" id="gogus2" name="sikayetler[]
value="gogus3" id="gogus3" name="sikayetler[]
value="gogus4" id="gogus4" name="sikayetler[]
value="gogus5" id="gogus5" name="sikayetler[]
value="gogus6" id="gogus6" name="sikayetler[]"
value="halsizlik" id="halsizlik" name="sikayetler[]"
value="bayilma" id="bayilma" name="sikayetler[]"
type="number" value="bayilmasayisi" name="bayilmasayisi
value="kiloKaybi" id="kilo-kaybi" name="sikayetler[]"
value="ates" id="ates" name="sikayetler[]"
value="bas" id="bas" name="sikayetler[]"
value="basDonmesi" id="basDonmesi" name="sikayetler[]"
value="basAgrisi" id="basAgrisi" name="sikayetler[]"
value="basAgri1" id="basAgri1" name="sikayetler[]
value="basAgri2" id="basAgri2" name="sikayetler[]"
value="basAgri3" id="basAgri3" name="sikayetler[]"
value="basAgri4" id="basAgri4" name="sikayetler[]
value="basAgri5" id="basAgri5" name="sikayetler[]"
value="basAgri6" id="basAgri6" name="sikayetler[]"
value="karin" id="karin" name="sikayetler[]"
value="mideBulantisi" id="mideBulantisi" name="sikayetler[]"
value="karinAgrisi" id="karinAgrisi" name="sikayetler[]"
value="karin1" name="sikayetler[]" id="karin1">
value="karin2" name="sikayetler[]" id="karin2">
value="karin3" name="sikayetler[]" id="karin3">
value="karin4" name="sikayetler[]" id="karin4">
value="karin5" name="sikayetler[]" id="karin5">
value="karin6" name="sikayetler[]" id="karin6">
type="text" id="sure" name="sure"
"""

lines = data.split("\n")


for val in lines:
    for datas in val.split(" "):
        print(datas.split("="))