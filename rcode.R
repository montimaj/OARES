#options(java.home="C:\\Program Files\\Java\\jre1.8.0_162")
library(RNetLogo)
model.path <- "/home/monti/Documents/IIRS_ITC/Rainfall_ABM/rainfall_ssa.nlogo"
nlDir <- "/home/monti/Downloads/SW/NetLogo-6.0.2/app"
setwd(nlDir)
nl.path <- getwd()
NLStart(nl.path,gui = TRUE,nl.jar='netlogo-6.0.2.jar')
NLLoadModel(model.path)
NLCommand("set draw? false")    
NLCommand("set erosion? true")
NLCommand("set show_water_amount? false")
NLCommand("set show_elevation_change? false")
rain_rate=read.csv(file="/home/monti/Documents/IIRS_ITC/Rainfall_ABM/Data/Weather_Data/weather.csv", header=TRUE, sep=",")
curve_number=read.csv(file="/home/monti/Documents/IIRS_ITC/Rainfall_ABM/Data/Soil_Data/curve_number.csv", header=TRUE, sep=",")
b_soil_percent=0.6456
c_soil_percent=1-b_soil_percent
avg_cn=round(mean(curve_number$B)*b_soil_percent + mean(curve_number$C)*c_soil_percent)
S=25400/avg_cn - 254
numdays=length(rain_rate$Precipitation)
runoff=numeric(numdays)
for(i in 1:numdays) {
	rr=round(rain_rate$Precipitation[i])
	wh=runif(1,1,4)
	if(rr==0){
		wh=0
	} else if(rr>=70){
		wh=runif(1,4,6)
	}
	wh=round(wh)
	NLCommand("set rain-rate", rr)
	NLCommand("set water-height", wh)
	NLCommand("setup")
	NLCommand("go")
	P=NLReport("count turtles")
	if(P>0.2*S)
	  runoff[i]=((P-0.2*S)^2)/(P+0.8*S)
}
plot_mat=matrix(nrow=numdays, ncol=2)
plot_mat[,1]=paste('',rain_rate$Date)
plot_mat[,2]=runoff
print(runoff)
plot(runoff, xlab="Day", ylab='Runoff',col="blue")
axis(1, at=1:numdays, labels=rain_rate$Date)
plot(plot_mat[,1], plot_mat[,2], xlab="Date", ylab='Runoff', col="blue")
lines(plot_mat[,1], plot_mat[,2], col="#77dbee")
lines(runoff, col="#77dbee")
write.table(plot_mat, file='/home/monti/Documents/IIRS_ITC/Rainfall_ABM/Outputs/runoff.csv',sep=",")