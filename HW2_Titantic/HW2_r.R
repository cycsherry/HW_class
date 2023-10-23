library("openxlsx")
data <- read.csv("/Users/yucheng/Desktop/DA/titanic.csv")
library("ggplot2")
p <- ggplot(data, aes(x=fare)) + 
  geom_histogram(aes(y = ..density..),
                 colour = 1, fill = "pink") +
  geom_density(adjust=0.7)+
  ggtitle("Plot of density distribution") +
  xlab("Fare (All)") + ylab("Density")+
  theme(plot.title = element_text(hjust = 0.5))
p

p.1 <- data.frame(fare=data[data$pclass==1,8])
p.2 <- data.frame(fare=data[data$pclass==2,8])
p.3 <- data.frame(fare= data[data$pclass==3,8])
p.3 <-data.frame(fare =p.3[-626,])

p <- ggplot(p.3, aes(x=fare)) + 
  geom_histogram(aes(y = ..density..),
                 colour = 1, fill = "lightblue") +
  geom_density(adjust=0.7)+
  ggtitle("Plot of density distribution") +
  xlab("Fare (Pclass=3)") + ylab("Density")+
  theme(plot.title = element_text(hjust = 0.5))+
  xlim(0,200)
p

q <- ggplot(p.1, aes(x=fare)) + 
  geom_histogram(aes(y = ..density..),
                 colour = 1, fill = "lightgreen") +
  geom_density(adjust=0.7)+
  ggtitle("Plot of density distribution") +
  xlab("Fare (Pclass=1)") + ylab("Density")+
  theme(plot.title = element_text(hjust = 0.5))+
  xlim(0,200)
q

r <- ggplot(p.2, aes(x=fare)) + 
  geom_histogram(aes(y = ..density..),
                 colour = 1, fill = "red") +
  geom_density(adjust=0.7)+
  ggtitle("Plot of density distribution") +
  xlab("Fare (Pclass=2)") + ylab("Density")+
  theme(plot.title = element_text(hjust = 0.5))
r

#=================KV test=====
ks.test(p.1$fare,p.2$fare)
ks.test(p.3$fare,p.2$fare)
ks.test(p.1$fare,p.3$fare)

summary(p.1)
sd(p.1$fare)


summary(p.2)
sd(p.2$fare)


summary(p.3)
sd(p.3$fare)
