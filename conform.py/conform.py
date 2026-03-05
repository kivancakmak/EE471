# This script is written by Kıvanç Çakmak



def pleaseConformOnepass(caps):
    start = 0
    for i in range(1, len(caps)):
        if caps[i] != caps[start]:
            if i - start > 0:
                print("People in positions", start, "through", i-1, "flip your caps!")
            start = i

    if caps[start] == 'F':
        print("People in positions", start, "through", len(caps)-1, "flip your caps!")
        