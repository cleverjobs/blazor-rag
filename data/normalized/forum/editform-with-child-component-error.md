# EditForm with child component error

## Question

**Jen** asked on 15 May 2023

Hi, I'm trying to create EditForm with child components inside it. Child component has two drop down lists, that after selection should return single value. You can see attached Component.razor and razor.cs with the code. However, my EditForm throws me error regarding ValueExpression. If I understand right, I can reference it to specific model property, but I have 2 dropdown menus and I dont hold value for any of them in my object? So how I should use it? I'm currently trying to use it like this: <Customs.UI.Shipments.Components.Common.LocodeComponent DateRequired="true" Title="Collection" Export="@(Shipment.Export)" @bind-CityId="Shipment.CollectionCityId" /> Last screenshot of it working absolutely fine outside EditForm.. Any help or guidance would be so much appreciated!

## Answer

**Svetoslav Dimitrov** answered on 18 May 2023

Hello Matas, From what I can see on the screenshots you are getting the Error SystemInvalidOperationException: Telerik.Blazor.Components.SomeComponent requires a value for 'ValueExpression'. ValueExpression is provided automatically when using 'bind-Value' error message. To solve that issue, you can check the Requires a value for ValueExpression Knowledge-based article. Regards, Svetoslav Dimitrov Progress Telerik
