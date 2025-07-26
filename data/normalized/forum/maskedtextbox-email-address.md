# MaskedTextBox: Email Address

## Question

**Joe** asked on 14 Jul 2025

How do none of your documentation examples show how to ensure a valid email address is entered? How do I enforce the a@aaa.aa format?

## Answer

**Dimo** answered on 14 Jul 2025

Hi Joel, The MaskedTextBox component is designed for string values and masks of a known fixed length. Emails normally vary in length, so the MaskedTextBox is not a suitable component. Instead, you can consider a regular TextBox component with a regex validation rule. Regards, Dimo Progress Telerik
