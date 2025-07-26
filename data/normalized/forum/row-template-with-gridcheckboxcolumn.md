# Row template with GridCheckboxColumn

## Question

**Rob** asked on 28 Nov 2019

Hi, I'm trying to implementa a RowTemplate. My grid has a GridCheckboxColumn as a first column but I don't know what to put in the first <td> element. I have tried putting <input type="checkbox" /> but context variable has no knowledge of a checked row. Any help is appreciated.

## Answer

**Marin Bratanov** answered on 29 Nov 2019

Hello Robert, When using a RowTemplate, everything in the row must be implemented by the developer. This would include not only selection, but also things like detail templates, buttons and the like. So, you would need to add a field in the model that denotes selection and bind the checkbox to it. If you want clicking the row to also invoke this, add an @onclick handler to the elements yourself that toggles this field as well. Regards, Marin Bratanov
