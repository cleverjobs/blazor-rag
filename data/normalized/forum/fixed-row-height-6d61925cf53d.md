# Fixed Row Height

## Question

**Nic** asked on 05 Jan 2021

Hello! I have set the grids row height with the given property to 65. The problem is, that the row height will change dynamically, I guess the row height property is some sort of max height. Is there a way to change the row height to a fixed value of e.g. 65? Thank you & best regards Nico

## Answer

**Marin Bratanov** answered on 05 Jan 2021

Hello Nico, The RowHeight is set as an inline rule on the <tr> element. It is used for Virtual Scrolling so the grid can perform the necessary calculations (see the Notes section of the article). The way browsers handle <table> elements and their sizes, however, is complex and such a height rule is only a guidance - it is more like min-height, because if there is a cell with larger content, the browser will disregard this height and make the row taller. If you can find a CSS solution for this behavior, you can target the grid cells easily with it. Regards, Marin Bratanov
