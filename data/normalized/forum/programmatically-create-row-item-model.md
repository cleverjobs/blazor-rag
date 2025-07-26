# Programmatically create row item/model

## Question

**Jen** asked on 22 Apr 2020

I use a MVVM approach to populate the Grid. The rows are actually viewmodels keeping state. They have no parameterless constructor, they are created by factory methos using injected services. The Grid creates the item before assigning it to the event args passed to the handler method. In my case "No parameterless constructor defined for type '...' is thrown. How can I have control on the creation of my row models?

## Answer

**Jens** answered on 23 Apr 2020

Ok, I see that one can override the default behaviour while creation (and other actions) with GridState. My post has been a little premature.

### Response

**Marin Bratanov** answered on 23 Apr 2020

Hello Jens, Indeed, a parameterless constructor is needed, and the state is a valid solution to this. I have added this to the documentation in the Notes section [https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes](https://docs.telerik.com/blazor-ui/components/grid/columns/bound#notes) Regards, Marin Bratanov

### Response

**Shabbir** commented on 12 Nov 2024

Can you share example code of the grid component working without a parameterless constructor? My attempt at Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor. doesn't work.
