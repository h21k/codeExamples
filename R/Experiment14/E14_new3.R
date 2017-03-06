setwd("~/Dropbox/R/E14new3")
#fix(Clear)
E11Data <- read.table("E11Data6.csv", header=TRUE, sep="," )
#E8Data
#head(E8Data)
#structure of the data - types!
str(E11Data)

#Error - Rate -------Total Data

TotalNumbersEntered <- sum(E11Data$NumbersTotal)
TotalErrorsMade <- sum(E11Data$ErrorsTotal)
TotalCorrectionsMade <- sum(E11Data$Corrections)
TotalErrorRate <- sum(E11Data$ErrorsTotal)*100/sum(E11Data$NumbersTotal)

#--------------------Groups

ClearLetters <- subset(E11Data, Condition=='CL')   
ClearNumbers <- subset(E11Data, Condition=='CN') 
ObscuredLetters <- subset(E11Data, Condition=='OL')
ObscuredNumbers<- subset(E11Data, Condition=='ON')

EnglishSpeaking <- subset(E11Data, EnglishCountry=='Yes')
NonEnglishSpeaking <- subset(E11Data, EnglishCountry=='No')

Clear <- subset(E11Data, Visibility=='clear')   
Obscured <- subset(E11Data, Visibility=='obscured')
Letters <- subset(E11Data, Audio=='letters')   
Numbers <- subset(E11Data, Audio=='numbers') 

mean(Clear$NumbersTotal)
mean(Obscured$NumbersTotal)
mean(Letters$NumbersTotal)
mean(Numbers$NumbersTotal)

sd(Clear$NumbersTotal)
sd(Obscured$NumbersTotal)
sd(Letters$NumbersTotal)
sd(Numbers$NumbersTotal)

mean(Clear$ErrorsTotal)
mean(Obscured$ErrorsTotal)
mean(Letters$ErrorsTotal)
mean(Numbers$ErrorsTotal)

sd(Clear$ErrorsTotal)
sd(Obscured$ErrorsTotal)
sd(Letters$ErrorsTotal)
sd(Numbers$ErrorsTotal)

mean(Clear$Corrections)
mean(Obscured$Corrections)
mean(Letters$Corrections)
mean(Numbers$Corrections)

sd(Clear$Corrections)
sd(Obscured$Corrections)
sd(Letters$Corrections)
sd(Numbers$Corrections)


#--------------------TotalNumbers

TotalNumbersClearLetters <- sum(ClearLetters$NumbersTotal)
TotalNumbersClearNumbers <- sum(ClearNumbers$NumbersTotal)
TotalNumbersObscuredLetters <- sum(ObscuredLetters$NumbersTotal)
TotalNumbersObscuredNumbers <- sum(ObscuredNumbers$NumbersTotal)

#--------------------Errors Details

TotalErrorsClearLetters <- sum(ClearLetters$ErrorsTotal)
MeanErrorsClearLetters <- mean(ClearLetters$ErrorsTotal)
SDErrorsClearLetters <- sd(ClearLetters$ErrorsTotal)

TotalErrorsClearNumbers <- sum(ClearNumbers$ErrorsTotal)
MeanErrorsClearNumbers <- mean(ClearNumbers$ErrorsTotal)
SDErrorsClearNumbers <- sd(ClearNumbers$ErrorsTotal)

TotalErrorsObscuredLetters <- sum(ObscuredLetters$ErrorsTotal)
MeanErrorsObscuredLetters <- mean(ObscuredLetters$ErrorsTotal)
SDErrorsObscuredLetters <- sd(ObscuredLetters$ErrorsTotal)

TotalErrorsObscuredNumbers <- sum(ObscuredNumbers$ErrorsTotal)
MeanErrorsObscuredNumbers <- mean(ObscuredNumbers$ErrorsTotal)
SDErrorsObscuredNumbers <- sd(ObscuredNumbers$ErrorsTotal)

#---------------------Numbers Details

TotalNumbersClearLetters <- sum(ClearLetters$NumbersTotal)
MeanNumbersClearLetters <- mean(ClearLetters$NumbersTotal)
SDNumbersClearLetters <- sd(ClearLetters$NumbersTotal)

TotalNumbersClearNumbers <- sum(ClearNumbers$NumbersTotal)
MeanNumbersClearNumbers <- mean(ClearNumbers$NumbersTotal)
SDNumbersClearNumbers <- sd(ClearNumbers$NumbersTotal)

TotalNumbersObscuredLetters <- sum(ObscuredLetters$NumbersTotal)
MeanNumbersObscuredLetters <- mean(ObscuredLetters$NumbersTotal)
SDNumbersObscuredLetters <- sd(ObscuredLetters$NumbersTotal)

TotalNumbersObscuredNumbers <- sum(ObscuredNumbers$NumbersTotal)
MeanNumbersObscuredNumbers <- mean(ObscuredNumbers$NumbersTotal)
SDNumbersObscuredNumbers <- sd(ObscuredNumbers$NumbersTotal)

MeanMean <- sum(MeanNumbersClearLetters,MeanNumbersClearNumbers)
MeanMeanMean <- mean(MeanMean)
#---------------------Corrections Detail

TotalCorrectionsClearLetters <- sum(ClearLetters$Corrections)
TotalCorrectionsClearNumbers <- sum(ClearNumbers$Corrections)
TotalCorrectionsObscuredLetters <- sum(ObscuredLetters$Corrections)
TotalCorrectionsObscuredNumbers <- sum(ObscuredNumbers$Corrections)

TotalCorrectionsClearLetters <- sum(ClearLetters$Corrections)
MeanCorrectionsClearLetters <- mean(ClearLetters$Corrections)
SDCorrectionsClearLetters <- sd(ClearLetters$Corrections)

TotalCorrectionsClearNumbers <- sum(ClearNumbers$Corrections)
MeanCorrectionsClearNumbers <- mean(ClearNumbers$Corrections)
SDCorrectionsClearNumbers <- sd(ClearNumbers$Corrections)

TotalCorrectionsObscuredLetters <- sum(ObscuredLetters$Corrections)
MeanCorrectionsObscuredLetters <- mean(ObscuredLetters$Corrections)
SDCorrectionsObscuredLetters <- sd(ObscuredLetters$Corrections)

TotalCorrectionssObscuredNumbers <- sum(ObscuredNumbers$Corrections)
MeanCorrectionsObscuredNumbers <- mean(ObscuredNumbers$Corrections)
SDCorrectionsObscuredNumbers <- sd(ObscuredNumbers$Corrections)


#---------------------RATE Detail

TotalRateClearLetters <- sum(ClearLetters$ErrorRate)
TotalRateClearNumbers <- sum(ClearNumbers$ErrorRate)
TotalRateObscuredLetters <- sum(ObscuredLetters$ErrorRate)
TotalRateObscuredNumbers <- sum(ObscuredNumbers$ErrorRate)

TotalCorrectionsClearLetters <- sum(ClearLetters$ErrorRate)
MeanCorrectionsClearLetters <- mean(ClearLetters$ErrorRate)
SDCorrectionsClearLetters <- sd(ClearLetters$ErrorRate)

TotalCorrectionsClearNumbers <- sum(ClearNumbers$ErrorRate)
MeanCorrectionsClearNumbers <- mean(ClearNumbers$ErrorRate)
SDCorrectionsClearNumbers <- sd(ClearNumbers$ErrorRate)

TotalCorrectionsObscuredLetters <- sum(ObscuredLetters$ErrorRate)
MeanCorrectionsObscuredLetters <- mean(ObscuredLetters$ErrorRate)
SDCorrectionsObscuredLetters <- sd(ObscuredLetters$ErrorRate)

TotalCorrectionssObscuredNumbers <- sum(ObscuredNumbers$ErrorRate)
MeanCorrectionsObscuredNumbers <- mean(ObscuredNumbers$ErrorRate)
SDCorrectionsObscuredNumbers <- sd(ObscuredNumbers$ErrorRate)







#---------------------Boxplots
boxplot(E11Data$NumbersTotal~E11Data$Condition,data=E11Data,ylab = expression(bold(Numbers~Entered)),xlab = expression(bold(Experimental~Condition))) 
#boxplot(NumbersTotal ~ Condition, bg="red", col="gray", main="", data=E11Data)
boxplot(E11Data$ErrorsTotal ~ E11Data$Condition, data=E11Data,ylab = expression(bold(Errors~Made)),xlab = expression(bold(Experimental~Condition)))
boxplot(E11Data$Corrections ~ E11Data$Condition, data=E11Data,ylab = expression(bold(Corrections~Made)),xlab = expression(bold(Experimental~Condition))) 
boxplot(E11Data$ErrorRate ~ E11Data$Condition, data=E11Data,ylab = expression(bold(Error~Rate(Errors/Total~numbers~entered))),xlab = expression(bold(Experimental~Condition))) 
#boxplot(E11Data$NumbersTotal ~ E11Data$Condition, bg="red", col="gray", outcol="gray", main="")
#vioplot(E8Data$ErrorsTotal ~ E8Data$Condition, main="")
#boxplot(E11Data$Corrections ~ E11Data$Condition)
#boxplot(E6Data$Corrections ~ E6Data$Group, main="Total corrections by group")
#boxplot(E6Data$Rate ~ E6Data$Group, main="Error-Rate by group")

#---------------------Means / SDs


mean(ClearLetters$ErrorsTotal)
sd(ClearLetters$ErrorsTotal)

mean(ClearNumbers$ErrorsTotal)
sd(ClearNumbers$ErrorsTotal)

mean(ObscuredLetters$ErrorsTotal)
sd(ObscuredLetters$ErrorsTotal)

mean(ObscuredNumbers$Rate)
sd(ObscuredNumbers$Rate)

#mean(GroupMedium$Rate)
#sd(GroupMedium$Rate)

#mean(GroupObscured$Rate)
#sd(GroupObscured$Rate)

#mean(GroupClear$TotalNumbers)
#sd(GroupClear$TotalNumbers)

#mean(GroupMedium$TotalNumbers)
#sd(GroupMedium$TotalNumbers)

#mean(GroupObscured$TotalNumbers)
#sd(GroupObscured$TotalNumbers)

#mean(GroupClear$Corrections)
#sd(GroupClear$Corrections)

#mean(GroupMedium$Corrections)
#sd(GroupMedium$Corrections)

#mean(GroupObscured$Corrections)
#sd(GroupObscured$Corrections)


#---------------------------------------------------------------------#

#--------------MAIN STATISTICAL TEST OF SIGNIFICANCE------------------#

#friedman.test(E11Data$Corrections, E11Data$Condition, E11Data$Participant )

#Create an ANOVA table
#E9Result.aov = aov(Corrections~(Source*Display)+Error(Participant/(Source*Display)),E11Data)
E11ResultCorrections.aov = aov(Corrections~Visibility*Audio,E11Data)
summary(E11ResultCorrections.aov)
boxplot(Corrections~Visibility*Audio,data=E11Data)
plot(Corrections~Visibility*Audio,data=E11Data)


#list <- rep(c(1,2,3,4),10)
#E11Data$List <- list
#boxplot(E11Data$ErrorsTotal ~ E11Data$List)
#boxplot(E11Data$ErrorsTotal ~ E11Data$Condition)
#friedman.test(E11Data$ErrorsTotal, E11Data$List, E11Data$Participant )


#Create an ANOVA table
#E9Result.aov = aov(ErrorsTotal~(Source*Display)+Error(Participant/(Source*Display)),E11Data)
E11ResultErrors.aov = aov(ErrorsTotal~(Visibility*Audio),E11Data)
summary(E11ResultErrors.aov)
boxplot(ErrorsTotal~Visibility*Audio,data=E11Data)
plot(ErrorsTotal~Visibility*Audio,data=E11Data)
TukeyHSD(E11ResultErrors.aov)
t.test(E11Data$ErrorsTotal ~ E11Data$Visibility)
#Kruskal Wallis test on the total errors made
#friedman.test(E8Data$ErrorsTotal, E8Data$Condition, E8Data$Participant )
#friedman.test(E8Data$NumbersTotal, E8Data$Condition, E8Data$Participant )
#Kruskal Wallis test on the total numbers entered by participants
#friedman.test(E8Data$TotalNumbers ~ E8Data$Condition)
#Kruskal Wallis test on the total number of detected & corrected errors
#kruskal.test(E6Data$Corrections ~ E6Data$Group)
#Kruskal Wallis test on the rates? total error / total numbers entered 
#friedman.test(E8Data$TotalRate ~ E8Data$Condition)
E11ResultNumbers.aov = aov(NumbersTotal~(Visibility*Audio),E11Data)
summary(E11ResultNumbers.aov)
boxplot(NumbersTotal~Visibility*Audio,data=E11Data)

#ERROR RATE HERE
E11ResultRate.aov = aov(ErrorRate~Visibility*Audio,E11Data)
summary(E11ResultRate.aov)
boxplot(ErrorRate~Visibility*Audio,data=E11Data)
plot(ErrorRate~Visibility*Audio,data=E11Data)

#WilcoxNumbers NON PARAMETRIC CHECK IF THE ANOVAS WERE RIGHT - IF IT IS A TRUE EFFECT
wilcox.test(NumbersTotal~Visibility,data=E11Data)
wilcox.test(ErrorsTotal~Visibility,data=E11Data)
wilcox.test(ErrorRate~Visibility,data=E11Data)
wilcox.test(Corrections~Audio,data=E11Data)

#--------------ENSLISH & NON-ENGLISH-----------------------
#Numbers
#E11ResultEnglish.aov = aov(EnglishSpeaking$NumbersTotal~(EnglishSpeaking$Visibility*EnglishSpeaking$Audio),EnglishSpeaking)
#summary(E11ResultEnglish.aov)
#boxplot(EnglishSpeaking$NumbersTotal~EnglishSpeaking$Visibility*EnglishSpeaking$Audio,data=E11Data$EnglishSpeaking)

#E11ResultNonEnglish.aov = aov(NonEnglishSpeaking$NumbersTotal~(NonEnglishSpeaking$Visibility*NonEnglishSpeaking$Audio),NonEnglishSpeaking)
#summary(E11ResultNonEnglish.aov)
#boxplot(NonEnglishSpeaking$NumbersTotal~NonEnglishSpeaking$Visibility*NonEnglishSpeaking$Audio,data=E11Data$NonEnglishSpeaking)

#Errors
#E11ResultEnglish.aov = aov(EnglishSpeaking$ErrorsTotal~(EnglishSpeaking$Visibility*EnglishSpeaking$Audio),EnglishSpeaking)
#summary(E11ResultEnglish.aov)
#boxplot(EnglishSpeaking$ErrorsTotal~EnglishSpeaking$Visibility*EnglishSpeaking$Audio,data=EnglishSpeaking)

#E11ResultNonEnglish.aov = aov(NonEnglishSpeaking$ErrorsTotal~(NonEnglishSpeaking$Visibility*NonEnglishSpeaking$Audio),NonEnglishSpeaking)
#summary(E11ResultNonEnglish.aov)
#boxplot(NonEnglishSpeaking$ErrorsTotal~NonEnglishSpeaking$Visibility*NonEnglishSpeaking$Audio,data=E11Data$NonEnglishSpeaking)

#Corrections
#E11ResultEnglish.aov = aov(EnglishSpeaking$Corrections~(EnglishSpeaking$Visibility*EnglishSpeaking$Audio),EnglishSpeaking)
#summary(E11ResultEnglish.aov)
#boxplot(EnglishSpeaking$Corrections~EnglishSpeaking$Visibility*EnglishSpeaking$Audio,data=EnglishSpeaking)

#E11ResultNonEnglish.aov = aov(NonEnglishSpeaking$Corrections~(NonEnglishSpeaking$Visibility*NonEnglishSpeaking$Audio),NonEnglishSpeaking)
#summary(E11ResultNonEnglish.aov)
#boxplot(NonEnglishSpeaking$Corrections~NonEnglishSpeaking$Visibility*NonEnglishSpeaking$Audio,data=E11Data$NonEnglishSpeaking)


#boxplot(E11Data$NumbersTotal~E11Data$EnglishCountry)
#boxplot(E11Data$ErrorsTotal~E11Data$EnglishCountry)

#----------------------------------------------------------

#some discriptive stuff things...
#test <- E6Data$Corrections
# median(test, na.rm = false) #na.rm = remove NA values or not
# > mean(test, na.rm = false)
# boxplot(test, test2, main="dasd", names=c("test","test2"))

#----------FOLLOW-UP TESTS-----------
#kruskalmc(resp=E11Data$Corrections, categ=E11Data$Condition,probs = 0.05, cont=NULL)
#kruskalmc(resp=E6Data$Rate, categ=E6Data$Group,probs = 0.05, cont=NULL)


########################
#Mean and SD of the Age:
#mean(E11Data$Age_n)
#sd(E11Data$Age_n)

########################
#install directly from github repository
#library(devtools)
#install_github('shiny', 'rstudio')
#install_github('R-Websockets', 'rstudio')
#nrow(E6Data) number of rows in dataframs - same for colums ncol()