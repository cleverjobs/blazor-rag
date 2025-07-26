# TelerikGrid SelectedItems updated only if SelectedItemsChanged event listening

## Question

**Cla** asked on 29 Sep 2021

Hi, i use a TelerikGrid component and i would like to change the UI on grid selection change, so i have: <TelerikGrid @ref="Grid"... />...

@if (Grid?.SelectedItems.Count()> 0)

{ <span> There are items selected! </span> } but the message is never displayed even when i select rows on grid. I noted who if i bind the event SelectedItemsChanged then the SelectedItems property is updated correctly, and the message is diplayed: <TelerikGrid @ref="Grid" SelectedItemsChanged="@OnSelectedItemsChanged"... />...

@if (Grid?.SelectedItems.Count()> 0)

{ <span> There are items selected! </span> } Why i need to bind SelectedItemsChanged event even if don't use it? Thanks

## Answer

**Marin Bratanov** answered on 30 Sep 2021

Hello Claudio, You need to use something like this: <TelerikGrid @bind-SelectedItems="@MySelectedItemsCollection"... />

@if(MySelectedItemsCollection !=null && MySelectedItemsCollection.Any())
{
<span>something if selected items</span>
}

@code{
IEnumerable<MyModel> MySelectedItemsCollection { get; set;}=Enumerable.Empty<MyModel>();
} Here are the key points: you must use the view-model data, not component reference for this (you can read more about handling the selectedi items from the grid here and here ) using two-way binding lets you skip your own handler, the framework will do this for you (you can read more about this here ) This is just how the Blazor framework is designed. Regards, Marin Bratanov Progress Telerik
