# Force 2 Decimal Places For all NumericTextBoxes

## Question

**ZeeZee** asked on 27 Mar 2021

Hi, How do I set the default number of decimal places for all "NumericTextBoxes" to 2. Currently all NumericTextBox decimal places are default to 3. I have multiple Grids with decimal columns which can be edited Inline. <GridColumn Field="@nameof(Item.Price)" Title="Price" DisplayFormat="{0:N2}" /> All numeric textboxes in edit mode are set to 3 decimal places. Why is the default three decimal places?

## Answer

**Marin Bratanov** answered on 29 Mar 2021

Hello Zee, The Format (for example, currency), decimal separator, group separator and default number of Decimals are taken from the current culture. Thus, whether it will default to 2 or 3 decimals is up to the app. You can read more on how our components handle the culture of the app here. That aside, you can set the Format and Decimals parameters of the numeric textbox as required by your app and set the decimal places there, instead of relying on the app culture. To do that in a grid, use the editor template of the column. Regards, Marin Bratanov Progress Telerik
