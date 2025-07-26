# Bound Data To Grid

## Question

**kha** asked on 27 Sep 2020

Hello, there is a problem in binding list of tuple to the grid which results in adding one empty cell at the top of grid like if the list count is 1 there is 2 rows in the grid which first one is completely empty

## Answer

**Marin Bratanov** answered on 27 Sep 2020

Hi Khashayar, The grid works with a collection of models. At worst, a collection of ExpandoObject or a Dictionary (which can be obtained from a DataTable ) can be used. A Tuple is not tested or supported. Regards, Marin Bratanov
