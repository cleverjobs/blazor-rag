# ComboBox: How to prevent Text entry

## Question

**Joe** asked on 15 May 2025

How do I prevent the user from typing text into the text field in the combobox? <TelerikComboBox @bind-Value="@SessionOptionIndex1" Data="@SessionOption1Items" ShowClearButton="false" TextField="Name" ValueField="Id" />

## Answer

**Anislav** answered on 16 May 2025

Hi Joel, If you want to prevent the user from typing into the text field, you should use the TelerikDropDownList component instead of the TelerikComboBox. The TelerikComboBox is designed to allow typing and even custom value entry (if enabled), whereas the TelerikDropDownList is strictly for selecting from predefined options and does not allow user input. Regards, Anislav Atanasov

### Response

**Hristian Stefanov** answered on 16 May 2025

Hi all, Indeed, the TelerikDropDownList component is more suitable for scenarios where you don't want users to type in the input. One of the main purposes of the ComboBox is to allow typing to help users find a specific item. However, if you still prefer to use the ComboBox, you can prevent typing by using a small JavaScript function — similar to the example shown here: How to Restrict Numeric Input in ComboBox. Regards, Hristian Stefanov Progress Telerik
