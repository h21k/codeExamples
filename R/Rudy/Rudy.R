setwd("~/Dropbox/R/Rudy")

#Loading the Data into RStudio- explain the function!
NEData <- read.table("Data.csv", header=TRUE, sep="," )
#Displays the Data
NEData
#Displays the head of the Data
head(NEData)
#Displays the Structure/Datatype of the Data
str(NEData)
#A factor is a categorical (also called nominal) variable.
#This means that there is no relationship between the values 
#as there is with ordinal or interval data
#ONLY ONE WHICH IS REALLY A FACTORIAL NOT INT SO:
NEData$Condition <- factor(NEData$Condition)
#Now check again:
str(NEData)
#Rename / define factors 
NEData$Condition <- factor(NEData$Condition, levels=c(1,2), labels=c("LowCost","HighCost"))

#creating and deleting a new column
NEData$Test <- NEData$Age 

#Deleting
NEData$Test <- NULL

#### DESCRIBING THE DATA #####

# are we getting in terms of the numbers of errors that people make.BARCHART

ErrCount <- table(NEData$ErrorsTotal)
#List of Values and number of times it was answered:
ErrCount

#Now we feed this into a barchart

barplot(ErrCount, main="Barplot of Total Number of Errors")

#not often that people make exactly the same number of errors

#barplots are better for nominal variables

barplot(NEData$cheerful, main="How many ppl were cheerful")

NEData$cheerful <- factor(NEData$cheerful, levels=c(1,2,3,4,5)

                          
#BACK to ERRORS TOTAL -  Histogram
                          
hist(NEData$ErrorsTotal)             
#help(hist) lots more parameters
                          
                          
#For numbers total
hist(NEData$NumbersTotal)
                          
#For corrections total
hist(NEData$CorectionsTotal)  
                          
#Lets have a look at more descriptives - SUBSET
ErrorData <- NEData[c("ErrorsTotal", "NumbersTotal", "Corrections", "Condition", "Sex")]

#Lets check if we got it right
ErrorData
                          
#Now we can summarize the data:
summary(ErrorData)

#we are really interested in the difference in errors between conditions
#Also, standard deviation is always useful 
#(even when the data isn’t necessarily normally distributed
#For this we need the dinction describe
describe(ErrorData)

#So we are getting an error its in the Psych library
                          
install.packages("psych") or show the other way & activate

#Now we can summarize (compare means and standart deviations to the histograms)
describe(ErrorData)
                          
#Need visibility on IAC so we group the data by conditions - differences in means?
describeBy(ErrorData, ErrorData$Condition)
                                                  
#numbers are hard to interpret. A graph is better - Boxplot!
                          
boxplot(ErrorsTotal~Condition, data=ErrorData)
boxplot(NumbersTotal~Condition, data=ErrorData)
boxplot(Corrections~Condition, data=ErrorData)
#is the difference comparable to the size of the boxes? if so sign diff! 
                          
#You can also produce boxplots for more than one factor
boxplot(ErrorsTotal~Condition * Sex, data = ErrorData)
                          
#Now Speed accuracy tradeoff?
plot(NEData$ErrorsTotal,NEData$NumbersTotal)
                          
#can also add a regression line which is an indicator 
#of the linear relationship between the two variables

abline(lm(NEData$NumbersTotal~NEData$ErrorsTotal), col="red")

#We could go on looking into more discriptives

                          
#LETS HAVE A LOOK AT INFERENTIALS!
#MANN WHITNEY_TEST
                          
wilcox.test(NEData$ErrorsTotal~NEData$Condition)
                          
#Wohoo! Significance!  We could also write:
                          
wilcox.test(ErrorsTotal~Condition, data=NEData)
                          
#Speed Accuracy tradeoff?
wilcox.test(NumbersTotal~Condition, data=NEData)   
                          
# A t-test does exactly the same thing as a Mann-Whitney test                     
t.test(NEData$ErrorsTotal~NEData$Condition)
