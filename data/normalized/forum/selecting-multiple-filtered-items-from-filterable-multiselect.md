# Selecting multiple filtered items from filterable MultiSelect

## Question

**Ram** asked on 16 Mar 2023

Hello, it seems that selecting multiple items from a filterable MultiSelect can be quite a pain if you want to select items that are filtered. I have adapted the snippet from your documentation to show the problem I'm currently facing with a user request: [https://blazorrepl.telerik.com/cRaRPKvP25KEN0xs54](https://blazorrepl.telerik.com/cRaRPKvP25KEN0xs54) by making the dropdown not close automatically and be Contains filterable. If the user wants to select all items containing the number 3 from the list it might go something like this: User types 3 into the input box. Multiselect shows items containing 3. User selects an item from the filtered options. Multiselect adds the chosen item to the list of selected items and clears the filter. User now has to type 3 again to filter the multiselect again etc. So the "clear the filter after user selects item" is the problem here. Is there any way to avoid this, or select multiple items in "one go" from the list of filtered items?

## Answer

**Dimo** answered on 21 Mar 2023

Hello Rami, Indeed, the current behavior doesn't look optimal for the user and we have already included it in our short-term backlog for fixing. We may even include the fix for the next release 4.2.0, due in late April. Regards, Dimo

### Response

**Rami** commented on 21 Mar 2023

Hello Dimo, thank you for the reply and I hope you are able to improve on this behaviour.

### Response

**Rami** commented on 28 Apr 2023

I had a look at [https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-4-2-0](https://www.telerik.com/support/whats-new/blazor-ui/release-history/ui-for-blazor-4-2-0) and tried the REPL after updating it to the 4.2.0 release, but it seems that this item didn't make the cut. Is there anywhere I can follow this or do I just have to keep checking after every release?

### Response

**Dimo** commented on 28 Apr 2023

Yes, Rami, here - Filter text is cleared when you select an item
