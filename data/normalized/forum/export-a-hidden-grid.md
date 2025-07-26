# Export a hidden grid

## Question

**Dea** asked on 21 Oct 2021

Is there a way to hide a grid on the page, but still allow for export to Excel the "easy way" - using the ExportToExcel command? For example, can this command be called by another button?

## Answer

**Marin Bratanov** answered on 23 Oct 2021

Hello Dean, If you hide a grid the Blazor way (e.g., an @if(condition){<Grid>}, it will not render at all and so it could not be exported. If you hide it with CSS alone, that might work, but it is a bit of an overkill. You may want to Vote for and Follow this enhancement idea for a programmatic export call, but it will still require a grid to be instantiated. If you don't want the grid, I can suggest you generate the exportin you separate application code, the Document Processing Libraries we offer let you do that. You can find a basic example here. Regards, Marin Bratanov Progress Telerik

### Response

**Dean** commented on 26 Oct 2021

What's the CSS way of hiding it? Do you have an example?

### Response

**Marin Bratanov** commented on 26 Oct 2021

Just set a Class to it and in it - the display:none; rule

### Response

**Dean** commented on 27 Oct 2021

Sorry if I'm missing something but I get an error when adding a class to either a TelerikGrid or a GridColumn - it says it's not allowed. I'm a couple of versions behind, has this been added recently?
