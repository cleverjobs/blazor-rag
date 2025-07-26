# AutoComplete firing twice

## Question

**Kev** asked on 30 May 2023

I'm using a TelerikAutoComplete as a filter/searchbox for a Grid. I'm using the OnChange event to call a method that gets the filtered Grid data. It works great until the user clicks the (Add) button to add a new record. At this point, the OnChange event fires again because the OnChange also fires for the OnBlur. The effect is that the user clicks the Add button and they see the spinner in the TelerikLoaderContainer for a second or less, and then they have to click the button again to actually fire the event for the button. I need to move focus away from the AutoComplete after the first OnChange fires, but FocusAsync() doesn't exist for a TelerikGrid or GridCommandButton.

## Answer

**Dimo** answered on 01 Jun 2023

Hello Kevin, Moving the focus programmatically will still fire OnChange again. A better solution will be to check if the new value is the same as the old one, and in this case, abort handler execution. Regards, Dimo Progress Telerik

### Response

**Kevin** commented on 01 Jun 2023

Thanks for the reply. That's what I ended up doing.
