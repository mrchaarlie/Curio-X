# Libraries
library(plyr)
library(ggplot2)
library(reshape2)
library(gridExtra)

# Data
logs <- read.csv("logs.csv")
results <- read.csv("results.csv")
gold <- read.csv("goldstandard.csv")
dim(logs); dim(results); dim(gold)

# Overview
summary(gold); summary(results);

# Make a joined set
names(gold) == names(results)
all <- rbind(results,gold)
all$class[all$User == "RobJon"] <- "gold"
all$class[all$User != "RobJon"] <- "userResult"
all$class <- as.factor(all$class)

# User results entries
imgProcByUser <- count(results,"User")$freq
mean(imgProcByUser)
sd(imgProcByUser)
qplot(imgProcByUser,main="Image Completion Histogram",xlab="Images Completed",ylab="Number of Users")

# TODO: Check skips?
#actionByUser <- count(logs,"Action")$freq
#mean(imgProcByUser)
#sd(imgProcByUser)
#qplot(imgProcByUser,main="Image Completion Histogram",xlab="Images Completed",ylab="Number of Users")

# Results histograms (TODO: Fix scales for comparison)
qplot(Fruit,data=results ,main="Fruit Evaluation Results",xlab="Image has Fruit",ylab="Number of Users")

p1 <- ggplot(all, aes(x=Flower, fill=class)) + geom_histogram(binwidth=.5, position="dodge")
p2 <- ggplot(all, aes(x=Bud, fill=class)) + geom_histogram(binwidth=.5, position="dodge")
p3 <- ggplot(all, aes(x=Fruit, y=..count../sum(..count..), fill=class)) + 
  geom_histogram(binwidth=.5, position="dodge") #+ scale_y_continuous(labels = percent_format())
grid.arrange(p1, p2, p3, ncol=3)

#
# Compare to gold standard
#
images <- results[,c("User","iID","Flower","Bud","Fruit")] #results$User == "AmusingBombay"
images$correctFlower <- "False"; images$correctBud <- "False"; images$correctFruit <- "False"
accuracyCols <- c("tpFlower","tpBud","tpFruit","tnFlower","tnBud",
                  "tnFruit","fpFlower","fpBud","fpFruit","fnFlower","fnBud","fnFruit")
images[accuracyCols] <- 0

for (i in 1:dim(images)[1]) {
  if (gold$Flower[gold$iID == images$iID[i]] == images$Flower[i]) {
    images$correctFlower[i] <- "True"
    if (images$Flower[i] == "True") {
      images$tpFlower[i] <- 1
    } else {
      images$tnFlower[i] <- 1
    }
  } else {
    if (images$Flower[i] == "True") {
      images$fpFlower[i] <- 1
    } else {
      images$fnFlower[i] <- 1
    }
  }
  
  if (gold$Bud[gold$iID == images$iID[i]] == images$Bud[i]) {
    images$correctBud[i] <- "True"
    if (images$Bud[i] == "True") {
      images$tpBud[i] <- 1
    } else {
      images$tnBud[i] <- 1
    }
  } else {
    if (images$Bud[i] == "True") {
      images$fpBud[i] <- 1
    } else {
      images$fnBud[i] <- 1
    }
  }
  
  if (gold$Fruit[gold$iID == images$iID[i]] == images$Fruit[i]) {
    images$correctFruit[i] <- "True"
    if (images$Fruit[i] == "True") {
      images$tpFruit[i] <- 1
    } else {
      images$tnFruit[i] <- 1
    }
  } else {
    if (images$Fruit[i] == "True") {
      images$fpFruit[i] <- 1
    } else {
      images$fnFruit[i] <- 1
    }
  }
}

images$correctFlower <- as.factor(images$correctFlower)
images$correctBud <- as.factor(images$correctBud)
images$correctFruit <- as.factor(images$correctFruit)

#
# Aggregate for images
#
confmat <- aggregate(cbind(tpFlower,fpFlower,tnFlower,fnFlower,
                           tpBud,fpBud,tnBud,fnBud,tpFruit,fpFruit,
                           tnFruit,fnFruit) ~ iID, images, sum)

metricCols <- c("accuracyFlower","tprFlower","fdrFlower",
             "accuracyBud","tprBud","fdrBud",
             "accuracyFruit","tprFruit","fdrFruit")

confmat[metricCols] <- 0.0

# Calculate metrics for images
for (i in 1:dim(confmat)[1]) {
  # Flowers
  confmat$accuracyFlower[i] <- (confmat$tpFlower[i] + confmat$tnFlower[i]) /
    (confmat$tpFlower[i] + confmat$tnFlower[i] + confmat$fpFlower[i] + confmat$fnFlower[i])
  confmat$tprFlower[i] <- confmat$tpFlower[i] / (confmat$tpFlower[i] + confmat$fnFlower[i])
  confmat$fdrFlower[i] <- confmat$fpFlower[i] / (confmat$tpFlower[i] + confmat$fpFlower[i])
  
  # Buds
  confmat$accuracyBud[i] <- (confmat$tpBud[i] + confmat$tnBud[i]) /
    (confmat$tpBud[i] + confmat$tnBud[i] + confmat$fpBud[i] + confmat$fnBud[i])
  confmat$tprBud[i] <- confmat$tpBud[i] / (confmat$tpBud[i] + confmat$fnBud[i])
  confmat$fdrBud[i] <- confmat$fpBud[i] / (confmat$tpBud[i] + confmat$fpBud[i])
  
  # Fruit
  confmat$accuracyFruit[i] <- (confmat$tpFruit[i] + confmat$tnFruit[i]) /
    (confmat$tpFruit[i] + confmat$tnFruit[i] + confmat$fpFruit[i] + confmat$fnFruit[i])
  confmat$tprFruit[i] <- confmat$tpFruit[i] / (confmat$tpFruit[i] + confmat$fnFruit[i])
  confmat$fdrFruit[i] <- confmat$fpFruit[i] / (confmat$tpFruit[i] + confmat$fpFruit[i])
}

# TODO: WTF
# Comparison of disributions for flower, bud, and fruit on accuracy, TPR, and FDR
fl1 <- qplot(confmat$accuracyFlower,xlab="Flower Classification Accuracy",ylab="Number of Users")
fl2 <- qplot(confmat$tprFlower,xlab="Flower True Positive Rate",ylab="Number of Users")
fl3 <- qplot(confmat$fdrFlower,xlab="Flower False Discovery Rate",ylab="Number of Users")
bud1 <- qplot(confmat$accuracyBud,xlab="Bud Classification Accuracy",ylab="Number of Users")
bud2 <- qplot(confmat$tprBud,xlab="Bud True Positive Rate",ylab="Number of Users")
bud3 <- qplot(confmat$fdrBud,xlab="Bud False Discovery Rate",ylab="Number of Users")
fr1 <- qplot(confmat$accuracyFruit,xlab="Fruit Classification Accuracy",ylab="Number of Users")
fr2 <- qplot(confmat$tprFruit,xlab="Fruit True Positive Rate",ylab="Number of Users")
fr3 <- qplot(confmat$fdrFruit,xlab="Fruit False Discovery Rate",ylab="Number of Users")
grid.arrange(fl1, fl2, fl3, bud1, bud2, bud3, fr1, fr2, fr3, ncol=3)

# Mean and std dev distrubutions fr images
# Accuracy
distflAcc <- c(mean(confmat$accuracyFlower,na.rm=TRUE), sd(confmat$accuracyFlower,na.rm=TRUE))
distbudAcc <- c(mean(confmat$accuracyBud,na.rm=TRUE),sd(confmat$accuracyBud,na.rm=TRUE))
distfrAcc <- c(mean(confmat$accuracyFruit,na.rm=TRUE), sd(confmat$accuracyFruit,na.rm=TRUE))

x <- seq(0,1,length=1000);
y <- dnorm(x,mean=distflAcc[1],sd=distflAcc[2]); qplot(x,y)
y <- dnorm(x,mean=distbudAcc[1],sd=distbudAcc[2]); qplot(x,y)
y <- dnorm(x,mean=distfrAcc[1],sd=distfrAcc[2]); qplot(x,y)

# True Positive Rate
distflTpr <- c(mean(confmat$tprFlower,na.rm=TRUE), sd(confmat$tprFlower,na.rm=TRUE))
distbudTpr <- c(mean(confmat$tprBud,na.rm=TRUE),sd(confmat$tprBud,na.rm=TRUE))
distfrTpr <- c(mean(confmat$tprFruit,na.rm=TRUE), sd(confmat$tprFruit,na.rm=TRUE))

x <- seq(0,1,length=1000);
y <- dnorm(x,mean=distflTpr[1],sd=distflTpr[2]); qplot(x,y)
y <- dnorm(x,mean=distbudTpr[1],sd=distbudTpr[2]); qplot(x,y)
y <- dnorm(x,mean=distfrTpr[1],sd=distfrTpr[2]); qplot(x,y)

# False Discovery Rate
distflFdr <- c(mean(confmat$fdrFlower,na.rm=TRUE), sd(confmat$fdrFlower,na.rm=TRUE))
distbudFdr <- c(mean(confmat$fdrBud,na.rm=TRUE),sd(confmat$fdrBud,na.rm=TRUE))
distfrFdr <- c(mean(confmat$fdrFruit,na.rm=TRUE), sd(confmat$fdrFruit,na.rm=TRUE))

# Bimodal -- either really good or bad
x <- seq(0,1,length=1000);
y <- dnorm(x,mean=distflFdr[1],sd=distflFdr[2]); qplot(x,y)
y <- dnorm(x,mean=distbudFdr[1],sd=distbudFdr[2]); qplot(x,y)
y <- dnorm(x,mean=distfrFdr[1],sd=distfrFdr[2]); qplot(x,y)

#
# Aggregate for users
#
users <- images
users$iID <- NULL

confmat <- aggregate(cbind(tpFlower,fpFlower,tnFlower,fnFlower,
                           tpBud,fpBud,tnBud,fnBud,tpFruit,fpFruit,
                           tnFruit,fnFruit) ~ User, users, sum)

metricCols <- c("accuracyFlower","tprFlower","fdrFlower",
                "accuracyBud","tprBud","fdrBud",
                "accuracyFruit","tprFruit","fdrFruit")

confmat[metricCols] <- 0.0

# Calculate metrics for users
for (i in 1:dim(confmat)[1]) {
  # Flowers
  confmat$accuracyFlower[i] <- (confmat$tpFlower[i] + confmat$tnFlower[i]) /
    (confmat$tpFlower[i] + confmat$tnFlower[i] + confmat$fpFlower[i] + confmat$fnFlower[i])
  confmat$tprFlower[i] <- confmat$tpFlower[i] / (confmat$tpFlower[i] + confmat$fnFlower[i])
  confmat$fdrFlower[i] <- confmat$fpFlower[i] / (confmat$tpFlower[i] + confmat$fpFlower[i])
  
  # Buds
  confmat$accuracyBud[i] <- (confmat$tpBud[i] + confmat$tnBud[i]) /
    (confmat$tpBud[i] + confmat$tnBud[i] + confmat$fpBud[i] + confmat$fnBud[i])
  confmat$tprBud[i] <- confmat$tpBud[i] / (confmat$tpBud[i] + confmat$fnBud[i])
  confmat$fdrBud[i] <- confmat$fpBud[i] / (confmat$tpBud[i] + confmat$fpBud[i])
  
  # Fruit
  confmat$accuracyFruit[i] <- (confmat$tpFruit[i] + confmat$tnFruit[i]) /
    (confmat$tpFruit[i] + confmat$tnFruit[i] + confmat$fpFruit[i] + confmat$fnFruit[i])
  confmat$tprFruit[i] <- confmat$tpFruit[i] / (confmat$tpFruit[i] + confmat$fnFruit[i])
  confmat$fdrFruit[i] <- confmat$fpFruit[i] / (confmat$tpFruit[i] + confmat$fpFruit[i])
}

# Comparison of disributions for flower, bud, and fruit on accuracy, TPR, and FDR
fl1 <- qplot(confmat$accuracyFlower,xlab="Flower Classification Accuracy",ylab="Number of Users")
fl2 <- qplot(confmat$tprFlower,xlab="Flower True Positive Rate",ylab="Number of Users")
fl3 <- qplot(confmat$fdrFlower,xlab="Flower False Discovery Rate",ylab="Number of Users")
bud1 <- qplot(confmat$accuracyBud,xlab="Bud Classification Accuracy",ylab="Number of Users")
bud2 <- qplot(confmat$tprBud,xlab="Bud True Positive Rate",ylab="Number of Users")
bud3 <- qplot(confmat$fdrBud,xlab="Bud False Discovery Rate",ylab="Number of Users")
fr1 <- qplot(confmat$accuracyFruit,xlab="Fruit Classification Accuracy",ylab="Number of Users")
fr2 <- qplot(confmat$tprFruit,xlab="Fruit True Positive Rate",ylab="Number of Users")
fr3 <- qplot(confmat$fdrFruit,xlab="Fruit False Discovery Rate",ylab="Number of Users")
grid.arrange(fl1, fl2, fl3, bud1, bud2, bud3, fr1, fr2, fr3, ncol=3)

# Mean and std dev distrubutions for users
# Accuracy
distflAcc <- c(mean(confmat$accuracyFlower,na.rm=TRUE), sd(confmat$accuracyFlower,na.rm=TRUE))
distbudAcc <- c(mean(confmat$accuracyBud,na.rm=TRUE),sd(confmat$accuracyBud,na.rm=TRUE))
distfrAcc <- c(mean(confmat$accuracyFruit,na.rm=TRUE), sd(confmat$accuracyFruit,na.rm=TRUE))

x <- seq(0,1,length=1000);
y <- dnorm(x,mean=distflAcc[1],sd=distflAcc[2]); qplot(x,y)
y <- dnorm(x,mean=distbudAcc[1],sd=distbudAcc[2]); qplot(x,y)
y <- dnorm(x,mean=distfrAcc[1],sd=distfrAcc[2]); qplot(x,y)

# True Positive Rate -- really crappy for buds
distflTpr <- c(mean(confmat$tprFlower,na.rm=TRUE), sd(confmat$tprFlower,na.rm=TRUE))
distbudTpr <- c(mean(confmat$tprBud,na.rm=TRUE),sd(confmat$tprBud,na.rm=TRUE))
distfrTpr <- c(mean(confmat$tprFruit,na.rm=TRUE), sd(confmat$tprFruit,na.rm=TRUE))

x <- seq(0,1,length=1000);
y <- dnorm(x,mean=distflTpr[1],sd=distflTpr[2]); qplot(x,y)
y <- dnorm(x,mean=distbudTpr[1],sd=distbudTpr[2]); qplot(x,y)
y <- dnorm(x,mean=distfrTpr[1],sd=distfrTpr[2]); qplot(x,y)

# False Discovery Rate
distflFdr <- c(mean(confmat$fdrFlower,na.rm=TRUE), sd(confmat$fdrFlower,na.rm=TRUE))
distbudFdr <- c(mean(confmat$fdrBud,na.rm=TRUE),sd(confmat$fdrBud,na.rm=TRUE))
distfrFdr <- c(mean(confmat$fdrFruit,na.rm=TRUE), sd(confmat$fdrFruit,na.rm=TRUE))

# Bimodal -- either really good or bad (bad for buds)
x <- seq(0,1,length=1000);
y <- dnorm(x,mean=distflFdr[1],sd=distflFdr[2]); qplot(x,y)
y <- dnorm(x,mean=distbudFdr[1],sd=distbudFdr[2]); qplot(x,y)
y <- dnorm(x,mean=distfrFdr[1],sd=distfrFdr[2]); qplot(x,y)

