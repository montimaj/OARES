def clean_dem_file(input):
    fp=open(input,'r')
    data=fp.read()
    lines=data.split('"nl"')
    fp.close()
    values=[]
    new_lines=[]
    numlines=len(lines)-2
    for line in lines[:numlines]:
        line=line.strip()
        new_lines.append(line)
        values.append(len(line.split(' ')))
    return max(values), numlines, new_lines

def read_lines(fp, n):
    lines=[]
    while n>0:
        lines.append(fp.readline())
        n-=1
    fp.close()
    return lines[2:]

def generate_new_dem_file(original_dem,output, data):
    params=read_lines(open(original_dem, 'r'), 6)
    fp2=open(output,'w')
    ncols='ncols         '+str(data[0])
    nrows='nrows         '+str(data[1])
    fp2.write(ncols+'\n'+nrows+'\n')
    for param in params:
        fp2.write(param)
    for d in data[2]:
        fp2.write(d+'\n')
    fp2.close()

ncols, nrows, new_lines =clean_dem_file("D:/SDAM/Project/data/result.asc")
generate_new_dem_file("D:/SDAM/Project/data/asan_dem.asc","D:/SDAM/Project/data/out.asc", (ncols,nrows,new_lines))
