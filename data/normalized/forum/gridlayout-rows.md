# GridLayout rows?

## Question

**Dea** asked on 10 Nov 2022

I have a page/component using the <TelerikGridLayout> object. I dont seem to be understanding the row tag. <GridLayoutRows> <GridLayoutRow Height="100px"></GridLayoutRow> @*App Msg*@<GridLayoutRow Height="25px"></GridLayoutRow> @*Report Choices*@<GridLayoutRow Height="50px"></GridLayoutRow> <GridLayoutRow Height="5%"></GridLayoutRow> <GridLayoutRow Height="75%"></GridLayoutRow> @*Report Grid *@</GridLayoutRows> I have tried %s also but the same thing seems to happen. Sometimes the 1st row is covered by the objects in the 2nd row. example: That text msg area is on the 1st row the Labels and button are on the 2nd row. I thought the 1st row would push the 2nd row stuff down auto like. :) How do I get it to not cover each other? Thanks Deasun.

## Answer

**Dimo** answered on 15 Nov 2022

Hello Deasun, The GridLayout creates a layout structure with the exact dimensions that you set. It does not expand automatically to wrap overflowing content. If you have a zone ("cell") with varying content, consider a nested scrollable element. Regards, Dimo Progress Telerik
