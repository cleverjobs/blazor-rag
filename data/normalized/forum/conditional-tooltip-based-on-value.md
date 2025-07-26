# Conditional Tooltip based on value

## Question

**JimJim** asked on 24 Apr 2023

Hello, I want to set the value of a tool tip based on a value of an item in my grid. I have tried this, but I get an error: This is above all HTML taken from an example <TelerikTooltip TargetSelector=".tooltip-target"> </TelerikTooltip> <GridColumn Editable=false Locked=true Visible="@isIDVisible" Field=@nameof(ProductDto.ProductId) Title="ID" Width="150px"> <Template> @{
var item=(ProductDto)context;
} <TelerikButton ThemeColor="success" OnClick="()=> SetAmtToAnotherCol(item)"> Test </TelerikButton> <br /> <TelerikButton FillMode="link" ThemeColor="info" Class="tooltip-target" Title="(@item.UnitsInStock <0) ? 'neg' : 'pos'" OnClick="()=> SetAmtToAnotherCol(item)"> @item.UnitsInStock </TelerikButton> </Template> </GridColumn> I receive this error: RZ9986 Component attributes do not support complex content (mixed C# and markup). Attribute: 'Title', text: '(item.UnitsInStock <0) ? 'neg' : 'pos'' If I simply do this, it works: Title=@item.UnitsInStock.ToString() Is there a way for me to set a string based on a value?

## Answer

**Jim** answered on 24 Apr 2023

I wound up figuring this out for anyone who is interested, I just changed my code block a bit in the grid template: <Template> @{
// item gets a refernce to the data behind the row... PERFECT !!!!
var item=(ProductDto)context; var title=(item.UnitsInStock <=0) ? "Click to Utilize Full Credit" : "Click to Pay Full Net Balance"; } <TelerikButton ThemeColor="success" OnClick="()=> SetAmtToAnotherCol(item)"> Test </TelerikButton> <br /> <TelerikButton FillMode="link" ThemeColor="info" Class="tooltip-target" Title=@title OnClick="()=> SetAmtToAnotherCol(item)"> @item.UnitsInStock </TelerikButton> </Template>
