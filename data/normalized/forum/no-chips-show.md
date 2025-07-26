# No chips show

## Question

**Osc** asked on 22 Apr 2021

Hello, Is it possible to not show the selection at all on multiselect component. I mean, I don't want to show the chips. Just the current user input or placeholder text. Thanks!

## Answer

**Oscar** answered on 22 Apr 2021

Edit: I want to add, to make sense to the question, that I will show the selecction in a different component list, so I don't need to show them twice. Also they can open the multiselect popup to unselect, cause I will put checkboxes on the popup elements to show they are selected. Thanks!

### Response

**Marin Bratanov** answered on 22 Apr 2021

Hello Oscar, If you cancel the ValueChanged event (i.e., you do not update the view-model in it), the user will see no selection. Selection will then not show up in the dropdown either. Another approach would be to use CSS to hide the DOM elements of the multiselect from the rendering selection would still happen, selected items in the dropdown will still show up, but CSS can hide the chips in the input itself. Regards, Marin Bratanov
