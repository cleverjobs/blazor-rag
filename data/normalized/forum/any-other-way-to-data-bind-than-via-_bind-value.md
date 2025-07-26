# any other way to data bind than via @bind-Value?

## Question

**Arn** asked on 23 Mar 2020

Hello, I am using Telerik DDL for Blazor (2.6.1). For now it works as expected. Right now, for what I could see, you can only databind to the selected VALUE (via bind-Value property). Is there a way that I missed, to databind via the selected ITEM? I use this code: <TelerikDropDownList Data="@MyListOfMyItem" TextField="@(nameof(MyItem.prop1))" ValueField="@(nameof(MyItem.prop1))" @bind-Value=@MyItemSelected TItem="MyItem" TValue="string"/> At the moment, I can only access to the prop1 property of the selected MyItem element (using @bind-Value). I can obviously deduct the MyItem element from the collection via LinQ, but I would definitelyprefer to have another binding property that directly returns the MyItem element to me. In other words, something similar to the SelectedItem from MS components. Is there a way to do that? If not, is it something that you plan to release in the future? Thx in advance A

## Answer

**Svetoslav Dimitrov** answered on 23 Mar 2020

Hello Arnaud, Yes, you can get an instance of the model when an item is selected a dropdown. You can do so by following the instructions below: Use the unique identifier you get from the component (the Value ) Get the entire model from its data source by filtering it (e.g., by using the Where() operator). More information (like why this cannot be implemented out-of-the-box) and working example can be found on our Knowledge Base from this link: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model) Regards, Svetoslav Dimitrov
