setwd("~/Desktop/R_Script")

source("fit_proxima.R")

dadda <- read.table("data_dev/king.wcet.dat")
dadda2 <- read.table("data_dev/s2.dat")
iid <- read.table("iid.txt")

da <- dadda$V1
da2 <- dadda2$V1
iid<-iid$V1
#write.table(da, "mydata.txt", sep="\t")
write.table(da, "ffmpeg2.txt", col.names = F, row.names = F)
write.table(da2, "ffmpeg1.txt", col.names = F, row.names = F)

#do_proxima(da, "probabilities.txt", "method.txt")
do_proxima("ffmpeg1.txt", "probabilities.txt", "method.txt")
do_proxima("f.txt", "probabilities.txt", "method.txt")
do_proxima("iid.txt", "probabilities.txt", "method.txt")





A1<-do_GPD(da2) #works
A2<-best_size_block_GEV(da2,"s","s")
EVT<-best_size_block_GEV(da2, "v", "6")
my_plot_GEV(da2,EVT[[1]],EVT[[3]],EVT[[4]],results,set)
