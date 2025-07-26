# Blazor TelerikCheckBox Name property

## Question

**Mar** asked on 29 Aug 2023

The blazor TelerikCheckBox do not implement the Name property as TelerikTextBox do instead. I need to use it in a native html form to post login values to an action for cookie authentication. Is there any way to add the name attribute?

## Answer

**Nadezhda Tacheva** answered on 01 Sep 2023

Hi Marco, The CheckBox indeed does not expose a Name property. I opened a request for it on your behalf in our feedback portal: [https://feedback.telerik.com/blazor/1622073-name-property.](https://feedback.telerik.com/blazor/1622073-name-property.) I added your vote to bump its popularity since we track the gathered votes when planning the enhancements. As a creator, you are automatically subscribed to get status updates. For the time being, a possible option is to set the name attribute of the HTML input element with JavaScript. Here is an example: [https://blazorrepl.telerik.com/GdatabEA52LKlGnv02.](https://blazorrepl.telerik.com/GdatabEA52LKlGnv02.) I hope you will find the above information useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik
