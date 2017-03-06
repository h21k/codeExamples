TData <- read.table("alldatacodedworking.csv", header=TRUE, sep="," )

str(TData)

library("psych")
library(ltm)

The.presence.of.my.opponents.motivated.me
\\which( colnames(TData)=="The.presence.of.my.opponents.motivated.me" )

Ignore blank/incomplete command?
x <- subset(x, complete.cases(x)) # Omit missing values?
dfx = dfx[complete.cases(dfx),]

#Measures
Coop <- TData[c(24:32,34:39,41:44,46:48,50:52)]
Comp <- TData[c(10:23)]
Trust <- TData[c(33,40,45,49)]

Com1 <- TData[c(14, 15, 17, 18, 19, 21)]
Com2 <- TData[c(10, 11, 12, 13, 16, 20, 22, 23)]

Coo1  <- TData[c(24, 50, 25, 47, 44)]
Coo2  <- TData[c(29, 30, 52, 31, 35, 41, 37, 39)]
Coo3  <- TData[c(38, 32, 42, 36, 43, 28)]
Coo4  <- TData[c(34, 46, 27, 48, 26, 51)]


#Main Variables
GroupArma <- subset(TData, Game=='Arma')
GroupChiv <- subset(TData, Game=='Chivalry')
GroupCSGO <- subset(TData, Game=='CSGO')
GroupDota <- subset(TData, Game=='Dota')
GroupMnB <- subset(TData, Game=='MnB')
GroupNS <- subset(TData, Game=='NS')
GroupWT <- subset(TData, Game=='WT')
Group29 <- subset(TData, Game=='TNID')

Grouppub <- subset(TData, Game.Type=='pub')
Grouporg <- subset(TData, Game.Type=='org')

GroupWin <- subset(TData, WinorLose=='win')
GroupLoss <- subset(TData, WinorLose=='loss')
GroupDraw <- subset(TData, WinorLose=='draw')


\\Subgroups
#win/lose

CoopWin <- subset(TData[c(7,24:32,34:39,41:44,46:48,50:52)], WinorLose=='win')
CoopLoss <- subset(TData[c(7,24:32,34:39,41:44,46:48,50:52)], WinorLose=='loss')
CoopDraw <- subset(TData[c(7,24:32,34:39,41:44,46:48,50:52)], WinorLose=='draw')

CoopWinArma  <- subset(GroupArma[c(7,24:32,34:39,41:44,46:48,50:52)], WinorLose=='win')
SumFirstCol <- sum(CoopWinArma$I.acted.with.my.team.mates.in.mind)
MeanFirstCol <- mean(CoopWinArma$I.acted.with.my.team.mates.in.mind)
SdFirstCol <- sd(CoopWinArma$I.acted.with.my.team.mates.in.mind)


#Frank's shit
CoopWinArmaOWin  <- subset(CoopWinArma[c(2:26)])
SumTest <- sum(CoopWinArmaOWin, na.rm =TRUE)
# this is the answer ....... vvvvvvvv
RowTest <- rowSums(CoopWinArmaOWin, na.rm = FALSE)
#!!!!
CoopLossArma <- subset(GroupArma[c(7,24:32,34:39,41:44,46:48,50:52)], WinorLose=='loss')
CoopDrawArma <- subset(GroupArma[c(7,24:32,34:39,41:44,46:48,50:52)], WinorLose=='draw')

help(sum)

\\29th

TNTrust <- Group29[c(33,40,45,49)]
TNCoop <- Group29[c(24:32,34:39,41:44,46:48,50:52)]
TNComp <- Group29[c(10:23)]

TNCom1 <- Group29[c(14, 15, 17, 18, 19, 21)]
TNCom2 <- Group29[c(10, 11, 12, 13, 16, 20, 22, 23)]

TNCoo1  <- Group29[c(24, 50, 25, 47, 44)]
TNCoo2  <- Group29[c(29, 30, 52, 31, 35, 41, 37, 39)]
TNCoo3  <- Group29[c(38, 32, 42, 36, 43, 28)]
TNCoo4  <- Group29[c(34, 46, 27, 48, 26, 51)]

TNorg <- subset(Group29, Game.Type=='org')
TNpub <- subset(Group29, Game.Type=='pub')


\\Arma
ArmaTrust <- GroupArma[c(33,40,45,49)]
ArmaCoop <- GroupArma[c(24:32,34:39,41:44,46:48,50:52)]
ArmaComp <- GroupArma[c(10:23)]

ArmaCom1 <- GroupArma[c(14, 15, 17, 18, 19, 21)]
ArmaCom2 <- GroupArma[c(10, 11, 12, 13, 16, 20, 22, 23)]

ArmaCoo1  <- GroupArma[c(24, 50, 25, 47, 44)]
ArmaCoo2  <- GroupArma[c(29, 30, 52, 31, 35, 41, 37, 39)]
ArmaCoo3  <- GroupArma[c(38, 32, 42, 36, 43, 28)]
ArmaCoo4  <- GroupArma[c(34, 46, 27, 48, 26, 51)]

Armaorg <- subset(GroupArma, Game.Type=='org')
Armapub <- subset(GroupArma, Game.Type=='pub')

\\Chiv
ChivTrust <- GroupChiv[c(33,40,45,49)]
ChivCoop <- GroupChiv[c(24:32,34:39,41:44,46:48,50:52)]
ChivComp <- GroupChiv[c(10:23)]

ChivCom1 <- GroupChiv[c(14, 15, 17, 18, 19, 21)]
ChivCom2 <- GroupChiv[c(10, 11, 12, 13, 16, 20, 22, 23)]

ChivCoo1  <- GroupChiv[c(24, 50, 25, 47, 44)]
ChivCoo2  <- GroupChiv[c(29, 30, 52, 31, 35, 41, 37, 39)]
ChivCoo3  <- GroupChiv[c(38, 32, 42, 36, 43, 28)]
ChivCoo4  <- GroupChiv[c(34, 46, 27, 48, 26, 51)]

Chivaorg <- subset(GroupChiv, Game.Type=='org')
Chivpub <- subset(GroupChiv, Game.Type=='pub')

\\CSGO
CSGOTrust <- GroupCSGO[c(33,40,45,49)]
CSGOCoop <- GroupCSGO[c(24:32,34:39,41:44,46:48,50:52)]
CSGOComp <- GroupCSGO[c(10:23)]

CSGOCom1 <- GroupCSGO[c(14, 15, 17, 18, 19, 21)]
CSGOCom2 <- GroupCSGO[c(10, 11, 12, 13, 16, 20, 22, 23)]

CSGOCoo1  <- GroupCSGO[c(24, 50, 25, 47, 44)]
CSGOCoo2  <- GroupCSGO[c(29, 30, 52, 31, 35, 41, 37, 39)]
CSGOCoo3  <- GroupCSGO[c(38, 32, 42, 36, 43, 28)]
CSGOCoo4  <- GroupCSGO[c(34, 46, 27, 48, 26, 51)]

CSGOaorg <- subset(GroupCSGO, Game.Type=='org')
CSGOpub <- subset(GroupCSGO, Game.Type=='pub')

\\Dota
DotaTrust <- GroupDota[c(33,40,45,49)]
DotaCoop <- GroupDota[c(24:32,34:39,41:44,46:48,50:52)]
DotaComp <- GroupDota[c(10:23)]

DotaCom1 <- GroupDota[c(14, 15, 17, 18, 19, 21)]
DotaCom2 <- GroupDota[c(10, 11, 12, 13, 16, 20, 22, 23)]

DotaCoo1  <- GroupDota[c(24, 50, 25, 47, 44)]
DotaCoo2  <- GroupDota[c(29, 30, 52, 31, 35, 41, 37, 39)]
DotaCoo3  <- GroupDota[c(38, 32, 42, 36, 43, 28)]
DotaCoo4  <- GroupDota[c(34, 46, 27, 48, 26, 51)]

Dotaaorg <- subset(GroupDota, Game.Type=='org')
Dotapub <- subset(GroupDota, Game.Type=='pub')


\\MnB
MnBTrust <- GroupMnB[c(33,40,45,49)]
MnBCoop <- GroupMnB[c(24:32,34:39,41:44,46:48,50:52)]
MnBComp <- GroupMnB[c(10:23)]

MnBCom1 <- GroupMnB[c(14, 15, 17, 18, 19, 21)]
MnBCom2 <- GroupMnB[c(10, 11, 12, 13, 16, 20, 22, 23)]

MnBCoo1  <- GroupMnB[c(24, 50, 25, 47, 44)]
MnBCoo2  <- GroupMnB[c(29, 30, 52, 31, 35, 41, 37, 39)]
MnBCoo3  <- GroupMnB[c(38, 32, 42, 36, 43, 28)]
MnBCoo4  <- GroupMnB[c(34, 46, 27, 48, 26, 51)]

MnBaorg <- subset(GroupMnB, Game.Type=='org')
MnBpub <- subset(GroupMnB, Game.Type=='pub')


\\NS
NSTrust <- GroupNS[c(33,40,45,49)]
NSCoop <- GroupNS[c(24:32,34:39,41:44,46:48,50:52)]
NSComp <- GroupNS[c(10:23)]

NSCom1 <- GroupNS[c(14, 15, 17, 18, 19, 21)]
NSCom2 <- GroupNS[c(10, 11, 12, 13, 16, 20, 22, 23)]

NSCoo1  <- GroupNS[c(24, 50, 25, 47, 44)]
NSCoo2  <- GroupNS[c(29, 30, 52, 31, 35, 41, 37, 39)]
NSCoo3  <- GroupNS[c(38, 32, 42, 36, 43, 28)]
NSCoo4  <- GroupNS[c(34, 46, 27, 48, 26, 51)]

NSaorg <- subset(GroupNS, Game.Type=='org')
NSpub <- subset(GroupNS, Game.Type=='pub')


\\WT
WTTrust <- GroupWT[c(33,40,45,49)]
WTCoop <- GroupWT[c(24:32,34:39,41:44,46:48,50:52)]
WTComp <- GroupWT[c(10:23)]

WTCom1 <- GroupWT[c(14, 15, 17, 18, 19, 21)]
WTCom2 <- GroupWT[c(10, 11, 12, 13, 16, 20, 22, 23)]

WTCoo1  <- GroupWT[c(24, 50, 25, 47, 44)]
WTCoo2  <- GroupWT[c(29, 30, 52, 31, 35, 41, 37, 39)]
WTCoo3  <- GroupWT[c(38, 32, 42, 36, 43, 28)]
WTCoo4  <- GroupWT[c(34, 46, 27, 48, 26, 51)]

WTaorg <- subset(GroupWT, Game.Type=='org')
WTpub <- subset(GroupWT, Game.Type=='pub')