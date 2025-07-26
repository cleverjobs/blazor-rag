# GridLayout... ColumnSpan

## Question

**ale** asked on 03 Dec 2022

Hi. Why in this snippet [https://blazorrepl.telerik.com/wGvwOxGP22SKTu0O14](https://blazorrepl.telerik.com/wGvwOxGP22SKTu0O14) the "Item 1" is not taking the size of the 3 columns on the first row as defined in the snippet Thanks

## Answer

**Nadezhda Tacheva** answered on 06 Dec 2022

Hi Alexandre, When you specify the desired ColumnSpan, you should also provide the Column that will serve as a start position for the item taking several columns. This is the key part that is missing in the shared example. I realize that this specifics is not included in our documentation, so please accept my apologies if this has caused some troubles on your end. We will work on improving the article in this regard. I'd like to mention another useful note - if you want to control the position of all items, you should set their Column and Row values as desired. The items that do not have Column and Row values will be distributed in the available space. Here is the modified sample to demonstrate the difference: [https://blazorrepl.telerik.com/GQlwkgPq31p2o2jH38.](https://blazorrepl.telerik.com/GQlwkgPq31p2o2jH38.) I hope you will find the above information and sample useful to move forward with your application. Please let us know if you are facing any other difficulties. Regards, Nadezhda Tacheva Progress Telerik
