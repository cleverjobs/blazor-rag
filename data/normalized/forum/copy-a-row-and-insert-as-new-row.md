# Copy a row and insert as new row

## Question

**Pon** asked on 01 Jun 2023

Hi, I'm using the TK UI for Blazor Grid. This is the table: First Name Last Name Height Position Points per game Stephen Curry 191 Point Guard 28 Klay Thompson 201 Shooting Guard 21 I have created an add new item method which allows me to enter all fields manually. Is there a way in TK to copy e.g the first row and paste it to the open form? Of course, we have around 50 columns in real world and our Users find it exhausting to manually enter all fields. Thanks for any hint

## Answer

**Dimo** answered on 05 Jun 2023

Hi Ponlu, The desired behavior is possible to implement with Grid row selection and/or custom Copy/Paste buttons: Use the SelectedItemsChanged event or the SelectedItems parameter, or a custom Copy button, or a CommandButton to get the data item values to copy. Use a custom Paste button in the new row to set the "copied" values. It is not possible to directly use standard browser commands such as Ctrl+C and Ctrl+V, unless the user is copying a single value. Regards, Dimo
