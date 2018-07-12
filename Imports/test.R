library(RNetLogo)
args = commandArgs(trailingOnly=TRUE)

NLStart(args[1],gui = TRUE,nl.jar='netlogo-6.0.2.jar')
NLLoadModel(args[2])