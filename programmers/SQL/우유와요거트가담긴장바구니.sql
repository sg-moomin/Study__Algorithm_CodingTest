/**
* 프로그래머스 - 우유와 요거트가 담긴 장바구니
* URL : https://programmers.co.kr/learn/courses/30/lessons/62284
*/

## 방법 1
SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE NAME = 'Milk'
AND CART_ID IN (SELECT DISTINCT CART_ID
          FROM CART_PRODUCTS
          WHERE NAME = 'Yogurt')


## 방법 2
SELECT DISTINCT milk_tb.CART_ID FROM
(SELECT CART_ID
  FROM CART_PRODUCTS
  WHERE NAME = 'Milk') AS milk_tb
,(SELECT CART_ID
  FROM CART_PRODUCTS
  WHERE NAME = 'Yogurt') AS youg_tb
WHERE milk_tb.CART_ID = youg_tb.CART_ID
