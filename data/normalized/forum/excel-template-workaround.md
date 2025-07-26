# Excel template workaround?

## Question

**Dou** asked on 17 Sep 2020

Hello, I know the documentation says that grid templates will be ignored on Excel export but I'm wondering if there's any way around that. I have columns that are integers which represent strings (like from a type table on the database) so I have templates set up on those columns to display the strings represented by the integers but of course when I export to Excel it exports the integers which are meaningless to an end user. Maybe there's a way to get access to the context in the Field property or something? Otherwise I'll have to modify my classes to include the strings as well which isn't the end of the world but figured I'd check with you first. Thanks.

## Answer

**Marin Bratanov** answered on 17 Sep 2020

Hello Doug, There isn't a way in Blazor to programmatically get the text of such templates, and even if there were - you can't put HTML in Excel. A solution is to use a Field for that column that you want exported. Perhaps adding those string representations to the view-model the grid uses will be the easiest option - it will let you point the grid directly to them so they will be exported and the user will also be able to better group and filter on them. Another option is to generate the .xlsx file yourself, you can find a sample in my post from 13 Jan 2020 here. Regards, Marin Bratanov
