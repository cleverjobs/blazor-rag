# Dropdown able to Edit and Save

## Question

**Vis** asked on 19 Jul 2021

Hi Team, I need Dropdown list which is able to Edit and Save inside the dropdown. Could you please suggest on this. Thanks, Vishnu Vardhanan H

## Answer

**Matthias** answered on 19 Jul 2021

Hi Vishnu, I think you are talking about combobox? Try this: <TelerikComboBox Data="@_List" @bind-Value="aItem" Placeholder="press return to add a new item" AllowCustom="true" OnChange="@OnChangeHandler"> </TelerikComboBox> @code {
ObservableCollection<string> _List { get; set; }=new ObservableCollection<string>(); protected string aItem { get; set; }="one"; protected override async Task OnInitializedAsync ( ) {
_List.Add( "one" );
_List.Add( "two" );
_List.Add( "three" ); await InvokeAsync(StateHasChanged);
} private void OnChangeHandler ( object theUserInput ) {
newItem=theUserInput !=null? Convert.ToString(theUserInput) : ""; if (! string.IsNullOrEmpty(newItem) && !_List.Contains(newItem))
{
_List.Add(newItem);
StateHasChanged();
}
}

} the user can write in the combobox, hit return and then the new item is in the list if you want to edit the item - I would use a textbox outside of the list, or after editing in "OnChangeHandler" ask the user, if the item is new or changed Best regards Matthias
