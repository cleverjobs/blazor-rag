# Notification overlaps Textbox

## Question

**Hen** asked on 18 Jul 2023

Even if the TelerikNotification Component is not visible it kind of blocks the Textbox for getting focused. I made a screenshot to demonstrate that with the BrowserTools. I only can focus the Textbox if I am clicking in the area marked with the red box. Is there a solution for it ?

## Answer

**Georgi** answered on 18 Jul 2023

Hi, Hendrik I have investigated the provided screenshot and I have noticed that there is a height and width explicitly set. By default, the k-notification-group element does not have any dimensions and is resized dynamically when new notifications are added. In the current case, due to the high z-index value, the element appears on top of the input. Hence, stopping the focus from reaching the input. If you would like to limit the height and width of the container, make sure you set the max-height and max-width CSS rules, instead. This way, when no notifications are present, the container will shrink and allow the users to freely focus the input. Alternatively, increase the z-index of the TextBox components (or their parent container directly). Additional information on the z-index rule can be found in the Notification appearance article. I have prepared a REPL example that demonstrates setting the dimensions via the max-width and max-height rules. Let me know if there is anything else I can help with. Best Regards, Georgi Progress Telerik

### Response

**Hendrik** commented on 18 Jul 2023

Hello Georgi, works like a charm ! Thank you very much !!
