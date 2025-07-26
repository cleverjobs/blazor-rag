# ComboBox & DropDownList virtualization (remote data)

## Question

**Con** asked on 29 Nov 2021

I have a ComboBox or a DropDownList that gets data from a remote service, using virtualization. When the PageSize property is big enough (in my case 20), I have issues scrolling up the selection box drop down list, it tries to scroll but then resets to the current selected item making it almost imposible to scroll up. You can use your own demo examples to replicate this issue. To reproduce the issue, try the ComboBox - Virtualization, in Telerik REPL ( Demo ), change the PageSize from 10 to 20. Then open the combo box, scroll a couple of pages down and select a value. Reopen the combo and try to scroll (with mouse wheel) upwards, it will return to the selected value and will not allow you to reach the top of the item list.

## Answer

**Hristian Stefanov** answered on 02 Dec 2021

Hi Constantinos, Thank you for reporting that behavior. I can confirm it is a bug. I created a bug report on your behalf on our Public Feedback Portal: ComboBox virtual scrolling breaks when you slowly scroll up after selecting an item. You are automatically subscribed to receive email notifications for status updates. I confirm that the only way to avoid the problem is to reduce the PageSize. As a small gesture of gratitude, I added Telerik points to your account. Regards, Hristian Stefanov Progress Telerik
