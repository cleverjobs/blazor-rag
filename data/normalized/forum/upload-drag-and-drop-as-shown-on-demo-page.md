# Upload Drag and Drop as Shown on Demo Page

## Question

**Jef** asked on 16 Jan 2023

On the Blazor Upload demo page it shows the control with a "drag and drop" option. I haven't been able to find information on the site on how to implement that. I have found a few places where it makes it sound as if that is not yet possible. Can you direct me to a location where it has further information on that feature? Thanks

## Answer

**Hristian Stefanov** answered on 19 Jan 2023

Hi Jeff, I confirm that the drag-and-drop functionality is possible out of the box for the Telerik Upload component (similar to the standard uploads). I agree that we can improve our documentation to show that better. The drop zone is the " Select files... " button. If you want to make it wider, the easiest way is to use some CSS for padding, display, width, etc. I have prepared a sample for you in this REPL link that shows the described approach. The styles are changeable based on the scenario needs. Please test the REPL by dragging an item from your computer and dropping it into the Upload zone. Let me know if the above sample suits your needs. Additionally, we have an open feature request that will allow customizing the Upload drop zone more easily, without the need for custom CSS: Custom DropTarget for TelerikUpload. I voted there on your behalf and raised the priority. Regards, Hristian Stefanov
