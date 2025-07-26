# DefaultText Selection doesn't hit ValueChanged Event

## Question

**Rog** asked on 30 Jan 2020

The ValueChanged event doesn't fire when the DefaultText item is selected. I have a dropdown containing associate names and I want the user to be able to remove the selected associate and choose the empty one (DefaultText). The ValueChange event will make an API call to remove the associate's id from the record. In my example the type for Value is int?. <TelerikDropDownList Class="tlk-dd-sm tlk-dd-bg-white w-100" Data="@associates" ValueField="AssociateId" TextField="FullName" ValueChanged="@((int? i)=> WorkItemAssigneeChanged(i, workItem))" Value="@workItem.AssignedToAssociateId" DefaultText="" />

## Answer

**Marin Bratanov** answered on 30 Jan 2020

Hi Roger, The following worked fine for me (there must be some text in the DefaultText parameter in order for it to work) and I am also attaching to this post a video of the expected behavior as a reference: @result
<br />
<TelerikDropDownList DefaultText="none" Data="@myDdlData" TextField="MyTextField" ValueField="MyValueField" Value="selectedValue" ValueChanged="@((int? i)=> WorkItemAssigneeChanged(i))">
</TelerikDropDownList>

@code { string result; void WorkItemAssigneeChanged ( int? i ) {
result=$"selection is {i} at {DateTime.Now} ";
} //in a real case, the model is usually in a separate file //the model type and value field type must be provided to the dropdpownlist public class MyDdlModel { public int MyValueField { get; set; } public string MyTextField { get; set; }
}

IEnumerable<MyDdlModel> myDdlData=Enumerable.Range( 1, 20 ).Select(x=> new MyDdlModel { MyTextField="item " + x, MyValueField=x }); int? selectedValue { get; set; }=3; //usually the current value should come from the view model data } If this does not help you move forward and get the desired behavior, could you modify this sample to showcase the problem so I can investigate? Regards, Marin Bratanov

### Response

**Roger** answered on 30 Jan 2020

Thanks for the response. I was able to find what was causing my issue. When I was testing the firing of the event, I had commented out the line of code that was updating the Value the dropdown was bound to. This makes sense because the DefaultItem would have been null and the Value would have been null, therefore the event wouldn't fire because it was the same. I thought the backend value was being updated because the text would change in the dropdown when I selected a different item even though the bound value was never being set. I just downloaded version 2.7 and the text doesn't change anymore when I select a different item in the list without updating the bound value. But in the previous version 2.6.1 it does. All is working as expected now, Thanks, Roger
