rtc=function(row.to.change){# <- 1
  (new.row <- seq(min(d[row.to.change,c(-1, -2)], na.rm=TRUE), max(d[row.to.change,c(-1,-2)], na.rm=TRUE)))
  (num.add <- length(new.row) - ncol(d) + 2)
  # [1] 3
  if (num.add <= 0) {
    new.row <- c(new.row, rep(NA, -num.add))
  }
  new.row
}

d <- read.table(text='   V1 V2  V3  V4  V5  V6  V7
1 1 a 2 3 4 9 6
                2 1 b 2 2 4 5 NA
                3 1 c 1 3 4 5 8
                4 1 d 1 2 3 6 9
                5 2 a 1 2 3 4 5
                6 2 b 1 4 5 6 7
                7 2 c 1 2 3 5 8
                8 2 d 2 3 6 7 9', header=TRUE)

#newr=lapply(1:nrow(d),rtc) # for the hole data
# for specific condition, like lines with "b" in V2 change to:
newr=lapply(1:nrow(d),function(z)if(d$V2[z]=="c")rtc(z) else as.numeric(d[z,c(-1, -2)])) 
mxl=max(sapply(newr,length))
newr=lapply(newr,function(z)if(length(z)<mxl)c(z,rep(NA,mxl-length(z))) else z)
if (ncol(d)-2 < mxl) {
  d <- cbind(d, replicate(mxl-ncol(d)+2, rep(NA, nrow(d))))
}
d[,c(-1, -2)] <- do.call(rbind,newr)
colnames(d) <- paste0("V", seq_len(ncol(d)))
