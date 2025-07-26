# Could you split a GridColumn field string into multiple columns?

## Question

**Luc** asked on 19 Apr 2022

I have a Field in my TelerikGrid : <GridColumn Field=@nameof(EssGrpParm.Str) Title="Tekst" Width="30%"/>. Could I somehow split EssGrpParm.Str with data that looks like this: "CONT INT TFT CSS". into separate columns;. CONT, INT, TFT and CSS? Should I add a list field in EssGrpParm and foreach over the list to get new columns?

## Answer

**Dimo** answered on 21 Apr 2022

Hi Lucas, You have several options: Split the data in advance in the data layer, or in the business logic. Create additional model fields with standard getters. Split the data on the fly, in the Class implementation. Use addititional model fields with custom getters. Leave the data as is. Use additional Grid columns with <Template> s. Each template will execute custom logic (IndexOf, Substring, etc.) to extract the correct part of the string and display it. With options 1 and 2, the Grid will not know about the original concatenated data. Everything will work normally. I don't recommend the last option. Its main downside is that you will execute string manipulation logic more times than needed. Also, sorting, filtering and editing will not work correctly. Regards, Dimo
