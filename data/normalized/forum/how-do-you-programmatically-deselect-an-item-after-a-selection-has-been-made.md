# How do you programmatically deselect an item after a selection has been made?

## Question

**Dou** asked on 13 Oct 2021

I have an EditForm with a DropDownList (among other things) and when my OnValidSubmit fires I do what I need to do and then I want to clear the controls so the user can select different values and submit again. The problem is the drop down doesn't clear when I set the selected value to null. I wrote a test app to demonstrate it. When the app loads nothing is selected. If you select the item in the drop down and then click the "clear selection" button it doesn't clear. What do I need to do to make that work? @page "/" <br /> <TelerikButton OnClick="@ClearSelection">Clear selection</TelerikButton> <TelerikDropDownList Data="@data" @bind-Value="selectedValue" /> @code { List<string> data=new() { "selection" }; string selectedValue; void ClearSelection() { // This does not cause the drop down to deselect the selected item selectedValue=null; StateHasChanged(); } }

## Answer

**Hristian Stefanov** answered on 18 Oct 2021

Hi Doug, We have the following knowledge base article regarding the scenario you have: Clear the value (selection) of a combobox, dropdown, input In short, the article shows how you can clear the selection of input by changing its Value parameter to the default value for its type (or to a desired other value). On the other hand, if you want a completely empty default selection without any default text, you can add some additional CSS rules for display. I added such styles to the provided code snippet: <br /> <TelerikButton OnClick="@ClearSelection"> Clear selection </TelerikButton> <TelerikDropDownList Data="@data" @bind-Value="selectedValue" DefaultText=" " /> @code {
List <string> data=new() { "selection" };

string selectedValue;

void ClearSelection()
{
selectedValue=default;
}
} <style>.k-list.k-item.k-state-selected,.k-list-optionlabel.k-state-selected,.k-list-optionlabel { display: none;
} </style> I hope this helps. If you have any other concerns, please let me know. Thank you. Regards, Hristian Stefanov

### Response

**Doug** commented on 27 Oct 2021

Hristian, Thanks for the response, however I was already doing what the KB article says to do. Setting a string to null is the same as setting it to "default" because the default for strings is null. The difference is the default value. The article is slightly misleading when it says this: "... when the Value matches the default value for its type, the Telerik component will show the placeholder automatically ( if one is set )." This doesn't work if you don't have a placeholder set. It doesn't clear the selection. I don't like how Telerik uses the default value in drop down lists because it basically just adds it as an additional item in the drop down. The user shouldn't be able to select the default value (or at least there should be an option whether to allow the user to select it as I guess I can see scenarios where you would want that). But in my case, when the component loads, nothing is selected, and I'd like to be able to get back to that state but apparently I can't do that without messing around with CSS which seems rather messy to me. I suppose I should create a feature request to have the drop down list clear the selection when the bind value gets set to null (or the default) and there's no default value set.

### Response

**Hristian Stefanov** answered on 01 Nov 2021

Hi Doug, Thank you for making a public item in our Public Feedback Portal regarding the described scenario. I completely understand the point of view you are sharing, and the behavior can even be interpreted as a bug. This is why I changed the type of the item to "Bug report" and also changed the status to "Unplanned". DropDownList should clear selection when bind value is set to null (or the default) and no default value is set We prioritize bug reports depending on interest. With your vote already added to the public item, the item's popularity is increased. The status of the item means that the reported problem is a confirmed bug, and we have it in our backlog. Since you are the creator of the post, you are automatically subscribed to receive email notifications on status updates. Regards, Hristian Stefanov
