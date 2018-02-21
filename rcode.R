library(RNetLogo)
args = commandArgs(trailingOnly=TRUE)

NLStart(args[1],gui = TRUE,nl.jar='netlogo-6.0.2.jar')
NLLoadModel(args[2])
NLCommand("set input-dem", args[3])
NLCommand("set out-resampled-file", args[4])
NLCommand("set out-eroded-file", args[5])
NLCommand("set draw? false")    
NLCommand("set erosion? true")
NLCommand("set show_water_amount? false")
NLCommand("set show_elevation_change? false")
NLCommand("setup")
NLCommand("export_original")

rain_rate=read.csv(file=args[6], header=TRUE, sep=",")
curve_number=read.csv(file=args[7], header=TRUE, sep=",")
b_soil_percent=0.6456
c_soil_percent=1-b_soil_percent
avg_cn=round(mean(curve_number$B)*b_soil_percent + mean(curve_number$C)*c_soil_percent)
S=25400/avg_cn - 254
numdays=length(rain_rate$Precipitation)
runoff=numeric(numdays)
for(i in 1:numdays) {
	P=round(rain_rate$Precipitation[i])
	if(P>0.2*S) {
	  runoff[i]=((P-0.2*S)^2)/(P+0.8*S)
	  wh=runif(1,1,4)
	  if(P>=70) wh=runif(1,4,6)
	  wh=round(wh)
	  rr=1
	  total_water=0
	  while (total_water<=P) {
	    NLCommand("set rain-rate", rr)
	    NLCommand("set water-height", wh)
	    NLCommand("go")
	    total_water=NLReport("count turtles")
	    rr=rr+1
	  }
	  NLCommand("clear_turtles")
	}
}
NLCommand("export_eroded")
plot_mat=matrix(nrow=numdays, ncol=2)
plot_mat[,1]=paste(rain_rate$Date)
plot_mat[,2]=runoff
print(runoff)
write.table(plot_mat, file=args[8],sep=",")