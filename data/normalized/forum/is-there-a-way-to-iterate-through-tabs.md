# is there a way to iterate through tabs

## Question

**EdEd** asked on 16 Feb 2021

I am looking to set the background color on the active tab's title. But I need to reset every other one to it's original color first. Which, usually, requires a loop of some sort. Any help would be great. Thanks ... Ed

## Answer

**Nadezhda Tacheva** answered on 16 Feb 2021

Hi Ed, You can use the Class parameter of the TabStripTab to set your custom CSS class for the design of the non-active tabs (in case you want to change the default styling). The active tab has .k-item, .k-state-active and .k-tab-on-top classes which you can access and modify to match the desired styling. To make sure you are styling just the certain instance of the TapStrip (and not all instances on the page/app, use the Class parameter of the TapStrip to set your custom CSS class for the component). To better illustrate the described setup, I have created the following example: <style>
.my-tabstrip .non-active {
background-color: red;
}

.my-tabstrip .k-item.k-state-active.k-tab- on -top {
background-color: green;
}
</style> <TelerikTabStrip Class="my-tabstrip">
@{ foreach (MyTabModel item in tabs)
{
<TabStripTab Class="non-active" Title="@item.Title">
Content for tab @item.Title
</TabStripTab>
}
}
</TelerikTabStrip>

@code {
List<MyTabModel> tabs=new List<MyTabModel>()
{ new MyTabModel { Title="One" }, new MyTabModel { Title="Two" }, new MyTabModel { Title="Three" }
}; public class MyTabModel { public string Title { get; set; } public int Index { get; set; }
}
} Regards, Nadezhda Tacheva

### Response

**Ed** answered on 17 Feb 2021

Maybe I'm missing something, but when I tried your suggestion I got an error saying: 'Telerik.Blazor.Components.TelerikTabStrip' does not have a property matching the name 'Class'. Thanks ... Ed

### Response

**Nadezhda Tacheva** answered on 18 Feb 2021

Hi Ed, The Class parameter of the TabStrip component is implemented as of version 2.21.0 of the Telerik UI for Blazor. I also tested with the current latest (2.21.1) to see if any issues appear. I can confirm that it works as expected (see project attached and try to run it locally to see if it works as expected for you, too). My advice at this stage will be to check and make sure you are indeed using version 2.21.1. If this is the the case but you are still getting the error, you can either send us a runnable example where the issue is reproduced or modify the one that I send to reproduce the problem, so we can investigate further and provide a solution. Regards, Nadezhda Tacheva

### Response

**Dean** answered on 25 Jan 2022

But is there a way to iterate through tabs?

### Response

**Marin Bratanov** commented on 26 Jan 2022

The information from Nadezhda shows the core principle. This sample project offers more examples and details as well: [https://github.com/telerik/blazor-ui/tree/master/tabstrip/DynamicTabs](https://github.com/telerik/blazor-ui/tree/master/tabstrip/DynamicTabs)
