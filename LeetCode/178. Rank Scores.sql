/**
* LeetCode : Rank Scores(순위 점수)
* URL : https://leetcode.com/problems/rank-scores/
*/

select score, dense_rank() over(order by score desc) as rank
from Scores
