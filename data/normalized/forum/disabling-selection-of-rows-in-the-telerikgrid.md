# Disabling selection of rows in the TelerikGrid

## Question

**Afr** asked on 10 Apr 2023

Hi, I am using telerikgrid control to present my data on the page. I am using a header GridCheckboxColumn to select the rows. I want to put a condition so that some rows cannot be selected (disabled for selection). Please can someone provide some solution for this requirement. Thanks, Afreen

## Answer

**Hristian Stefanov** answered on 13 Apr 2023

Hi Afreen, In order to achieve the desired result, you can use the SelectedItemsChanged event, which will give you the current selection in the grid. Then, compare it with the current one, employ the desired business logic to determine what needs to remain selected, and set that to the SelectedItems collection of the grid. I'm at your disposal if further assistance is needed. Regards, Hristian Stefanov Progress Telerik
