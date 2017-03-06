d <- read.table(text='   V1 V2  V3  V4  V5  V6  V7
1 1 a 2.0 3.0 4.0 9.0 6.0
2 1 b 0.1 0.2 0.4 0.5 0.6
3 1 c 0.1 0.3 0.4 0.5 0.8
4 1 d 0.1 0.2 0.3 0.6 0.9
5 2 a 1.0 2.0 3.0 4.0 5.0
6 2 b 0.1 0.4 0.5 0.6 0.7
7 2 c 0.1 0.2 0.3 0.5 0.8
8 2 d 0.2 0.3 0.6 0.7 0.9', header=TRUE)
 
v <- c(2, 3)

doNice <- function(d, v, text='b') {   
    # adding a new column VV of NA values at the end of table d
    d$VV <- apply(d,1,function(row) NA);
    # pliting table by V1
    d.split <- split(d, d$V1);
    # getting rid of the final values of the vector (these out of number of rows in d)
    z <- v[1:min(length(v), max(d["V1"]))];

    mapply(function(x, y, n) {
              # x - a set of rows with the same value V1
              # y - vector
              # n - number of columns in table
                            
              # r - first row from x
              r <- x[1, -(1:2)]
              
              # match row
              matchRowId <- which.min(abs(y-r))
              
              x2 <- setNames(              
              # get such values from x:
              # columns 1, 2 and the one that contains closest value to y
              # (which.min gives index of a minimum from vector)
              x[, c(1:2, 2 + match(r[matchRowId], r, nomatch = n - 2))],
              c('V1', 'V2', 'MATCH'))
              
              # index of "next higher one"
              indexMax <- which.max(x2[-(1:1),3]) + 1
              indexMax <- which(x2[,2] == text)
                     
              # sum of every -V7 in x   
              sums <- rowSums(x[, (2+matchRowId+1):(length(x) - 1)])
              
              # changing the value
              x2[indexMax,3] <- sums[indexMax]
              x2              
              }, d.split, z, length(d), SIMPLIFY=FALSE)
}

       
                      
nice <- function(d, v, text) {
    res <- unsplit(doNice(d,v,text), d$V1);
    res$N <- apply(res, 1, function(row) v[as.numeric(row[1])])
    res
}

#e<-read.table("data.txt", header=FALSE, sep = " ", fill = TRUE, col.names = paste0("V", seq_len(5000)))
