setwd("C:/Users/rohuj/Desktop/ras_cam")
model <- readRDS("mymodel.rds")
test <- read.csv("aligned_team_features.csv")
test
pred <- predict(model, test[,-1])
write.csv(pred, "result.csv")
