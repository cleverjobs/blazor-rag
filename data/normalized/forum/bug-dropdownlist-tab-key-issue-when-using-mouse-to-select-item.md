# Bug: DropDownList Tab Key Issue When Using Mouse To Select Item

## Question

**Ind** asked on 03 Feb 2023

How to reproduce: 1. Select an item in the DropDownList using mouse. 2. Press tab to go to the next field. Focus should go to the next field. Instead focus goes back to the first field. I modified REPL from your demos, adding textboxes to reproduce the issue. demo 1: [https://demos.telerik.com/blazor-ui/dropdownlist/templates](https://demos.telerik.com/blazor-ui/dropdownlist/templates) modified REPL: [https://blazorrepl.telerik.com/cHawYHPd47d0122o27](https://blazorrepl.telerik.com/cHawYHPd47d0122o27) demo 2: [https://demos.telerik.com/blazor-ui/dropdownlist/virtualization](https://demos.telerik.com/blazor-ui/dropdownlist/virtualization) modified REPL: [https://blazorrepl.telerik.com/QxYmknPR49ZdbVQQ02](https://blazorrepl.telerik.com/QxYmknPR49ZdbVQQ02) I fix this focus issue using OnClose event, setting the focus to the current DropDownList with FocusAsync(). But I have to modify all the DropDownList in my projects.

### Response

**Indra** commented on 05 Feb 2023

Same lost focus issue with DateTimePicker when using mouse to select input then press TAB [https://www.telerik.com/forums/unable-to-tab-to-next-field-in-a-form](https://www.telerik.com/forums/unable-to-tab-to-next-field-in-a-form)

## Answer

**Yanislav** answered on 08 Feb 2023

Hello Indra, I've reviewed the case and the issue seems to be similar to the one discussed in the other forum discussion. I've added a comment in the logged Bug Report specifying that the behavior is also observed with the dropdown list. I have updated your Telerik points as a token of gratitude for helping us identify this issue. Also, thank you for sharing the solution you've come up with. It might be helpful for someone facing the same issue. Regards, Yanislav
