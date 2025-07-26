# TabStrip Titles - Reading from a DataTable

## Question

**cma** asked on 31 Jan 2023

I would like to know if it's possible to read the "Title" from code, a database table versus it being in the razor text. If it is possible, any example would be great to share. I'd like this title to be more flexible and user-defined. <TabStripTab Title="PowerBI Dashboard #1"> <div class="h_iframe"> <iframe src=@TargetUrl frameborder="0" allowfullscreen /> </div> </TabStripTab> <TabStripTab Title="PowerBI Dashboard #2"> <div class="h_iframe"> <iframe src=@TargetUrl2 frameborder="0" allowfullscreen /> </div> </TabStripTab> Thanks!

## Answer

**Yanislav** answered on 03 Feb 2023

Hello Chris, The Title configuration can be bound to a property. This means you can fetch the data from the DB and assign the retrieved value to this property. Here is a simple example that demonstrates the approach: [https://blazorrepl.telerik.com/QduGaHvl27uqf4DU38](https://blazorrepl.telerik.com/QduGaHvl27uqf4DU38) I've simplified it by using a method in which you can execute the logic to fetch the DB and return the value that has to be used as Title. I hope this helps. Regards, Yanislav
