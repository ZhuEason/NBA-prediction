The NBA now is incredibly successful around the world. With the growing attention to this league, more and more teams began using statistic way to manage and lead the team. Predicting the win percentage of an NBA team based on the previous performance of their roster is quite valuable to general managers, coaches, players fans, gamblers, and statisticians alike. Moreover, knowing which particular statistic or feature is most influential to winning games is also desirable. Our project aims to do exactly that.


A naive way to predict a team performance is to use k-nearest-neighbors, for a team who has its first 20 games in a new season, we can compare its average data to the history team to predict how many wins it would have in the whole season. But it would happen based on the first 20 games. Is there any way to use the earlier season data to predict next season?

We built a two-phases regression learning algorithm. For the predicting team, we gather its team members’ performance in the last season(it may come from another team). Using linear regression to find the relationship between the team members performance last season and the team performance the second year, such as rebounce, grades, pts so on and so forth. It is obvious that the team performance has a strong relationship with the win percentage, which is performed in the second phase linear regression. 

To compare the algorithms effect, we used the team performance data in the earlier season to directly predict the win percentage of the team in the next season. At last, we compared two results we got.
