# Grid which can accept multiple data types

## Question

**Gui** asked on 24 Oct 2022

Hello, in our application we have a grid which uses Auto Generate Columns. Right now we're only using one type but we want it to accept a generic object which can one of a few types and have it automatically generate the columns for it so we don't need to make a grid for each type. Is this possible or do we need the make multiple grids?

## Answer

**Nadezhda Tacheva** answered on 27 Oct 2022

Hi Guido, By design, when using the automatic column generation, the Grid will generate a column for each public property of its model so you do not have to declare the columns manually. However, it needs to work with a collection of a specific model, so it can know what columns to render. If you bind the Grid to a collection of objects which includes different model instances, it will not be able to get the properties in order to generate the columns. In summary, it is not possible to pass different models to the Grid. However, if the models are somehow related, it is possible to nest them and bind the Grid to nested (navigation) properties in complex objects. I hope you will find this information useful. Please let us know if additional questions appear. Regards, Nadezhda Tacheva
