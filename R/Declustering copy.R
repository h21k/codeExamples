# Declustering

#input
#   y    : observed data
#   pN   : the percentage of the data set, to be declustered  (en général pN=10%)
#   Nu   : number of points taken out above the chosen threshold
#
# output
#     valuesOUT : values above the threshold
#     indexOut : corresponding index
#     seuil : threshold correponding to Nu
#     YDC : the declustered data set
#     IndexDC : corresponding index (compared to the original data set)


seriedeclus<-function(y,pN,Nu)
{
 library(chron)
 library(evir)
 vdNu<-rep(0,Nu)
 N<-round(length(y)*pN)+1
 pn<-rep(0,N)
 y_index=data.frame(times=1:length(y),y)
 dpn<- y_index[,1]; index= y_index[,1]
 niv <- findthresh(y,N)
 dpn <-dpn[which(y>niv)]
 pn<- y[which(y>niv)]
 attributes(pn)$times<-dpn
 vd<- decluster(pn,1,picture = F)
 dvd <- attr(vd,"times")
 nbvalde<-length(vd)
 ifelse(nbvalde>=Nu ,seuilNu<- findthresh(vd,Nu), ((seuilNu<-niv) & (Nu=nbvalde)))
 dvndNu<-dpn[which(pn>seuilNu)]
 dvdNu<-dvd[which(vd>seuilNu)]
 non<-dvndNu
 nn<-length(non)
 Inum<-rep(0,nn)
 for(ij in 1:nn) {Inum[ij]<-which(index==non[ij])}
 dc<-index[-Inum]
 dcv<-y[-Inum]
nd<-length(dc)
Dnu<-index[Inum]
Vnu<-y[Inum]
write(dcv,file=paste(repertory,set,"_declust.txt", sep=""), ncolumns =1,append=F)
out<-list(seuil=seuilNu,indexOut=Dnu,valuesOUT=Vnu,IndexDC=dc,YDC=dcv)
}

# Apply gpd.wcet on data y=seriedeclus(y,pN,Nu)$YDC


