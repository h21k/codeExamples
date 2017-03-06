sessionInfo()
#Showcase of different plots
library(googleVis)

#Motion chart example
#M <- gvisMotionChart(data, idvar='id', timevar='date', options=list(), chartid)
suppressPackageStartupMessages(library(googleVis))
plot(gvisMotionChart(Fruits, "Fruit", "Year", options = list(width = 600, height = 400)))


#Line chart example with edit function

df <- data.frame(label=c("US", "GB", "BR"), val1=c(1,3,4), val2=c(23,12,32))
Line <- gvisLineChart(df, xvar="label", yvar=c("val1","val2"),
                      options=list(title="Hello World", legend="bottom",
                                   titleTextStyle="{color:'red', fontSize:18}",                         
                                   vAxis="{gridlines:{color:'red', count:3}}",
                                   hAxis="{title:'My Label', titleTextStyle:{color:'blue'}}",
                                   series="[{color:'green', targetAxisIndex: 0}, 
                         {color: 'blue',targetAxisIndex:1}]",
                                   vAxes="[{title:'Value 1 (%)', format:'##,######%'}, 
                                  {title:'Value 2 (\U00A3)'}]",                          
                                   curveType="function", width=500, height=300                         
                      ))

plot(gvisLineChart(df, options = list(gvis.editor = "Edit me!", height = 350)))


#Line chart example with edit function - NUMBERS

Line <- gvisLineChart(E6Data, xvar="label", yvar=c("ErrorsTotal","val2"),
                      options=list(title="Hello World", legend="bottom",
                                   titleTextStyle="{color:'red', fontSize:18}",                         
                                   vAxis="{gridlines:{color:'red', count:3}}",
                                   hAxis="{title:'My Label', titleTextStyle:{color:'blue'}}",
                                   series="[{color:'green', targetAxisIndex: 0}, 
{color: 'blue',targetAxisIndex:1}]",
                                   vAxes="[{title:'Value 1 (%)', format:'##,######%'}, 
{title:'Value 2 (\U00A3)'}]",                          
                                   curveType="function", width=500, height=300                         
                      ))

plot(gvisLineChart(E6Data, options = list(gvis.editor = "Edit me!", height = 350)))


#Organisational chart

Org <- gvisOrgChart(Regions, options=list(width=600, height=250,
                                          size='large', allowCollapse=TRUE))
plot(Org)

#Notice the data structure. Each row in the data table describes one node. 
#Each node (except the root node) has one or more parent nodes.

Regions


#Tree map - clicking on the areas reveales the subareas

Tree <- gvisTreeMap(Regions, idvar = "Region", parentvar = "Parent", sizevar = "Val", 
                    colorvar = "Fac", options = list(width = 450, height = 320))
plot(Tree)






# - Geographical Data - Plot countries' credit rating sourced from Wikipedia

library(XML)
url <- "http://en.wikipedia.org/wiki/List_of_countries_by_credit_rating"
x <- readHTMLTable(readLines(url), which=3)
levels(x$Rating) <- substring(levels(x$Rating), 4, 
                              nchar(levels(x$Rating)))
x$Ranking <- x$Rating
levels(x$Ranking) <- nlevels(x$Rating):1
x$Ranking <- as.character(x$Ranking)
x$Rating <- paste(x$Country, x$Rating, sep=": ")
G <- gvisGeoChart(x, "Country", "Ranking", hovervar="Rating",
                  options=list(gvis.editor="S&P",
                               projection="kavrayskiy-vii",
                               colorAxis="{colors:['#91BFDB', '#FC8D59']}"))

plot(G)





### Display earth quake information of last 30 days

library(XML)
eq <- read.csv("http://earthquake.usgs.gov/earthquakes/feed/v0.1/summary/2.5_week.csv")
eq$loc=paste(eq$Latitude, eq$Longitude, sep=":")

G <- gvisGeoChart(eq, "loc", "Depth", "Magnitude",
                  options=list(displayMode="Markers", 
                               colorAxis="{colors:['purple', 'red', 'orange', 'grey']}",
                               backgroundColor="lightblue"), chartid="EQ")

plot(G)





#Merging gvis objects

G <- gvisGeoChart(Exports, "Country", "Profit", 
                  options=list(width=250, height=120))
B <- gvisBarChart(Exports[,1:2], yvar="Profit", xvar="Country",                  
                  options=list(width=250, height=260, legend='none'))
M <- gvisMotionChart(Fruits, "Fruit", "Year",
                     options=list(width=400, height=380))
GBM <- gvisMerge(gvisMerge(G,B, horizontal=FALSE), 
                 M, horizontal=TRUE, tableOptions="cellspacing=5")

plot(GBM)


### Cyclones display! 

library(XML)

url <- "http://www.gdacs.org/Cyclones/report.aspx?eventid=41058&episodeid=28&eventtype=TC"

dat <- readHTMLTable(readLines(url), which=5)
#dat2 <- readHTMLTable(readLines(url), which=4) table 4

dat$latlon <- dat[,8]
levels(dat$latlon) <- sapply(strsplit(levels(dat[,8]), ",\n        "),
                             function(x) paste(x[2], x[1], sep=":")
)
dat$Category <- factor(dat$Category, levels=levels(dat$Category)[c(6,7,1:5)],
                       ordered=TRUE)

dat$cat <- as.numeric(dat$Category)
dat$Gust_kmh <- dat[,6] 
levels(dat$Gust_kmh) <- sapply(strsplit(levels(dat[,6]), "km"), 
                               function(x) gsub(" ", "",x[1]))

dat$Gust_kmh <- as.numeric(as.character(dat$Gust_kmh))

#options("googleVis.viewer" = NULL) to display in browser

library(googleVis)

M <- gvisGeoChart(dat, "latlon", sizevar="cat",
                  colorvar="Gust_kmh",
                  options=list(region='035', 
                               backgroundColor="lightblue",
                               datalessRegionColor="grey"))
plot(M)



##### More examples can be found here:


library(googleVis)
?googleVis
demo(googleVis)

##### Slidify ! create presentations in R

library(slidify)
author("googleVis_Tutorial")
## Edit the file index.Rmd file and then
slidify("index.Rmd")


