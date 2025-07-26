# Hide or disable the GridCheckboxColumn for some rows

## Question

**Jas** asked on 29 Jul 2022

We don't want users to be able to select some rows, so we want to disable the checkbox on GridCheckboxColumn. I do realize this is a bit more complicated since it deals with row selection. We are using it to add selected items to a shopping cart. Some items are not for sale, so they cannot be added in bulk this way. So in this use case, we don't want them selecting the row. Any suggestions? We are open to other ways to handle this, but we wanted to avoid having the user click on something and then have it say "No you cannot do that."

## Answer

**Dimo** answered on 03 Aug 2022

Hi Jason, My suggestion is: Use the OnRowRender event to apply custom CSS class to specific rows. Then, use this class in custom CSS code that hides specific checkboxes ( <input class="k-grid-checkbox" /> ). Use the SelectedItemsChanged event to have full control over the selected rows (e.g. if the user selects multiple rows at the same time you will remove the "disabled" ones in the handler). Regards, Dimo
