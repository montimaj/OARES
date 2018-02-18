def read_lines(fp, n):
    lines=[]
    while n>0:
        lines.append(fp.readline())
        n-=1
    fp.close()
    return lines

def clean_dem_file(abm_generated_dem):
    fp=open(abm_generated_dem,'r')
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

def generate_new_dem_file(original_dem, abm_generated_dem, output_dem):
    params=read_lines(open(original_dem, 'r'), 6)
    cols, rows, data = clean_dem_file(abm_generated_dem)
    fp2=open(output_dem,'w')
    ncols='ncols         '+str(cols)
    nrows='nrows         '+str(rows)
    fp2.write(ncols+'\n'+nrows+'\n')
    for param in params[2:]:
        fp2.write(param)
    for d in data:
        fp2.write(d+'\n')
    fp2.close()
    cellsize = float(params[4].strip().split(' ')[-1])
    return cellsize