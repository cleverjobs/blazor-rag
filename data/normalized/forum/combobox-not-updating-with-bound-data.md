# ComboBox not Updating With Bound Data

## Question

**Jos** asked on 14 Apr 2020

The ComboBox control does not appear to be refreshing/updating when the underlying list that it is bound to is updated. Some sample code to replicate this is: @page "/" @using Telerik.Blazor; <TelerikComboBox Data="@ComboValues" Value="@SelectedValue" ValueChanged="@((string v)=> ComboBoxSelectionChanged(v))"> </TelerikComboBox> @code { List<string> ComboValues=new List<string> { "One", "Two", "Three", "Four", "Five" }; string SelectedValue=null; void ComboBoxSelectionChanged(string v) { ComboValues.Remove(v); ComboValues.Add("New " + v); SelectedValue=null; } } Keep in mind this is overly simplistic but does demonstrate what isn't working as expected. I would expect in this case for the selected entry to be removed from the ComboBox and replaced with "New {Selected Entry}"; I had this working fine relatively recently but started updating my code after upgrading to version 2.10. Now i can't tell for sure if this is a bug introduced in version 2.10 or if i just made a change that broke things. Any feedback would be greatly appreciated. Thank You Josh

## Answer

**Marin Bratanov** answered on 15 Apr 2020

Hi Josh, To update a data source like this, it has to be an observable collection, so we can hook to its CollectionChanged event and update our component. Otherwise, the reference to the parameter (Data in this case) stays the same when you change items in the list, so the framework won't raise the OnParametersSet event, and our component cannot know the data changed. Here's a sample that worked for me to alter the data source and clean up the combo value upon selection (keep reading after the snippet, though): @using System.Collections.ObjectModel <TelerikComboBox Data="@ComboValues" Value="@SelectedValue" ValueChanged="@((string v)=> ComboBoxSelectionChanged(v))">
</TelerikComboBox>

@foreach ( var item in ComboValues)
{
<div>@item</div>
}

@code { ObservableCollection <string> ComboValues=new ObservableCollection <string> { "One", "Two", "Three", "Four", "Five" }; string SelectedValue=null; void ComboBoxSelectionChanged ( string v ) {
ComboValues.Remove(v);
ComboValues.Add( "New " + v);

SelectedValue=null;
}
} There are a couple of key problems here still, however - the ValueChanged event fires very often, much more often than it looks like at first glance - you will see that by checking how many times you enter the handler and how "extra" items get added to the data source (that's why I added the foreach loop after the combo). I would suggest using the OnChange event instead, and also adding some logic to determine when to actually do this removal and change of the value. Also, setting the Value to null will clear the combo box, you should set it to the desired value you want it to show. @using System.Collections.ObjectModel

<TelerikComboBox Data="@ComboValues" Value="@SelectedValue" OnChange="@ComboBoxSelectionChanged">
</TelerikComboBox>

@foreach ( var item in ComboValues)
{
<div>@item</div>
}

@code {
ObservableCollection<string> ComboValues=new ObservableCollection<string> { "One", "Two", "Three", "Four", "Five" }; string SelectedValue=null; void ComboBoxSelectionChanged ( object v ) { string val=v as string; // you should add logic to determine when to do this - I don't think // that you should do it every time the event fires - even with OnChange // and much less with ValueChanged ComboValues.Remove(val); string desiredValue="New " + val;
ComboValues.Add(desiredValue);
SelectedValue=desiredValue;
}
} As a general rule, I would advise providing your user with the necessary options beforehand - the main purpose of a dropdown type of control is to let the user choose something existing, and not for you to have to go and change it after they do. The built-in filtering can let people find things in long lists faster. If you do end up having to change everything, you will need to devise the necessary business logic to avoid executing the code multiple times, avoid infinite loops and missing/wrong values. Regards, Marin Bratanov

### Response

**Joshua** answered on 15 Apr 2020

Hello Marin Thank you for your response. I will modify my code as you suggested in the second example. The code snippet i provided was based upon a much earlier version of the ComboBox control and at that time the documentation specifically indicated that you could not utilize the OnChange event along with Binding to the Value parameter. I can understand how utilizing an observable collection would be a better option, but i swear this was working as I wanted with a regular List as recently as release 2.8. Are you able to confirm that the change in behavior is likely due to changes that you made in the control in recent releases? To give some background on why i'm asking, I'm making the case internally that we need to migrate from our current WebForms development to Blazor and changes like this hamper that discussion unless i can fully explain them. Again, I get an observable collection is probably the better pattern for this. In terms of your feedback on the UI, As i stated the example i provided was overly simplistic for brevity and to demonstrate the problem. I'm building a control similar to the Blazing Pizza toppings selection control with the exception that once an item is selected from the ComboBox it should no longer be a selection and thus should be removed from the ComboBox. After a selection has been made in the ComboBox a button for the selection is added right below the ComboBox and the ComboBox is cleared to allow for additional selections. Conversely, if they click on the button to remove the selection, that option should be added back into ComboBox. This is all very similar to the Multiselect box, but that doesn't quite meet our needs nor does it fit as nicely within the rest of our UI. Thank you again for your feedback. Josh

### Response

**Marin Bratanov** answered on 15 Apr 2020

Hi Josh, The DropDownList didn't have an OnChange event but we added it, just to allow an event and two-way binding. With the combo it was always possible. If something is not clear about this in the docs, could you point it out to me so I can fix it? On a change in behavior - we did make some fixes and performance improvements across the board, and we've had reports that some people have exploited those bugs to update the data in a similar fashion. It might have been around 2.8.0 or 2.9.0, indeed. It should never have worked in the first place, though. On the particular scenario: indeed, and ObservableCollection is the way to do this data source change. Another way is to new up the collection so its reference changes in a fashion similar to this sample app but I feel like it's more work and unnecessary requests. in your case setting the value to null would be correct, I had misunderstood the comments around it and I wanted to make sure we are on the same page regarding how things work Regards, Marin Bratanov

### Response

**Joshua** answered on 16 Apr 2020

Marin, Nothing wrong with the docs, like i said this was some time ago and the controls and docs have since changed and i never updated my code along with it. Thank you very much for the feedback on the changes. Helps to alleviate the concern that there is going to be too many changes in a new platform if we weren't doing something right to begin with and it just happened to work. Josh
