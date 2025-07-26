# How to add TelerikDropDownList to Wizard?

## Question

**Ale** asked on 12 Jan 2022

Even in the demo example, it shows Country as a textbox instead of a dropdown. How to integrate a dropdown with the telerik form in the wizard?

## Answer

**Marin Bratanov** answered on 15 Jan 2022

Hi Alex, The Form component by itself can use a dropdown only for Enum values, as this is the only case it can know what the possible values are. For other situations you must use its item template. Thus, the form in the wizard will have the same behavior. Regards, Marin Bratanov
