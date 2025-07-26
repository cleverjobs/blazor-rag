# Is it possible to set an ID attribute on inputs in grid's filter row?

## Question

**Grz** asked on 28 Jan 2022

Hello, My team would like to create E2E tests in Cypress for the grids we use and we are wondering whether it's possible to set unique ID values on the filter row. Currently, these IDs are just GUID values and we couldn't find a way to modify them. Kind regards, Greg

## Answer

**Marin Bratanov** answered on 30 Jan 2022

Hello Grzegorz, You can have the tests count the index of the column if you are looking to use DOM manipulation. We need to ensure unique IDs because otherwise we could clash with something from the page. Alternatively, you can use filter templates in the grid to define any custom rendering you want. Note, however, that this takes away the built-in functionality and could potentially be al of of work to replace if this is only for doing testing. Regards, Marin Bratanov
