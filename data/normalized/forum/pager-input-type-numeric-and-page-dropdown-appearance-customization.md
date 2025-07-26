# Pager input type numeric and page dropdown appearance customization

## Question

**Con** asked on 03 Nov 2023

Is it possible to customize the appearance of input and page size dropdown controls in the TelerikPager control or the pager of the TelerikGrid control? Our application uses the Material theme and all controls are using the Outline FillMode but I cannot change the Pages dropdown control of the grid's default pagger. I can use the GridPagerTemplate to change the default pager with a customized one but still the TelerikPager control does not allow configuration of the TelerikNumericBox control behind the PagerInput control and the TelerikDropDownList behind the PagerDropDownList control.

## Answer

**Dimo** answered on 07 Nov 2023

Hello Constantinos, Indeed, the way to proceed is to use a PagerTemplate with manually defined NumericTextBox and a DropDownList. Another option (that will work for the standalone Pager component too) is to override the styles of the components inside the pager. Remove the background color and apply a border. Regards, Dimo Progress Telerik

### Response

**Constantinos Petridis** answered on 10 Nov 2023

Thank you for the answer, I will also post a feature request to have the ability to customize the appearence of the pager's containing controls.
