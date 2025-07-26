# Generically typed context in templates

## Question

**Kas** asked on 25 Jun 2020

Hi, I noticed that the context variable in templates is of type object (e.g. in the drop-down-list, grid-column). Is this due to historical reasons? Could this be changed to a generically typed context? Regards Kasimier Buchcik

## Answer

**Kasimier Buchcik** answered on 25 Jun 2020

My bad, the drop-down-list actually uses a generically typed template. So do all the components already use generically typed templates (when possible) and the grid-column template is an exception? While migrating to Blazor I did went through only a fraction of components. Can we expect that all templates will be generically typed in the future? Regards Kasimier Buchcik

### Response

**Svetoslav Dimitrov** answered on 25 Jun 2020

Hello Kasimier, Most of our contexts are generic and that will continue in the future. We make it for the convenience of not having to cast it on your own. That being said, there are some where casting an object to the desired type is needed, for example in the TreeView for better hierarchical support, the Grid's Template and EditorTemplate. Regards, Svetoslav Dimitrov
