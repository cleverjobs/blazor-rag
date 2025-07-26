# Wrapping inline editor in a grid

## Question

**Pet** asked on 29 Sep 2022

Is it possible to just wrap the default inline grid editor with some additional markup? I want some html added inside. If not, then how do I get the tool tip validator? <GridColumn Field=@nameof(Person.Name) Context="pxxx"> <EditorTemplate> <TelerikTextBox @bind-Value=@(((Person)pxxx).Name)/> Some additional HTML here </EditorTemplate> </GridColumn> Thanks!

## Answer

**Dimo** answered on 04 Oct 2022

Hi Peter, As you correctly assume, the default editor is not exposed and cannot be wrapped / reused. In your case, add a <TelerikValidationTooltip /> inside the EditorTemplate. Also check the Telerik Validation Tools Overview. Regards, Dimo Progress Telerik
