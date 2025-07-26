# Dropdownlist item removing spaces/ tabs from the text value

## Question

**Bee** asked on 12 Apr 2022

Telerik Team, Currently, I am concatenating the text field value of dropdown list to include spaces or tabs in order to show data indented as tree view. Seems like the Telerik dropdown list component is removing space or tabs. I have also tried using &nbsp; (HTML tag) to accomplish this task. But this does not seem to work as well (may be due to HTML encoding/decoding). Is there are a way I can show the list items as intended data. Thank you for your help. Beena.

### Response

**Timothy J** commented on 12 Apr 2022

Use a treeview?

## Answer

**Dimo** answered on 14 Apr 2022

Hi Beena, &nbsp; will work, but you need ItemTemplate. Also, the &nbsp; must be outside the actual model values. Since you will be using a template, you can implement the formatting (indentation) in any other way via custom HTML/CSS. Regards, Dimo

### Response

**Beena** commented on 14 Apr 2022

Hello Dimo, Yes, ItemTemplate worked for me. Added space to the textfield of the item and used HTML <pre> element to maintain formatting of text.
