# ComboBoxReadEventArgs does not contain a definition for Data

## Question

**Gre** asked on 16 Feb 2022

Hello, all, I am implementing a solution to debounce the OnRead event of the TelerikComboBox using the following example: [https://docs.telerik.com/blazor-ui/components/combobox/events#onread](https://docs.telerik.com/blazor-ui/components/combobox/events#onread) [https://docs.telerik.com/blazor-ui/knowledge-base/combo-debounce-onread](https://docs.telerik.com/blazor-ui/knowledge-base/combo-debounce-onread) Apparently, the Data property is missing from the args object passed into the OnRead handler. Following the class definitions up the inheritance chain does not reveal that it is present whatsoever. Here is a screenshot of my code in progress, indicating the problem: The documentation seems to indicate that the Data property should exist, inherited from ReadEventArgs. I do not understand what could be missing here. Thanks in advance for assistance. :) I currently am using version 2.30.0 of the Telerik UI for Blazor library. Kindly, Greg

## Answer

**Gregory** answered on 17 Feb 2022

Hello again! Once again I managed to answer my own question. I hope this helps someone. By upgrading to 3.0.1 of Blazor UI I now have the Data property available. Perhaps the Data property was only recently introduced, I don't know. But this was what fixed the problem. Have a good day! -Greg

### Response

**Marin Bratanov** commented on 17 Feb 2022

Yes it was added in 3.0.0
