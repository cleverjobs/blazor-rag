# Select the only remaining option in a Filterable Combobox.

## Question

**Lel** asked on 07 Jun 2024

I have a TelerikComboBox where the Data is a list of objects with Text and Value parameters, AllowCustom="false," and Filterable="true." The user can start typing in their desired selection to narrow down the list of options in the dropdown. After a while, they will narrow the dropdown options to a single value. If they press enter, click on the item in the dropdown, press down, or finish typing the entire Text associated with that selection's Value, the selection will be made. However, if they tab to or click on the next component, the selection will NOT be made. My request is for a way to automatically select the only remaining item in the filtered dropdown list when the component loses focus.

## Answer

**Dimo** answered on 10 Jun 2024

Hello Leland, Indeed, the described behavior makes sense and we have a feature request about it: Select first filtered ComboBox item on tab when the drop down is open I encourage you to vote for it and follow it. It is quite popular, so I expect us to prioritize it for some of our next releases. Regards, Dimo Progress Telerik

### Response

**Leland** commented on 13 Jun 2024

I tried the JavaScript workaround listed. Notably `PopupClass` is no longer a Parameter of the TelerikComboBox. I'm assuming that now corresponds to ComboBoxSettings.ComboBoxPopupSettings.Class, so I tried setting that as "special-combobox". Now there are no errors, but `getComboHighligtedItem` always returns null. Were there other changes to the classes and styling of the TelerikComboBox that need to be reflected in the call to `document.querySelector`?

### Response

**Leland** commented on 13 Jun 2024

In the Chrome Developer Tools Console tab, I was able to finally get the value of the text entered into the ComboBox's TextInput with the following: document. querySelector ( '.k-input-inner[aria-expanded="true"]' ). value So I tried adjusting the the JavaScript to the following: function getComboHighligtedItem ( ) { var selItemElem=document. querySelector ( '.k-input-inner[aria-expanded="true"]' ); if (selItemElem) { return selItemElem. value;
}
} This returns the empty string, indicating that element was found but the value had previously been cleared. This can also be observed when setting a breakpoint at the start of the `Test` method from the sample code in the workaround, indicating that now the value is cleared before the ComboBox's `OnBlur` callback is triggered. So what can be done to get the workaround found in the link you provided to work? Or is there some other way make the selection when tabbing to the next component?

### Response

**Dimo** commented on 14 Jun 2024

@Leland - indeed, now the ComboBox removes its drop down content very fast on blur, so the previous workaround no longer works. I updated the public item with a new suggested approach. It's a bit more complex, but this is what we can offer while we schedule and release the feature.

### Response

**Leland** commented on 19 Jul 2024

@Dimo - Using `await Task.Delay` is flawed. If the user types a new character and then tabs before the delay, `SelectItemOnTab` will begin executing before the new `FirstFilteredItem` is available. Even if a similar delay is added to the beginning of `SelectItemOnTab`, we're back to the issue of the drop down content being removed , so `FirstFilteredItem` becomes null. Not to mention that the delay hinders responsive design, and filter times can be much larger than than any given delay for sufficiently long lists. This will be a very common issue in my use case, as the dropdown text contains both entity names and unique identifiers. New users need to be able to type in and find the entity by the common name, while experienced users will quickly type in the exact identifier and then hit tab to move to the next form item. Please keep this in mind when planning the feature schedule and release (I see it's still labeled as "unplanned" in the feedback page). In the meantime, I would appreciate it if you could give another attempt at a workaround.

### Response

**Dimo** commented on 20 Jul 2024

@Leland - indeed, the workaround relies on the user waiting for the correct item to get focus after typing. I am afraid there is no other workaround at this point.
