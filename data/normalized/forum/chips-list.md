# Chips List

## Question

**kha** asked on 23 Feb 2020

Hello, i wanted to know if you are planning on making chipslist component for ui for blazor or not ? and the most important feature for a chips list is the ability to add the written word to selected items list with a simple hit on enter key so is it gonna be able to work smoothly ?

## Answer

**Marin Bratanov** answered on 23 Feb 2020

Hello Khashayar, If I understand you correctly, you need a list of items that you can check off, and a way to add items to that list trough a user input. If so, I suggest the following: use a textbox (or an AutoComplete if you have some suggestions to show your user) and its OnChange event will take the user input and add it to the data list use a grid to show that data list and it selection feature to mark items off it. This will also let you use paging, filtering, sorting, showing multiple columns, aggregates and performing CRUD operations easily. You could even put that user input field in the grid toolbar. Regards, Marin Bratanov

### Response

**khashayar** answered on 23 Feb 2020

thank you, but as a user i would prefer to have something like here [https://codepen.io/bitlani12/pen/oNXbXGY](https://codepen.io/bitlani12/pen/oNXbXGY) it would be good if your team could create this component for blazor

### Response

**Marin Bratanov** answered on 23 Feb 2020

Have you considered the MultiSelect component we have: [https://demos.telerik.com/blazor-ui/multiselect/overview?](https://demos.telerik.com/blazor-ui/multiselect/overview?) With its OnRead event, you can add the current user input (the filter) to the data source so the user can select it: [https://docs.telerik.com/blazor-ui/components/multiselect/events#onread.](https://docs.telerik.com/blazor-ui/components/multiselect/events#onread.) Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 23 Feb 2020

Here's an example I made for you: <TelerikMultiSelect Data="@Options" @bind-Value="@TheValues" OnRead="@AddCurrentItem" Filterable="true" />
<br />
selected values
<ul>
@foreach ( var item in TheValues)
{
<li>@item</li>
}
</ul>

@code{
List<string> TheValues { get; set; }=new List<string>();
List<string> Options { get; set; }=new List<string>(); async Task AddCurrentItem ( MultiSelectReadEventArgs args ) { if (args.Request.Filters.Count> 0 ) // there is user filter input, skips providing data on initialization {
Telerik.DataSource.FilterDescriptor filter=args.Request.Filters[ 0 ] as Telerik.DataSource.FilterDescriptor; string userInput=filter.Value.ToString();
Options=new List<string> { userInput };
}
}
}
