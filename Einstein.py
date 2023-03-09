mas = int(input("Enter Mass value: "))                                          # get mass value
lightSpeed = 300000000                                                          # light speed
masDim = input("Please select type of mass scale: (kg, g, t, lb) ")             # get mass scale
enerDim = input("Please select type of enery scale:(j, kj, wh, kwh) ")          # get energy scale
massDims = {                                                                    # mass scale values
        "kg" : 1,
        "g" : 0.001,
        "t" : 1000,
        "lb" : 0.453592,
        "measurment" : "Mass"
    }
energyDims = {                                                                  # energy scale value
        "j" : 1,
        "kj" : 0.001,
        "wh" : 0.000277778,
        "kwh" : 0.00000027778,
        "measurment" : "Energy"
    }

def converter(source, val, dim):                                                # converter function
    dim = dim.strip().lower()                                                       # text formating
    if dim in source:
        return val * source[dim]
    else:
        return "Wrong " + source["measurment"] + " scale"

def einstein(s, m, d):                                                          # calculate einstein formula
    if m * lightSpeed **2 is type(int) or type(float) and d in s:
        return m*lightSpeed**2
    else:
        return converter(s, m, d)

def finalResult(s, m, d, s1, d1):                                               # need consultation
    if einstein(s,m,d) is type(int) or type(float) and d1 in s1:
        return converter(s1,einstein(s,m,d),d1)
    else:
        return converter(s1,einstein(s,m,d),d1)

print(finalResult(massDims,mas,masDim,energyDims,enerDim))                      # get final result
