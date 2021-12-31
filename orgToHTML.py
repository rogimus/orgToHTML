#!/usr/bin/env python3

def boilerplate(f,p):
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang=\"en\">\n")
    f.write("  <head>\n")
    f.write("    <meta charset=\"UTF-8\">\n")
    f.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    f.write("    <meta http-equiv=\"X-UA-Compatible\" content=\"ie=edge\">\n")
    f.write("    <title>"+p[:-4]+"</title>\n")
    f.write("    <link rel=\"stylesheet\" href=\"style.css\">\n")
    f.write("    <script type=\"text/javascript\" async\n")
    f.write("src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-MML-AM_CHTML\">\n")
    f.write("</script>\n")
    f.write("  </head>\n")
    f.write("  <body>\n")
    f.write("  <content>\n")
    f.write("   <p>\n")

def backboiler(f):
    f.write("</p>\n")
    f.write("</content>\n")
    f.write("</body>\n")
    f.write("</html>\n")

def divs(f,nf):
    i=0
    l = f.readlines()
    while i < len(l):
        lines = l[i]
        if lines != "\n":
            if lines[:15] == "#+BEGIN_theorem":
                nf.write("   <div class=\"theorem\">\n")
                if lines[15:] != "":
                    nf.write("   <div class=\"thhead\">\n")
                    nf.write("    "+lines[15:]+"\n")
                    nf.write("   </div>")
                else:
                    nf.write("   <div class=\"thhead\">\n")
                    nf.write("    Theorem\n")
                    nf.write("   </div>\n")
            elif lines[:13] == "#+BEGIN_proof":
                nf.write("   <div class=\"proof\">\n")
                if lines[13:] != "":
                    nf.write("   <div class=\"thhead\">\n")
                    nf.write("    "+lines[13:])
                    nf.write("   </div>\n")
                else:
                    nf.write("   <div class=\"thhead\">\n")
                    nf.write("    Proof\n")
                    nf.write("   </div>\n")
            elif lines[:13] == "#+END_theorem":
                nf.write("   </div>\n")
            elif lines[:11] == "#+END_proof":
                nf.write("   </div>\n")
            elif lines[1] == ".":
                nf.write("    <ol>\n")
                nf.write("      <li>"+lines[2:]+"</li>\n")
                t=1
                while t==1:
                    if l[i+1][1] == ".":
                        i = i+1
                        lines = l[i]
                        nf.write("      <li>"+lines[2:]+"</li>\n")
                    else: 
                        t=0
                        nf.write("    </ol>\n")
            else:
                nf.write(lines)
            i = i+1
        else:
            i = i+1
            nf.write("    </p>\n    <p>")

def main():
    path = input("file name: ")
    newpath = path[:-3]+"html"
    file = open(path)
    newfile = open(newpath, "x")
    boilerplate(newfile,path)
    divs(file, newfile)
    backboiler(newfile)

if __name__ == "__main__":
    main()
