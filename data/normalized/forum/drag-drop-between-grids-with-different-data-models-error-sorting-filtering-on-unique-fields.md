# Drag & Drop Between Grids with Different Data Models / Error Sorting & Filtering on Unique Fields

## Question

**Pet** asked on 12 Jun 2023

Good Day, I have been implementing drag&drop functionality between two Telerik Blazor grids using different data models. Using the documentation article as a reference below, I am able to get 2 models (derived from the same interface) to drag between 2 grids. How to Drag and Drop Different Models between Multiple Grids - Telerik UI for Blazor However, grid functions such as sorting and filtering start throwing errors, when unique fields are introduced per model. To re-produce, start with the demo code in the artcile and try and sort "Unique Field 1". This throws an exception: "Unhandled exception rendering component: Invalid property or field - 'UniqueField1' for type: IParentSampleData". See screenshot attached. This makes sense, but it's very limiting. My question is, if this can "worked around" in any way. I have tried to intercept the "StateChanged" event. But as I still need to call gridObj.SetStateAsync(args.GridState), I cannot circumvent the issue. As per the error, I assume that these Grid methods use the interface definition and not the actual model instance to determine available properties for filtering & sorting, etc. Is there somethig I am missing? Would anyone have any experience with this scenario and could point me in the direction of a "work around" if one exists? Many thanks, Peter

## Answer

**Nadezhda Tacheva** answered on 15 Jun 2023

Hi Peter, You are correct in your assumption. Unfortunately, I am not able to provide a workaround to get the built-in sorting to work for unique property names in this scenario. The only option that comes to my mind is to disable the built-in sorting for these fields and implement custom sorting for them. You can use a HeaderTemplate to render the header in a custom element and handle its onclick event. Upon click in the header, sort the Grid data in the needed way and refresh the Grid. In addition, you can conditionally declare an icon component in the HeaderTemplate to indicate the sort direction to the user. I hope you will find this information useful. Regards, Nadezhda Tacheva
