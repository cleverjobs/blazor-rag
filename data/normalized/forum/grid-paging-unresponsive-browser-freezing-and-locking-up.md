# Grid Paging unresponsive browser freezing and locking up

## Question

**Han** asked on 30 Apr 2024

We have recently upgraded to v5.1.1 and noticed on one of our Grids that when you have the page size set to 100 and start paging through the grid, when you reach page 6, the browser locks up and you get the chrome prompt of "wait/close tab". We reverted back to 4.5.0 and the issue seems to disappear. We are using the OnRead event to get the data for the grid. I tried replicate the issue with a simple object (fewer properties) and smaller data set and I was not able to do so so it seems it's only happening with larger data sets

## Answer

**Dimo** answered on 02 May 2024

Hello Hani, The attached sample project contains an SQLite data source with 100,000 items and paging works as expected. Is there anything special about page 6 in your case? Do you get any exceptions? Are you using a lot of column templates with child components inside? What are they? Can you send a similar runnable app for inspection? Regards, Dimo Progress Telerik
