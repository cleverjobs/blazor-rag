# DateTimePicker, DatePicker and TimePicker does not work correctly within a Boostrap Modal

## Question

**Dan** asked on 02 Nov 2023

Hi, I ́ve tried the DateTimePicker, DatePicker and TimePicker and they all work great but not when I put them inside a Boostrap Modal. If I have a TextBox followed by a DatePicker inside an opened Bootstrap Modal and then click the calendar icon in the DatePicker the TextBox gets focused. Is there a way around this behaviour? /Daniel

## Answer

**Georgi** answered on 07 Nov 2023

Hi, Daniel, In general, the Bootstrap modal doesn't allow any element outside of it to receive focus. However, the popups of our components are not rendered in their place of declaration but as a child of the TelerikRootComponent at the root of the Blazor app. This results in them being outside of the Bootstrap modal. There are a few ways to get out of this situation: Check if the Bootstrap modal has a setting to allow focus outside of it. For example, Bootstrap 5 has data-bs-focus="false". If the modal does not have such a setting, you will have to replace it with our Window or another modal of your choice. Let me know if additional questions arise. Best regards, Georgi Progress Telerik
