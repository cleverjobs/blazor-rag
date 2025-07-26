# Limit # of items that can be selected

## Question

**Rog** asked on 18 Mar 2020

Is there a way to limit the number of items that can be selected in a MultiSelect component?

## Answer

**Svetoslav Dimitrov** answered on 19 Mar 2020

Hello Roger, Yes, you can limit the total count of selected items in several ways: Use if / else statement to limit the Count (Below you can see a code snippet) In the following article, you will find two other approaches: [https://docs.telerik.com/blazor-ui/knowledge-base/multiselect-always-select-item-limit-total:](https://docs.telerik.com/blazor-ui/knowledge-base/multiselect-always-select-item-limit-total:) you can control what gets added to the list with your own code through the component events you can use forms validation to prevent form submission and easily show messages to the user Of course, you can combine the three approaches. Code snippet for if / else statement: This code snippet will show you how to limit the Count property of the C# List Render the component if the Count is below certain amount Render a custom message / component if the Count is over the predefined amount <h4 class="text-info"> Select multiple data </h4> @if (MySelectedItems.Count <MaximumNumberOfItems ) {
<TelerikMultiSelect Data="@Options" @bind-Value="@MySelectedItems" /> }
else
{ <div class="alert alert-danger"> You cannot select more items </div> } @if (MySelectedItems?.Count> 0)
{ <ul> @foreach (int item in MySelectedItems)
{ <li class="text-muted"> @item </li> } </ul> }

@code { int MaximumNumberOfItems=5; List <int> MySelectedItems { get; set; }=new List <int> (); List <int> Options { get; set; }=Enumerable.Range(1, 20).ToList();
} Regards, Svetoslav Dimitrov
