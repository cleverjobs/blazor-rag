# Hierarchical grid structure and OnStateChanged

## Question

**Pet** asked on 16 Jun 2021

I've got a hierarchical grid structure and I want to use the OnStateChanged event in the (0...N) child grids and do things with the state of the grid that has changed, but it seems impossible because there doesn't appear to be a way to work out which child grid is firing the event. Within OnStateChangedHandler(GridStateEventArgs<T> args), args doesn't contain a reference back to the grid that's changed. Obviously the top-level parent grid is easy enough, but I'm completely stumped with the children... Has anyone succeeded in doing this?

## Answer

**Marin Bratanov** answered on 17 Jun 2021

Hi Peter, I think the way to solve this is to use a lambda expression to pass more arguments to your handler that will identify the grid you want to work with. This will probably apply to the OnStateInit event as well. You can use the context of the DetailTempalte to uniquely identify the model that this grid is a child of to know what to save/load. You can find similar examples here (they are for editing but the concept is the same). Regards, Marin Bratanov
