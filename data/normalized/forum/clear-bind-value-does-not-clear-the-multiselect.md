# Clear bind-Value does not clear the multiselect

## Question

**Fre** asked on 02 Nov 2020

When clearing the bind-Value the multiselect still has the values previously selected. Is there another way to clear the multiselect?

## Answer

**Joana** answered on 02 Nov 2020

Hi Fredrik, The Value of the MultiSelect component is of type List<TValue>. However, any manipulations applied to the list do not trigger the Blazor lifecycle for update of the parameter as the reference of the list remains unchanged (for example: .Clear(), .Add()). That being said, you need to reinitialize the list of values in order to make sure that the Multiselect will be updated accordingly: <div> <button @onclick="@OnClick"> Clear MultiSelect Values </button> <TelerikMultiSelect Data="@Sports" @bind-Value="@Values" Placeholder="Select sports" Width="350px" /> <div> Selected Sports: <strong> @string.Join(", ", Values) </strong> </div> </div> @code {
List <string> Sports=new List <string> () {
"Baseball",
"Basketball",
"Cricket",
"Field Hockey",
"Football",
"Table Tennis",
"Tennis",
"Volleyball"
};
List <string> Values=new List <string> ();

private void OnClick()
{
Values.Clear();
}
} We understand that the type of the value is restrictive, and we have a logged feature request to update its type: [https://feedback.telerik.com/blazor/1478998-change-telerikmultiselect-value-to-type-icollection-t-or-ilist-t](https://feedback.telerik.com/blazor/1478998-change-telerikmultiselect-value-to-type-icollection-t-or-ilist-t) Once we support binding to ObservableCollection of values, you will be able to update the set of values through it. Let me know if you have further questions. Regards, Joana
