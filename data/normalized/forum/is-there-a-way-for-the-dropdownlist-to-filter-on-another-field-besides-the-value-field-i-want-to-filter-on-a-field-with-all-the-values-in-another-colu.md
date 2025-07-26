# Is there a way for the dropdownlist to filter on another field besides the value field? I want to filter on a field with all the values in another column I have provided in column of database

## Question

**joh** asked on 27 Oct 2023

Basically I would like to be able to use a dropdownlist where the user can insert a customer name, number, or email and filter on a column (property) provided by the database or myself in the class. But when the item/customer is selected...the name field is the only thing displayed. Right now I have to set the value field to my big column in order to filter properly. Hopefully this makes since. Was hoping to have a manual filtering/data control option like on a grid, but I do not see this available at the moment. Kind of like on the grid where I can use the search box and control what fields are filtered on. The only way I can think of now is to add a textbox in front and use that as the barcode/search option and manually filter the data behind. Similar to how quickbooks desktop allow the user to put in the barcode or the name of a product, but the display selection on only shows the product name.

## Answer

**Nadezhda Tacheva** answered on 31 Oct 2023

Hi John, It is possible to customize the filtering in the DropDownList in order to achieve the desired result. For that purpose, you have to bind the component with the OnRead event, so you can programmatically change the data request filter. You can find more information and an example in this article: Dropdown Search in Multiple Fields. I hope this will help you move forward with your application. Regards, Nadezhda Tacheva Progress Telerik
