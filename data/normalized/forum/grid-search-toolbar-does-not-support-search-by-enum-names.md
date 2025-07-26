# Grid search toolbar does not support search by enum names

## Question

**Ale** asked on 11 Mar 2022

If I have a field backed by an enum, the Grid will display the name of the enum in the Grid cell, but the Grid search toolbar will not search its string name, despite the string name being what is displayed to the user (it won't search the integer value either, if anyone was wondering) :/ It will work fine for all the other fields that are not an enum. REPL example: [https://blazorrepl.telerik.com/ccERPPET55C7yHfg40](https://blazorrepl.telerik.com/ccERPPET55C7yHfg40)

## Answer

**Apostolos** answered on 15 Mar 2022

Hello Alex, Currently the Grid Toolbar Searchbox filters only the visible string columns. Thus, if you use a column field of type enum it will not be able to filter it. The good news is that there is a feature request regarding this behavior which is under development. It is planned for our 3.2 release which is due in mid-April 2022. I hope the release date fits your time frame. In the meantime, it is possible to use custom manual search (filtering) in the Grid data if you use OnRead. The linked article shows how to get the search string. Regards, Apostolos
