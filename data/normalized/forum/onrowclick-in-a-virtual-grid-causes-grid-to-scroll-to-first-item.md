# OnRowClick in a Virtual Grid Causes Grid to Scroll to First Item

## Question

**Joh** asked on 30 Oct 2023

I'm still new to these components, but when any On***Click event is fired on the Grid, when using GridScrollMode.Virtual, the Grid scrolls back to top. This only happens when using virtual scrolling. I don't know if the Grid is rerendered or just scrolls up, it's hard to know. Feels like a bug, as it works well when not using virtual scrolling. I've tried setting the args.ShouldRender=false, without any luck.

## Answer

**Johan** answered on 30 Oct 2023

I found out the reason - the data model for the grid used a readonly getter, which for some reason got re-rendered every now and then actually. Why it behaves like this for virtual scrolling grids I have no idea. I thought it was a nice solution because the underlying collection is a 2-D array of strings and I converted the grid data model to a list of ExpandoObject via the getter. When let the grid data model be a "normal" property it works without re-rendering. Phew!
