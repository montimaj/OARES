options(java.home="C:\\Program Files\\Java\\jre1.8.0_162")
library(RNetLogo)
model.path <- "D:\\SDAM\\Project\\rainfall_ssa.nlogo"
nlDir <- "C:\\Program Files\\NetLogo 6.0.2\\app"
setwd(nlDir)
nl.path <- getwd()
NLStart(nl.path,gui = TRUE,nl.jar='netlogo-6.0.2.jar')
NLLoadModel(model.path)
NLCommand("set draw? false")    
NLCommand("set erosion? true")
NLCommand("set show_water_amount? false")
NLCommand("set show_elevation_change? false") 
runoff=c(1:365)
day=c(1:365)
rain_rate=read.csv(file="D:\\SDAM\\Project\\data\\weather_2013.csv", header=TRUE, sep=",")
for(i in 1:365) {
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
	runoff[i]=NLReport("count turtles * ( 0.55 + random-float 0.45 )")
}
print(runoff)
plot(runoff, xlab="Day", col="blue")
lines(runoff, col="#77dbee")




