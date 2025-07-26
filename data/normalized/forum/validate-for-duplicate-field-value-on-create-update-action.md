# Validate for duplicate field value on create/update action

## Question

**Oli** asked on 20 Nov 2020

Hello, Sorry if this has already been asked, but I couldnt find a topic on that subject. I would like to know if it's possible to validate for a duplicate value for a field when submitting an add/edit of a record in a grid (popup edit) and return an error in the form to inform the user that the value is already used. I am able to do it in the appropriate handle after the submit but i can't seem to prevent the form to close and to display an error message to the user. Thanks!

## Answer

**Nadezhda Tacheva** answered on 24 Nov 2020

Hello Olivier, In order to prevent the form from closing you need to modify the IsCancelled property of the event arguments in the update/edit handler. Setting its value to false will keep the grid in Insert/Edit mode and the PopUp will remain opened. This way you will also be able to display the necessary error message. More information as well as a relevant example you can find in this article - [https://docs.telerik.com/blazor-ui/components/grid/editing/overview](https://docs.telerik.com/blazor-ui/components/grid/editing/overview) and this sample project - [https://github.com/telerik/blazor-ui/tree/master/grid/remote-validation](https://github.com/telerik/blazor-ui/tree/master/grid/remote-validation) Regards, Nadezhda
