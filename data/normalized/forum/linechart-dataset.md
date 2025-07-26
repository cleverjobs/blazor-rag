# LineChart Dataset ?

## Question

**Dea** asked on 20 Sep 2022

I have a SP returning an unknown # of columns. 1st column is the time periods, 2022-07, 2022-08, etc 2nd and to many columns is for each line on the linechart I want to map. eg: StarWars, Marvel, LOTRs, etc... could be more dont know what the values could be or how many. The values of those columns is a int #. Example dataset. Periods StarWars Marvel LOTRs 2022-07 120 50 110 2022-08 125 55 105 So how do I attach that to a line chart control? I have read thru the demo codes but none seem to give me the answer. In my old days, :), I would return a dataset as structured above and then bind that control to the dataset. Then set the bottom axis to the Periods column values and the Up axis to the values in the other columns. With the legend using the column names. Not sure how to describe that in the data class as I dont know the column names that could be coming in. And not sure what the controls tags should be looking like. Any help would be appreciated. Thanks in advance. Deasun.

## Answer

**Stamo Gochev** answered on 23 Sep 2022

Hello, The documentation articles about Line Chart and Telerik Blazor Chart Data binding provide a detailed explanation of how to configure line series and setup the data in the proper format. I've created a Telerik Blazor REPL example, which shows one way to display the data that you mentioned using line series: The idea is to create separate series for the entries that you want and then bind the data using the corresponding "Field" and "CategoryField". If you want to build a chart depending on a dynamic structure, the above link shows one possible approach - you can name the fields of the model "Series1", "Series2", etc. up to the amount that you want (probably more than 10 items will result in too much data displayed in the chart, so it won't be easy to read anyway). If the number of series is also uncertain, then you can use a for loop to create them - similar to how it is done in the knowledge base article for creating dynamic series. Regards, Stamo Gochev Progress Telerik
