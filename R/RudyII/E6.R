
setwd("/Users/kenobi/Dropbox/R/E6/")
#fix(Clear)
E6Data <- read.table("dataHacs2.csv", header=TRUE, sep="," )
#E6Data
#head(E6Data)
#structure of the data - types!
str(E6Data)
#E6Data$Sex <- factor(E6Data$Sex) # tell R to set the data to a factor
#define factors as labels
#E6Data$Sex <- factor(E6Data$Sex, levels=c(0,1), labels=c("M", "F")) 
#access variables within the dataframe with using $ so this makes a copy of Age
#E6Data$Test <- E6Data$Age 

#Describing the data - lets check if the immersion questionairs is working
#first we produce barcharts using the table() function it counts up the different values
#Qn1count <- table(ImmData$Qn1)
#Qn1count # to see a list of different values of Qn1
#barplot(Qn1count, main="Answers to Qn1") //put this into a barchart

#what if one question does not have all values listed (for exampel 4 does not have 1s)
#so same thing again:

#Qn4count <- table(ImmData$Qn4)
#Qn4count // to see a list of different values of Qn1
#barplot(Qn4count, main="Answers to Qn4") //put this into a barchart

#UHhh but Question 4 has a 1  in there try question 5

#Qn4count <- table(ImmData$Qn4)
#Qn4count // to see a list of different values of Qn1
#barplot(Qn4count, main="Answers to Qn1") //put this into a barchart

#anyways 5 also have 1s so just in case you would transfer it into a factor
#ImmData$Qn4 <- factor(ImmData$Qn4, levels=c(1,2,3,4,5)
#now it should be included with noone aswering 1s

#NOW DISCRIPTIVE STATISTICS IEQ 13-43
#so we make a vector first called ieqcols
#ieqcols <- c(13:43)
#check ieqcols
#ieqcols
#Now make a subset of the ImmData which is just the IEQ data with:
#IEQData <- ImmData[ieqcols]
#Check you’ve got it right with head(IEQData). Now we can summarise the data with: summary(IEQData)
#head(IEQData)
#then summarise
#summary(IEQData)
#extract a small subset of immersion data
#ImmScores <- ImmData[c("Sex", "Task", "TotalImm", "CI", "EI", "RWD", "Ch", "Ctrl" ) ]
#we need the function describe() now
#fofund in tools-install packages psych()
#describe(ImmScores)
#barchart of immersion scores so that we can see the normal distribution
#hist(ImmScores$TotalImm)
#use help(hist) for more info
#describe.by(ImmScores, ImmScores$Task) LEFT THIS IS NUMBER 12
#then BOXPLOT
#boxplot(TotalImm∼Task, data=ImmScores)
GroupClear <- subset(E6Data, Group=='clear')   
GroupMedium <- subset(E6Data, Group=='medium') 
GroupObscured <- subset(E6Data, Group=='obscured')
#Does not work with 3 groups here because medium has one more row! 
#mydataframe <- data.frame(GroupClear$ErrorsTotal, GroupObscured$ErrorsTotal)
#test new plotting
#boxplot(E6Data$ErrorsTotal ~ E6Data$Group, main="Total errors by group", outlier.colour = "green", outlier.shape = 16, outlier.size = 2)

plot(E6Data$NumbersEntered ~ E6Data$Group, main="Total numbers entered by group")

plot(E6Data$NumbersEntered, E6Data$ErrorsTotal, main="Scatterplot Example", 
     xlab="Numbers ", ylab="Errors ", pch=19)
abline(lm(E6Data$NumbersEntered~E6Data$ErrorsTotal), col="red") # regression line (y~x) 
lines(lowess(E6Data$NumbersEntered,E6Data$ErrorsTotal), col="blue") # lowess line (x,y)



boxplot(E6Data$ErrorsTotal ~ E6Data$Group, main="Total numbers enterefd by group")
boxplot(E6Data$NumbersEntered ~ E6Data$Group, main="Total numbers entered by group") 
boxplot(E6Data$Corrections ~ E6Data$Group, main="Total corrections by group")
boxplot(E6Data$Rate ~ E6Data$Group, main="Error-Rate by group")


#boxplot
b1<-ggplot(E6Data, aes(ErrorsTotal, Group)) + 
  geom_boxplot(aes(fill = ErrorsTotal)) +
  theme(legend.position = "none")


#jitter plot
b2<-ggplot(xy, aes(zvar, xvar)) + 
  geom_jitter(alpha=I(1/4), aes(color=zvar)) +
  theme(legend.position = "none")

#volcano plot
b3<-ggplot(xy, aes(x = xvar)) +
  stat_density(aes(ymax = ..density..,  ymin = -..density..,
                   fill = zvar, color = zvar),
               geom = "ribbon", position = "identity") +
  facet_grid(. ~ zvar) +
  coord_flip() +
  theme(legend.position = "none")

grid.arrange(b1, b2, b3, nrow=1)
plot(b1)



mean <- mean(GroupClear$ErrorsTotal)
sd(GroupClear$ErrorsTotal)

mean(GroupMedium$ErrorsTotal)
sd(GroupMedium$ErrorsTotal)

mean(GroupObscured$ErrorsTotal)
sd(GroupObscured$ErrorsTotal)


mean(GroupClear$Rate)
sd(GroupClear$Rate)

mean(GroupMedium$Rate)
sd(GroupMedium$Rate)

mean(GroupObscured$Rate)
sd(GroupObscured$Rate)

mean(GroupClear$NumbersEntered)
sd(GroupClear$NumbersEntered)

mean(GroupMedium$NumbersEntered)
sd(GroupMedium$NumbersEntered)

mean(GroupObscured$NumbersEntered)
sd(GroupObscured$NumbersEntered)


mean(GroupClear$Corrections)
sd(GroupClear$Corrections)

mean(GroupMedium$Corrections)
sd(GroupMedium$Corrections)

mean(GroupObscured$Corrections)
sd(GroupObscured$Corrections)

#Create an ANOVA table
#E6.aov <- aov(E6Data$ErrorsTotal ~ E6Data$Group)
#summary(E6.aov)
#TukeyHSD(E6.aov)
#Kruskal Wallis test on the total errors made
kruskal.test(E6Data$ErrorsTotal ~ E6Data$Group)
#Kruskal Wallis test on the total numbers entered by participants
kruskal.test(E6Data$NumbersEntered ~ E6Data$Group)
#Kruskal Wallis test on the total number of detected & corrected errors
kruskal.test(E6Data$Corrections ~ E6Data$Group)
#Kruskal Wallis test on the rates? total error / total numbers entered 
kruskal.test(E6Data$Rate ~ E6Data$Group)


kruskalmc(resp=E6Data$ErrorsTotal, categ=E6Data$Group,probs = 0.05, cont=NULL)
kruskalmc(resp=E6Data$Rate, categ=E6Data$Group,probs = 0.05, cont=NULL)

#some discriptive stuff things...
#test <- E6Data$Corrections
# median(test, na.rm = false) #na.rm = remove NA values or not
# > mean(test, na.rm = false)
# boxplot(test, test2, main="dasd", names=c("test","test2"))
########################
#Mean and SD of the Age:
mean(E6Data$Age_n)
sd(E6Data$Age_n)

#install directly from github repository
#library(devtools)
#install_github('shiny', 'rstudio')
#install_github('R-Websockets', 'rstudio')
#nrow(E6Data) number of rows in dataframs - same for colums ncol()

#install directly from github repository
library(devtools)
install_github("MobilizeSimple", "AmeliaMN")


