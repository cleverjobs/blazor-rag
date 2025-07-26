# Hide the DropDownButtonItem after clicking it

## Question

**And** asked on 26 Nov 2024

One of the DropDownButtonItem in my TelerikDropDownButton control is Delete. The OnClick method for the Delete DropDownButtonItem uses Dialogs.ConfirmAsync to make sure that the user really wants to perform the delete. The issue is that the Delete button item is still visible when the ConfirmAsync window pops up. Depending on where the TelerikDropDownButton is on the page, the DropDownButtonItem overlaps the ConfirmAsync window. Here's an example that shows the DropDownButtonItem is visible when the popup is displayed: [https://blazorrepl.telerik.com/GylvcgFS09nqh4ZM26](https://blazorrepl.telerik.com/GylvcgFS09nqh4ZM26) Is there a way to hide the DropDownButtonItem after it is clicked?

## Answer

**Tsvetomir** answered on 28 Nov 2024

Hello Andrew, Thank you for the provided example and information about your scenario. We have an open feature request that will allow the desired behavior: Cancelable OnOpen and OnClose Events. Once these events are exposed, the desired outcome will be easily done. With that in mind, I've voted for the item on your behalf to raise its priority. In the meantime, the alternative is to use the DropDownList component. An example is shown in the linked item. Also, you can subscribe to the item to get email notifications for status updates. Regards, Tsvetomir Progress Telerik
