# Prevent ContextMenu to close when click on DatePicker

## Question

**Cla** asked on 19 Jun 2023

I have a grid with a headertemplate who raise a contextmenu to popup and allow to select a date. See for example: [https://blazorrepl.telerik.com/QxkKbZPH059REjJ030](https://blazorrepl.telerik.com/QxkKbZPH059REjJ030) Now, if i open the datepicker and click on the arrows (for select previous or next month) the context menu automatically close. Select a day or change the month or year in the datepicker does not cause this issue. I would like to allow user to click on previous/next month arrow without the contextmenu closed. Any suggestion? Thanks

## Answer

**Hristian Stefanov** answered on 22 Jun 2023

Hi Claudio, The described behavior is a known regression bug that appeared in version 4.3. Here is the public item for it: Date picker arrows in popups (e.g. Grid filter menu, context menu, etc.) prematurely close the parent popup when clicked to change the month. I voted there on your behalf and raised the priority. You can subscribe to the item to receive email notifications for status updates. Please be assured that regressions are given the highest priority in our backlog, and we will make every effort to include the fix in upcoming releases as soon as possible. In the meantime, if we come across any potential workarounds for this issue, I will promptly add them as comments to the item linked above. I remain at your disposal if we can assist with anything else. Regards, Hristian Stefanov
