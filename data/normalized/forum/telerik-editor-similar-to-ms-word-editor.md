# Telerik Editor Similar to MS-Word Editor

## Question

**Sus** asked on 23 Aug 2023

Hello Team, I have a requirement where I need to use microsoft word editor in blazor front end application. I found the closest component to it is the TelerikEditor. But it has a lot of limitations (like pages, columns, mail merge fields, footers etc). So, I need to do some customizations in the telerik editor ( [https://blazorrepl.telerik.com/QRkMwdvc41pMT93w35](https://blazorrepl.telerik.com/QRkMwdvc41pMT93w35) ). On initial research, I found that there is a library, Blazor Dev Express ([https://docs.devexpress.com/Blazor/401891/components/rich-text-editor)](https://docs.devexpress.com/Blazor/401891/components/rich-text-editor)) that offers an editor similar to that of ms-word. Is there any similar editor in Telerik UI for Blazor or is anything similar coming up soon in future upgrades?

## Answer

**Dimo** answered on 28 Aug 2023

Hello Susan, Indeed, the Editor component is designed to work with web content. You need a different component that works with page (paper) content and which our Blazor suite still doesn't have, namely - the RichTextBox. I voted for the feature request on your behalf and you can follow it to receive status updates. In the meantime, you can review our Document Processing library and specifically, WordsProcessing. This tool allows you to convert HTML to DOCX and vice versa. You can also produce or edit Word documents with it. So, a possible alternative to the RichTextBox may be some integration between the Editor in the front-end and WordsProcessing in the back-end. Regards, Dimo Progress Telerik
