# Blazor TelerikDropDownList

## Question

**kha** asked on 04 Dec 2019

Hello, i wanted to know how can i get the the whole object instead of pass ValueField and Get That as a value <TelerikDropDownList Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" @bind-Value="selectedValue"></TelerikDropDownList> like in here i want my ValueField be the whole object no MyValueFierd

## Answer

**Marin Bratanov** answered on 04 Dec 2019

Hi, This is possible if you are binding to primitive types: [https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind#primitive-types.](https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind#primitive-types.) Alternatively, you should do a lookup in the model collection based on the value. You can read more about this in the following thread where a more detailed discussion is available: [https://www.telerik.com/forums/binding-to-an-instance-of-the-same-type-as-the-ienumerable.](https://www.telerik.com/forums/binding-to-an-instance-of-the-same-type-as-the-ienumerable.) Regards, Marin Bratanov
